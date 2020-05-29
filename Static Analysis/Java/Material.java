
public class Material {
	
	float E;
	
	Material(int Modulus_of_Elasticity) {
		this.E = Modulus_of_Elasticity;
		System.out.println("Defined Material : E = " + this.E);
	}
}
