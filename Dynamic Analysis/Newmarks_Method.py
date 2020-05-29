"""
    Time-History Analysis by Newmark's Method:
        
        m(a) + c(v) + k(u) = P
        
    P should be a list representing instantaneous value of external force 
    starting from t = 0 with time increasement dt.
                                    """
def Newmark(m,k,c,u0,v0,P,dt):
    u=[0]*len(P)
    u[0]=u0
    v=[0]*len(P)
    v[0]=v0
    a=[0]*len(P)
    a[0]=(P[0]-c*v[0]-k*u[0])/m #m/s2
    
    kstar=k+2*c/dt+4*m/dt**2 #kg/s2
    dF = [0]*len(P)
    dFstar = [0]*len(P)
    for i in range(len(P)-1):
        dF[i]=P[i+1]-P[i] #N
        dFstar[i]=dF[i]+(4*m/dt+2*c)*v[i]+2*m*a[i] #N
        du=dFstar[i]/kstar
        u[i+1]=u[i]+du
        
        dv=2*du/dt-2*v[i]
        v[i+1]=v[i]+dv
        da=4*du/dt**2-4/dt*v[i]-2*a[i]
        a[i+1]=a[i]+da
    return u