from numpy import sin, cos

class UVSphereMapping():
    def __init__(self, r=1., x_period = 1., y_period = 1.):
        self.r=r
        self.x_p=x_period
        self.y_p=y_period

    def map(self, xs, ys, zs):
        theta,omega=xs/self.x_p,ys/self.y_p
        zs=sin(omega)*self.r
        rs=cos(omega)*self.r
        xs,ys=sin(theta)*rs,cos(theta)*rs

        return xs, ys, zs

class UVCylinderMapping():
    pass

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

