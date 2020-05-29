
public class Section {
	
	float area,inertia;
	Material material;
	
	Section(int Area,int Inertia,Material M) {
		this.area = Area;
		this.inertia = Inertia;
		this.material = M;
		System.out.println("Defined Section : Area = "+this.area+", Inertia = "+this.inertia+", Material = "+this.material);
	}

}
