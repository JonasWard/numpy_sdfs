from numpy import sin, cos, pi

class UVSphereMapping():
    def __init__(self, r=1., m = 1., n = 1.):
        self.r=r
        self.m=m
        self.n=n

    def map(self, xs, ys, zs):
        theta,omega=xs/self.m,ys/self.n
        zs=sin(omega)*self.r
        rs=cos(omega)*self.r
        xs,ys=sin(theta)*rs,cos(theta)*rs

        return xs, ys, zs

class UVCylinderMapping():
    def __init__(self, r=1., m = 1., n = 1., direction='x'):
        self.r=r
        self.m=m
        self.n=n
        
        self.dir=direction

    def map(self, xs, ys, zs):
        if self.dir=='x':
            xs, ys, zs = self.map_function(xs, ys, zs)
        elif self.dir=='y':
            ys, xs, zs = self.map_function(ys, xs, zs)
        elif self.dir=='z':
            zs, xs, yz = self.map_function(zs, xs, yz)

        return xs, ys, zs
        
    def map_function(self, xs, ys, zs)

def uv_cylinder_mapping(tpms_grid, c_r=1., c_m=0, c_n=0):
    r = c_r+cos(pi+alfa*c_m)*cos(pi+alfa*c_n);
    r = r * pScales.z;
    vec3 v3 = vec3(cos(alfa)*r, sin(alfa)*r, uv.y*pScales.y);
    return v3;
}

vec3 translateForUV(vec3 p){
    p = translate( p, mvVecUV);
    return uvMapping(p.xy);
}

vec3 translateForDistance(vec3 p) {
    return translate( rotate( p ), mvVecP);
}

vec3 positionManagement(vec3 p){
    vec3 uv = translateForUV(p);
    return translateForDistance(uv);
}

