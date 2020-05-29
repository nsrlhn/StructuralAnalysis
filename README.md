# Two dimansional structural frame analysis
<sup>
Inputs:

        Node:

                Node(Coordinate) : Define a node

                AssignLoad(Direction, Magnitude) : Assign load to the node, direction should be 'x', 'y' or 'z'. 'z' means it is moment.

                AssignSupport(Name or Restriction) : Can be input 'fixed', 'pin' or restriction list like [1,1,0] for pin.

                AssignSupportSettlement(Direction, Magnitude) : Assign support settlement ot the node, direction should be 'x', 'y' or 'z'. 'z' means it is rotation.

                AssignMass(Mass) : Mass should be list according to global coordinate system as [x,y,z_rotation]

        Material:

                Material(Modulus of Elasticity, Thermal Expansion Coefficient) : Define a material

        Section:

                Section(Area, Moment of Inertia, Material) : Define a section

        Member:

                Member(Start Node, End Node, Section) : Define a member.

                AssignFEM([d1,d2,d3,d4,d5,d6]) : Assign FEM with respect to member's local coordinate system.

                AssignUniformLoad(Uniformly Distributed Load) : Assign uniformly distributed load perpendicular to the member.

                AssignPointLoad(Load, Distance from Start Node) : Assign point load perpendicular to the member.

                AssignMoment(Load, Distance from Start Node) : Assign moment load.

                AssignThermalLoad(Temperature Change) : Assign axial thermal load to the member. Both cases +dT and -dT should be observed!


        Structure:

                AssignThermalLoad(Temperature Change) : Assign axial thermal load to all members. Both cases +dT and -dT should be observed!

  
    
Output:

        Node:

                displacements : List of displacements for the node

                dof : List of dof numbers of the node assigned during equation numbering in the analysis.

                load : List of assigned loads.

                mass : List of assigned mass.

                restriction : List of assigned restrictions.

                SupportReactions : List of support reactions for the node.

        Member:

                getInternalForces() : Returns list of internal forces of the member.

                stiffness_local() : Returns array of local stiffness matrix of the member.

        Structure:

                K : Array of structural striffness matrix.

                F : Array of force vector.

                u : Array of displement vector.

                R : Array of support reactions.

                getPeriods() : Returns list of natural periods in length of number of assigned masses.</sup>
