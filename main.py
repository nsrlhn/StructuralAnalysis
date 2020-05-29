# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:34:45 2019

@author: ensar
"""
import numpy as np
from math import pi

Nodes = []
Members = []

class Node(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.load=[0,0,0]
        self.restriction=[0,0,0]
        self.dof=[0,0,0]
        self.displacements = [0,0,0]
        self.SupportReactions = [0,0,0]
        self.mass = [0,0,0]
        Nodes.append(self)
    def AssignLoad(self,direction,magnitude):
        if direction == 'x':
            self.load[0] = magnitude
        elif direction == 'y':
            self.load[1] = magnitude
        elif direction == 'z':
            self.load[2] = magnitude
        else: 
            raise ValueError("direction should be 'x', 'y' or 'z'")
    def AssignSupport(self,Type):
        if Type == 'Fixed' or Type == 'fixed':
            self.restriction=[1,1,1]
        elif Type == 'Pin' or Type == 'pin':
            self.restriction=[1,1,0]
        elif (Type[0]==0 or Type[0]==1) and (Type[1]==0 or Type[1]==1) and (Type[2]==0 or Type[2]==1):
            self.restriction=Type
        else:
            raise ValueError("Type should be 'fixed' or 'pin', or you can input list of restricted dof([x,y,z]) in a way that 1 for restriction 0 for free like [1,1,0] for pin")
    def AssignMass(self,mass):
        self.mass = mass
    def AssignSupportSettlement(self,direction,magnitude):
        if direction == 'x':
            self.displacements[0] = magnitude
        elif direction == 'y':
            self.displacements[1] = magnitude
        elif direction == 'z':
            self.displacements[2] = magnitude
        else: 
            raise ValueError("direction should be 'x', 'y' or 'z'")

class Material(object):
    def __init__(self,Modulus_of_Elasticity,Thermal_Expansion_Coefficient):
        self.E = Modulus_of_Elasticity
        self.c_thermal = Thermal_Expansion_Coefficient

class Section(object):
    def __init__(self,Area,Inertia,Material):
        self.A = Area
        self.I = Inertia
        self.Material = Material

class Member(object):
    def __init__(self,start,end,section):
        self.start=start
        self.end=end
        self.section = section
        self.FEM = [0,0,0,0,0,0]
        self.length = ((self.end.y - self.start.y)**2+(self.end.x - self.start.x)**2)**0.5
        Members.append(self)
    def AssignFEM(self,FEM):
        for i in range(6):
            self.FEM[i] += FEM[i]
    def AssignThermalLoad(self,dT):
        F = self.section.Material.c_thermal*self.section.A*self.section.Material.E*dT
        self.FEM[0]+=F
        self.FEM[3]-=F
    def AssignUniformLoad(self,w):
        self.FEM[2] += w*self.length**2/12
        self.FEM[5] += -w*self.length**2/12
        self.FEM[1] += w*self.length/2
        self.FEM[4] += w*self.length/2
    def AssignPointLoad(self,P,DistanceFromStartNode):
        L = self.length
        a = DistanceFromStartNode
        b=L-a
        self.FEM[2] += P*a*(b)**2/L**2
        self.FEM[5] +=-P*a**2*(b)/L**2
        self.FEM[1] += P/L*b
        self.FEM[4] += P/L*a
    def AssignMoment(self,M,DistanceFromStartNode):
        a = DistanceFromStartNode
        L = self.length
        b=L-a
        self.FEM[2] += M*b*(3*a-L)/L**2
        self.FEM[5] +=-M*a*(3*b-L)/L**2
    def stiffness_local(self):
        E = self.section.Material.E
        A = self.section.A
        I = self.section.I
        L = self.length
        return [[E*A/L,0,0,-E*A/L,0,0],
                [0,12*E*I/L**3,6*E*I/L**2,0,-12*E*I/L**3,6*E*I/L**2],
                [0,6*E*I/L**2,4*E*I/L,0,-6*E*I/L**2,2*E*I/L],
                [-E*A/L,0,0,E*A/L,0,0],
                [0,-12*E*I/L**3,-6*E*I/L**2,0,12*E*I/L**3,-6*E*I/L**2],
                [0,6*E*I/L**2,2*E*I/L,0,-6*E*I/L**2,4*E*I/L]]
    def R(self):
        cos = (self.end.x-self.start.x)/self.length
        sin = (self.end.y-self.start.y)/self.length
        return np.array([[cos,sin,0,0,0,0],
                         [-sin,cos,0,0,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,cos,sin,0],
                         [0,0,0,-sin,cos,0],
                         [0,0,0,0,0,1]])
    def stiffness_global(self):
        temp = np.matmul(self.R().T, self.stiffness_local())
        return np.matmul(temp,self.R())
    def dof(self):
        self.dof = self.start.dof + self.end.dof
        return self.dof
    def FEM_global(self):
        self.FEMg = np.matmul(self.R().T,self.FEM)
        return self.FEMg
    def getInternalForces(self):
        u_global = self.start.displacements + self.end.displacements
        u_local = np.matmul(self.R(),u_global)
        self.InternalForces = np.matmul(self.stiffness_local(),u_local)+self.FEM
        return self.InternalForces

class Structure(object):
    def AssignThermalLoad(self,dT):
        for i in Members:
            i.AssignThermalLoad(dT)
    def equationNumbering(self):
        i3 = 0
        for i in Nodes:
            for i2 in range(3):
                if i.restriction[i2] == 1:
                    i.dof[i2] = 0
                elif i.restriction[i2] == 0:
                    i3+=1
                    i.dof[i2] = i3
        self.Actives = i3
        for i in Nodes:
            for i2 in range(3):
                if i.restriction[i2] == 1:
                    i3+=1
                    i.dof[i2] = i3
        self.K = np.zeros([i3,i3])
    def createStiffnessMatrix(self):
        for i in Members:
            j2=0
            dof = i.dof()
            for i2 in dof:
                j3=0
                for i3 in dof:
                    self.K[i2-1][i3-1] += i.stiffness_global()[j2][j3]
                    j3+=1
                j2+=1
    def createForceAndDisplacementVectors(self):
        FF = np.zeros([self.Actives])
        FEM_R = np.zeros([len(self.K)-self.Actives])
        for i in Members:
            FEMg = i.FEM_global()
            dof = i.dof
            for i2 in range(6):
                if dof[i2] <= self.Actives:
                    FF[dof[i2]-1] -= FEMg[i2]
                else:
                    FEM_R[dof[i2]-1-self.Actives] += FEMg[i2]
        for i in Nodes:
            for i2 in range(3):
                if i.load[i2] != 0 and i.dof[i2] <= self.Actives:
                    FF[i.dof[i2]-1]+=i.load[i2]
        self.F = FF
        ur = np.zeros([len(self.K)-self.Actives])
        for i in Nodes:
            for i2 in range(3):
                if i.dof[i2] > self.Actives:
                    ur[i.dof[i2]-self.Actives-1] = i.displacements[i2]
        FF = FF - np.matmul(self.K[:self.Actives,self.Actives:],ur)
        uf = np.linalg.solve(self.K[:self.Actives,:self.Actives],FF)
        F_supports = np.matmul(self.K[self.Actives:,:self.Actives],uf)+np.matmul(self.K[self.Actives:,self.Actives:],ur)+FEM_R
        u = np.append(uf,ur)
        self.R = F_supports
        self.u = u
        for i in Nodes:
            for i2 in range(3):
                i.displacements[i2] = u[i.dof[i2]-1]
                if i.dof[i2] > self.Actives:
                    i.SupportReactions[i2] = F_supports[i.dof[i2]-self.Actives-1]  
    def getCondensedMatrix(self,dofs):
        K = self.K[:self.Actives,self.Actives:]
        Krr,Krc,Kcr,Kcc = [],[],[],[]
        for i in range(len(K)):
            rowr = []
            rowc = []
            for j in range(len(K)):
                k = self.K[i][j]
                if j+1 in dofs:
                    rowr.append(k)
                else:
                    rowc.append(k)
            if i+1 in dofs:
                Krr.append(rowr)
                Krc.append(rowc)
            else:
                Kcr.append(rowr)
                Kcc.append(rowc)
        return Krr - np.matmul(Krc,np.matmul(np.linalg.inv(Kcc),Kcr))
    def getPeriods(self):
        dofs = []
        m = []
        for n in Nodes:
            for d in range(3):
                if n.mass[d] !=0:
                    dofs.append(n.dof[d])
                    m.append(n.mass[d])
        mass = []
        for i in range(len(dofs)):
            row = []
            for j in range(len(dofs)):
                if i == j :
                    row.append(m[i])
                else:
                    row.append(0)
            mass.append(row)
        Kc = self.getCondensedMatrix(dofs)
        V,D = np.linalg.eig(np.matmul(np.linalg.inv(mass),Kc))
        T = []
        [T.append(2*pi/v**0.5) for v in V]
        return T
    
    def Analysis(self):
        self.equationNumbering()
        self.createStiffnessMatrix()
        self.createForceAndDisplacementVectors()
        
Structure = Structure()
