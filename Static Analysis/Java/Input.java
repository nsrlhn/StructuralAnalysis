import java.util.Arrays;

public class Input {
	
	public static void main(String[] args) {
		Node N1 = new Node(0,0);
		Node N2 = new Node(0,4);
		Node N3 = new Node(3,4);
		Node N4 = new Node(3,0);
		
		Material Concrete = new Material(1);

		Section S1 = new Section(600,432,Concrete);
		
		Member M1 = new Member(N1,N2,S1);
		Member M2 = new Member(N2,N3,S1);
		Member M3 = new Member(N3,N4,S1);
		Member M4 = new Member(N1,N3,S1);
		
		N2.Assign_Load('x', 10);
		N1.Assign_Restriction(1,1,1);
		N4.Assign_Restriction(1,1,1);
	
		M2.Assign_FEM(0,30,15,0,30,-15);
		
		Node[] Nodes = {N1,N2,N3,N4};
		Member[] Members = {M1,M2,M3,M4};
		
		Structure Structure1 = new Structure(Nodes,Members);
		//for(float[] x : Structure1.K) System.out.println("K :"+Arrays.toString(x));
		System.out.println("Force Vector : "+Arrays.toString(Structure1.F));
		float[] u = Structure1.getDisplacement();
		System.out.println("Displacements : "+Arrays.toString(u));
		System.out.println("Internal Forces of M1 :"+Arrays.toString(M1.getInternalForces()));
		System.out.println("Internal Forces of M2 :"+Arrays.toString(M1.getInternalForces()));
		System.out.println("Internal Forces of M3 :"+Arrays.toString(M3.getInternalForces()));
		System.out.println("Internal Forces of M4 :"+Arrays.toString(M4.getInternalForces()));
	}

}
