# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 00:32:28 2019

@author: ensar
"""
from TwoDimensionalAnalysisWithOOP import Node,Material,Section,Member,Structure

"""INPUT"""
N1 = Node(0,0)
N2 = Node(0,4)
N3 = Node(3,4)
N4 = Node(3,0)

Concrete = Material(1,0)

Section1 = Section(600,432,Concrete)

M1 = Member(N1,N2,Section1)
M2 = Member(N2,N3,Section1)
M3 = Member(N3,N4,Section1)
M4 = Member(N1,N3,Section1)

N2.AssignLoad('x',10)
N1.AssignSupport([1,1,1])
N4.AssignSupport('fixed')
N1.AssignSupportSettlement('z', 0)

M2.AssignUniformLoad(20)

Structure.AssignThermalLoad(0)

"""ANALYSIS"""
Structure.Analysis()

"""OUTPUT"""
K = Structure.K
F = Structure.F
u = Structure.u
R1 = N1.SupportReactions
R2 = N4.SupportReactions
F1 = M1.getInternalForces()
F2 = M2.getInternalForces()
F3 = M3.getInternalForces()
F4 = M4.getInternalForces()
