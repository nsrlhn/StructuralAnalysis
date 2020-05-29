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

Section = Section(0.15,3.125e-3,Concrete)

M1 = Member(N1,N2,Section)
M2 = Member(N2,N3,Section)
M3 = Member(N3,N4,Section)

N1.AssignSupport('fixed')
N4.AssignSupport('fixed')

Structure.AssignThermalLoad(10)

"""ANALYSIS"""
Structure.Analysis()

"""OUTPUT"""
u2 = N2.displacements
u3 = N3.displacements

F1 = M1.getInternalForces()
F2 = M2.getInternalForces()
F3 = M3.getInternalForces()