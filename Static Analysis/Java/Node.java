
public class Node {
	
	int x;	
	int y;	
	float[] load = {0,0,0};
	float[] displacement = {0,0,0};
	int[] restriction = {0,0,0};
	int[] dof = {0,0,0};
	
	Node(int Input_x,int Input_y) {
	this.x = Input_x;
	this.y = Input_y;
	System.out.println("Defined Node : ("+this.x+","+this.y+")");
	}
	
	void Assign_Load(char Direction, float Magnitude){
		switch(Direction) {
		case 'x':
			this.load[0] = Magnitude;
			break;
		case 'y':
			this.load[1] = Magnitude;
			break;
		case 'z':
			this.load[2] = Magnitude;
			break;
		}
		System.out.println("Asseigned Load : Along = "+Direction+", Magnitude = "+Magnitude);
	}
	
	void Assign_Restriction(int x, int y, int z) {
		this.restriction[0] = x;
		this.restriction[1] = y;
		this.restriction[2] = z;
		System.out.printf("Assigned Restriction : (%s,%s,%s)\n",x,y,z);
	}

}
