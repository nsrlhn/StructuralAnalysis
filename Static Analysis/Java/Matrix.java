
public class Matrix {
	
	static int[][] Multipication(int[][] Matrix1,int[][] Matrix2){
		int n = Matrix1.length;
		int m = Matrix1[0].length;
		int p = Matrix2.length;
		int q = Matrix2[0].length;
		int[][] Result = new int[n][q];
		if (p != m) { System.out.println("Matrices are Not Multipliable"); return Result;}
		else {
			for (int i1 = 0 ; i1 < n ; i1++) {
				for (int i2 = 0 ; i2 < q ; i2++) {
					for (int i3 = 0 ; i3 < m ; i3++) {
						Result[i1][i2] += Matrix1[i1][i3]*Matrix2[i3][i2];
					}
				}
			}
		}
		return Result;
	}
	
	static float[][] Multipication(float[][] Matrix1,float[][] Matrix2){
		int n = Matrix1.length;
		int m = Matrix1[0].length;
		int p = Matrix2.length;
		int q = Matrix2[0].length;
		float[][] Result = new float[n][q];
		if (p != m) { System.out.println("Matrices are Not Multipliable!!!"); return Result;}
		else {
			for (int i1 = 0 ; i1 < n ; i1++) {
				for (int i2 = 0 ; i2 < q ; i2++) {
					for (int i3 = 0 ; i3 < m ; i3++) {
						Result[i1][i2] += Matrix1[i1][i3]*Matrix2[i3][i2];
					}
				}
			}
		}
		return Result;
	}
	
	static float[] Multipication(float[][] Matrix1,float[] Vector1){
		int n = Matrix1.length;
		int m = Matrix1[0].length;
		int p = Vector1.length;
		int q = 1;
		float[][] Matrix2 = new float[p][q];
		for(int i = 0 ; i < p ; i++) Matrix2[i][0] = Vector1[i];
		float[] Result = new float[n];
		float[][] Result_Matrix = new float[m][1];
		if (p != n) { System.out.println("Matrices are Not Multipliable!!!"); return Result;}
		else {
			for (int i1 = 0 ; i1 < n ; i1++) {
				for (int i2 = 0 ; i2 < q ; i2++) {
					for (int i3 = 0 ; i3 < m ; i3++) {
						Result_Matrix[i1][i2] += Matrix1[i1][i3]*Matrix2[i3][i2];
					}
				}
			}
		}
		for(int i = 0 ; i < m ; i++) Result[i] = Result_Matrix[i][0];
		return Result;
	}
	
    static float[][] Transpose(float A[][]){ 
        int i, j;
        int n = A.length;
        int m = A[0].length;
        float B[][] = new float[m][n];
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) B[j][i] = A[i][j];
        }
        return B;
    } 
	
	static float[][] Identity(int Size){
		float[][] result = new float[Size][Size]; 
		for (int i = 0 ; i < Size ; i++) {
			for (int j = 0 ; j < Size ; j++) {
				if (i ==j) result[i][j] = 1 ;
				else result[i][j] = 0 ; 
			}
		}
		return result;
	}
	
	static float[][] Inverse(float[][] theMatrix){
		float[][] A = theMatrix;
		int n = A.length;
		int m = A[0].length;
		if (n == m) {
			float d,k;
			float[][] B = Matrix.Identity(n);
			for (int i = 0 ; i < n ; i++) {
				d = A[i][i];
				for (int j = 0 ; j < n ; j++) {
					A[i][j] /= d;
					B[i][j] /= d;
				}
				for (int x = 0 ; x < n ; x++) {
					if(x != i) {
						k = A[x][i];
						for (int j = 0 ; j < n ; j++) {
							A[x][j] -= A[i][j]*k;
							B[x][j] -= B[i][j]*k;
						}
					}
				}
			}
			return B;
		}
		else {
			System.out.println("Matrix should be square");
			float[][] B = new float[n][n];
			return B;
		}
	}
}
