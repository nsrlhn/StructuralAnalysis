# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 00:32:28 2019

@author: ensar
"""
from TwoDimensionalAnalysisWithOOP import Node,Material,Section,Member,Structure

"""INPUT"""
Nodes = []
MASS = 0,20,20,20,20,10
for II in range(6):
    Nodes.append(Node(0,II*3))
    Nodes.append(Node(6,II*3))
    Nodes[II*2].AssignMass([MASS[II],0,0])

Concrete = Material(32000000,0)

Section = Section(1e10,1.6e-3,Concrete)

Columns = []
Beams = []
for II in range(5):
    Columns.append(Member(Nodes[II*2],Nodes[II*2+2],Section))
    Columns.append(Member(Nodes[II*2+1],Nodes[II*2+3],Section))
    Beams.append(Member(Nodes[II*2+2],Nodes[II*2+3],Section))

Nodes[0].AssignSupport('fixed')
Nodes[1].AssignSupport('fixed')

"""ANALYSIS"""
Structure.Analysis()

"""OUTPUT"""
w = Structure.getPeriods()









