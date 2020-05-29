
public class Structure {
	
	Node[] Nodes = {};
	Member[] Members = {};
	int NumberOfNodes,NumberOfMembers,NumberOfActiveNodes;
	float[][] K;
	float[] F;
	float[] u;
	
	
	Structure(Node[] Nodes,Member[] Members){
		this.Nodes = Nodes;
		this.Members = Members;
		this.NumberOfNodes = Nodes.length;
		this.NumberOfMembers = Members.length;
		this.Equation_Numbering();
		this.K = this.getStiffnessMatrix();
		this.F = this.getForceVector();
	}
	
	private void Equation_Numbering() {
		int i3 = 0;
		for(Node N : this.Nodes) {
			for(int i2 = 0 ; i2 < 3 ; i2++) {
				if(N.restriction[i2] == 1) {N.dof[i2] = 0; }
				else if(N.restriction[i2] == 0) {i3++ ; N.dof[i2] = i3;}}}
		
		this.NumberOfActiveNodes = i3;
		for(Node N : this.Nodes) {
			for(int i2 = 0 ; i2 < 3 ; i2++) {
				if(N.restriction[i2] == 1) {i3++ ; N.dof[i2] = i3;}
			}
			System.out.println("dof numbers of the Node : ("+N.dof[0]+","+N.dof[1]+","+N.dof[2]+")");
		}
		for (Member M : this.Members) {
		for(int i = 0 ; i < 3 ; i++) M.dof[i] = M.i.dof[i];
		for(int i = 0 ; i < 3 ; i++) M.dof[i+3] = M.j.dof[i];}
	}
	private float[][] getStiffnessMatrix() {
		float[][] K = new float[this.NumberOfNodes*3][this.NumberOfNodes*3];
		for(Member M : this.Members) {
			int j2 = 0;
			for(int i2 : M.dof) {
				int j3 = 0;
				for(int i3 : M.dof) {
					K[i2-1][i3-1] += M.kg[j2][j3];
					j3 += 1;
				}
				j2 += 1;
			}	
		}
		return K;
	}
	
	private float[] getForceVector() {
		float[] F = new float[this.NumberOfActiveNodes];
		float[] FEM_R = new float[this.K.length-this.NumberOfActiveNodes];
		for(Member M : this.Members) {
			float[] FEMg = M.getFEM_global();
			int[] dof = M.dof;
			for(int i = 0 ; i < 6 ; i++) {
				if(dof[i] <= this.NumberOfActiveNodes) F[dof[i]-1] -= FEMg[i];
				else FEM_R[dof[i]-1-this.NumberOfActiveNodes] += FEMg[i];
			}
		}
		for(Node N : this.Nodes) {
			for( int i = 0 ; i < 3 ; i++) {
				if(N.load[i] != 0 && N.dof[i] <= this.NumberOfActiveNodes) F[N.dof[i]-1]+=N.load[i];
			}
		}
		return F;
	}
	
	float[] getDisplacement() {
		float[][] Kf = new float[this.NumberOfActiveNodes][this.NumberOfActiveNodes];
		for(int i = 0 ; i < this.NumberOfActiveNodes; i++) {
			for(int j = 0 ; j < this.NumberOfActiveNodes; j++) {
				Kf[i][j] = this.K[i][j];
			}
		}
		float[][] F_Matrix = new float[this.F.length][1];
		for(int i = 0 ; i < this.F.length ; i++) F_Matrix[i][0] = this.F[i];
		float[][] Kf_inverse = Matrix.Inverse(Kf);
		float[][] u_transpose = Matrix.Multipication(Kf_inverse, F_Matrix);
		float[] u = Matrix.Transpose(u_transpose)[0];
		
		for(Node N : Nodes) {
			for (int i = 0 ; i < 3 ; i++) {
				if(N.dof[i] <= this.NumberOfActiveNodes) N.displacement[i] = u[N.dof[i]-1];
				//if(N.dof[i] > this.NumberOfActiveNodes) N.SupportReactions[i] = F_supports[N.dof[i]-1];
			}
		}
		return u;
	}
	
}
