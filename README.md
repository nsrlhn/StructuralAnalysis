<p># Two dimansional structural frame analysis</p>
<p><br></p>
<p><br></p>
<p>Inputs:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Node:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Node(Coordinate) : Define a node</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignLoad(Direction, Magnitude) : Assign load to the node, direction should be &#39;x&#39;, &#39;y&#39; or &#39;z&#39;. &#39;z&#39; means it is moment.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignSupport(Name or Restriction) : Can be input &#39;fixed&#39;, &#39;pin&#39; or restriction list like [1,1,0] for pin.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignSupportSettlement(Direction, Magnitude) : Assign support settlement ot the node, direction should be &#39;x&#39;, &#39;y&#39; or &#39;z&#39;. &#39;z&#39; means it is rotation.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignMass(Mass) : Mass should be list according to global coordinate system as [x,y,z_rotation]</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Material:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Material(Modulus of Elasticity, Thermal Expansion Coefficient) : Define a material</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Section:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Section(Area, Moment of Inertia, Material) : Define a section</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Member:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Member(Start Node, End Node, Section) : Define a member.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignFEM([d1,d2,d3,d4,d5,d6]) : Assign FEM with respect to member&#39;s local coordinate system.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignUniformLoad(Uniformly Distributed Load) : Assign uniformly distributed load perpendicular to the member.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignPointLoad(Load, Distance from Start Node) : Assign point load perpendicular to the member.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignMoment(Load, Distance from Start Node) : Assign moment load.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; AssignThermalLoad(Temperature Change) : Assign axial thermal load to the member. Both cases +dT and -dT should be observed!</p>
<p><span style="white-space:pre;">&nbsp; &nbsp;&nbsp;</span>Structure:</p>
<p><span style="white-space:pre;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>AssignThermalLoad(Temperature Change) : Assign axial thermal load to all members. Both cases +dT and -dT should be observed!</p>
<p>Output:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Node:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displacements : List of displacements for the node</p>
<p><span style="white-space:pre;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>dof : List of dof numbers of the node assigned during equation numbering in the analysis.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; load : List of assigned loads.</p>
<p><span style="white-space:pre;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>mass : List of assigned mass.</p>
<p><span style="white-space:pre;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>restriction : List of assigned restrictions.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SupportReactions : List of support reactions for the node.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Member:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; getInternalForces() : Returns list of internal forces of the member.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; stiffness_local() : Returns array of local stiffness matrix of the member.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; Structure:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; K : Array of structural striffness matrix.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; F : Array of force vector.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; u : Array of displement vector.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; R : Array of support reactions.</p>
<p><span style="white-space:pre;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>getPeriods() : Returns list of natural periods in length of number of assigned masses.</p>
<p><br></p>
