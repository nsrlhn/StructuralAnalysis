# Two dimansional structural frame analysis

Inputs:
  Node:
    Node(Coordinate) : Define a node
    AssignLoad(Direction, Magnitude) : Assign load to the node, direction should be 'x', 'y' or 'z'. 'z' means it is moment.
                AssignSupport(Name or Restriction) : Can be input 'fixed', 'pin' or restriction list like [1,1,0] for pin.
                AssignSupportSettlement(Direction, Magnitude) : Assign support settlement ot the node, direction should be 'x', 'y' or 'z'. 'z' means it is rotation.
                AssignMass(Mass) : Mass should be list according to global coordinate system as [x,y,z_rotation]
