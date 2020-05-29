# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 00:32:28 2019

@author: ensar
"""
from TwoDimensionalAnalysisWithOOP import Node,Material,Section,Member,Structure

"""INPUT"""
N1 = Node(0,0)
N2 = Node(0,3)
N3 = Node(5,3)
N4 = Node(5,0)

Concrete = Material(33000000,1e-5)

Section = Section(0.15,1e-100,Concrete)

M1 = Member(N1,N2,Section)
M2 = Member(N2,N3,Section)
M3 = Member(N3,N4,Section)
M4 = Member(N1,N3,Section)

N2.AssignLoad('x',10)
N2.AssignLoad('y',-10)
N3.AssignLoad('x',10)
N3.AssignLoad('y',-10)
N1.AssignSupport('pin')
N4.AssignSupport('pin')

Structure.AssignThermalLoad(0)

"""ANALYSIS"""
Structure.Analysis()

"""OUTPUT"""
#K = Structure.K
#F = Structure.F
#u = Structure.u
#R1 = N1.SupportReactions
#R2 = N4.SupportReactions
u1 = N1.displacements
u2 = N2.displacements
u3 = N3.displacements
u4 = N4.displacements

F1 = M1.getInternalForces()
F2 = M2.getInternalForces()
F3 = M3.getInternalForces()
F4 = M4.getInternalForces()