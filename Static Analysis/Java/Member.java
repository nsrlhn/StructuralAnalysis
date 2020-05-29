
public class Member {
	
	Node i,j;
	Section section;
	float[] FEM  = {0,0,0,0,0,0};
	float[] InternalForces = {0,0,0,0,0,0};
	int[] dof = {0,0,0,0,0,0};
	float length;
	float[][] k;
	float[][] kg;
	float[][] R;
	float[][] R_Transpose;
	
	Member(Node Start_Node, Node End_Node, Section S){
		this.i = Start_Node;
		this.j = End_Node;
		this.section = S;
		this.length = this.getLength();
		this.k = this.getLocalStiffness();
		this.R = this.getR();
		this.R_Transpose = Matrix.Transpose(this.R);
		this.kg = this.getGlobalStiffness();
		System.out.println("Defined Member : "+this.i.x+","+this.i.y+" to "+this.j.x+","+this.j.y+"; Section = "+this.section);
	}
	
	void Assign_FEM(float dof1,float dof2,float dof3,float dof4,float dof5,float dof6) {
		this.FEM [0]= dof1;
		this.FEM [1]= dof2;
		this.FEM [2]= dof3;
		this.FEM [3]= dof4;
		this.FEM [4]= dof5;
		this.FEM [5]= dof6;
		System.out.println("Assigned FEM : ("+dof1+","+dof2+","+dof3+","+dof4+","+dof5+","+dof6+")");
	}
	
	float[] getFEM_global() {
		float[][] FEMg;
		float[][] FEM = new float[1][6];
		FEM[0] = this.FEM;
		FEMg = Matrix.Multipication(this.R (transpose olmali), Matrix.Transpose(FEM));
		return Matrix.Transpose(FEMg)[0];
	}
	
	private float getLength() {
		int dx,dy;
		dx = this.j.x-this.i.x;
		dy = this.j.y-this.i.y;
		return (float)Math.pow((dx*dx+dy*dy), 0.5);
	}
	
	private float[][] getLocalStiffness(){
		float E = this.section.material.E;
		float A = this.section.area;
		float I = this.section.inertia;
		float L = this.length;
		float[][] k = {{E*A/L,0,0,-E*A/L,0,0},
                			{0,12*E*I/L/L/L,6*E*I/L/L,0,-12*E*I/L/L/L,6*E*I/L/L},
                			{0,6*E*I/L/L,4*E*I/L,0,-6*E*I/L/L,2*E*I/L},
                			{-E*A/L,0,0,E*A/L,0,0},
                			{0,-12*E*I/L/L/L,-6*E*I/L/L,0,12*E*I/L/L/L,-6*E*I/L/L},
                			{0,6*E*I/L/L,2*E*I/L,0,-6*E*I/L/L,4*E*I/L}};
        return k;
	}
	
	private float[][] getR(){
		float cos = (this.j.x-this.i.x)/this.length;
		float sin = (this.j.y-this.i.y)/this.length;
		float[][] matrix = {{cos,sin,0,0,0,0},
                		   {-sin,cos,0,0,0,0},
                		   {0,0,1,0,0,0},
                		   {0,0,0,cos,sin,0},
                		   {0,0,0,-sin,cos,0},
                		   {0,0,0,0,0,1}};
		return matrix;
	}

	private float[][] getGlobalStiffness(){
		float temp[][] = Matrix.Multipication(this.R_Transpose, this.k);
		return Matrix.Multipication(temp, this.R);
	}
	
	float[] getInternalForces() {
		float[] u_global = new float[6];
		for (int i = 0 ; i < 3 ; i++) {
			u_global[i] = this.i.displacement[i];
			u_global[i+3] = this.j.displacement[i];
			}
		float[] u_local = Matrix.Multipication(this.R, u_global);
		float[] F = Matrix.Multipication(this.k, u_local);
		for(int i = 0 ; i < 6 ; i++) this.InternalForces[i] = F[i]+this.FEM[i];
		return this.InternalForces;
	}
}
