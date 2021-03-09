# functions that remap 2D coordinate to a 3D space

def rotate(tpms_grid, angle):
    p=tpms_grid.idx_grid
    c_a, s_a = cos(a), sin(a)
    tpms_grid.idx_grid = (
        p[0] * c_a - p[1] * s_a,
        p[0] * s_a + p[1] * c_a
    )

vec3 rotate(vec3 p) {
    return rotate(p, alpha);
}

vec3 uvMapping(vec2 uv){
    float alfa = uv.x*pScales.x;
    float r = cylinderRadiusBase+cos(pi+alfa*cylinderMultiplierM)*cos(pi+alfa*cylinderMultiplierN);
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