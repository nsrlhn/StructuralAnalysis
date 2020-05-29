# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:30:33 2017

@author: ensar
"""
from TwoDimensionalAnalysisWithOOP import Node,Material,Section,Member,Structure

"""INPUT"""
N1 = Node(0,3)
N2 = Node(5,3)
N3 = Node(5,0)

Concrete = Material(33000000,0)

Section = Section(0.15,3.125e-3,Concrete)

M1 = Member(N1,N2,Section)
M2 = Member(N2,N3,Section)

N1.AssignSupport('pin')
N3.AssignSupport('fixed')

N3.AssignSupportSettlement('y',-0.001)

"""ANALYSIS"""
Structure.Analysis()

"""OUTPUT"""
u1 = N1.displacements
u2 = N2.displacements
u3 = N3.displacements

F1 = M1.getInternalForces()
F2 = M2.getInternalForces()
