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
            zs, xs, ys = self.map_function(zs, xs, ys)

        return xs, ys, zs
        
    def map_function(self, xs, ys, zs):
        xs/=self.m
        phase=ys/self.n
        ys=cos(phase)*self.r
        zs=sin(phase)*self.r

        return xs, ys, zs

class UVSpiderMapping(UVCylinderMapping):
    def __init__(self, r_base=1., m_cyl = 1., n_cyl = 1., direction='x', m_remap = 0, n_remap = 0):
        self.r_base=r_base
        self.m_cyl=m_cyl
        self.n_cyl=n_cyl

        self.m_re=m_remap
        self.n_re=n_remap

        self.dir=direction

    def map_function(self, xs, ys, zs):
        xs/=self.m_cyl
        phase=ys/self.n_cyl
        r=self.r_base+cos(pi+self.m_re*phase)+cos(pi+self.n_re*phase)
        ys=cos(phase)*r
        zs=sin(phase)*r

        return xs, ys, zs

if __name__ == "__main__":
    from coordinate_grid import CoordinateGrid

    cg=CoordinateGrid(1000, 1000)
    cg.uv_map(UVSpiderMapping(
        r_base = 1.5, 
        m_cyl = 100., 
        n_cyl = 100., 
        direction='x', 
        m_remap = 2, 
        n_remap = 4
    ))

    cg.visualizeXY()

    cg.uv_map(UVSpiderMapping(
        r_base = 1.5, 
        m_cyl = 10., 
        n_cyl = 10., 
        direction='z', 
        m_remap = 0, 
        n_remap = 3
    ))

    cg.visualizeXY()

    cg=CoordinateGrid(1000,1000)
    cg.rotate_angles(angles=(1., -1.3, .6))

    cg.visualizeXY()

    cg.uv_map(UVSpiderMapping(
        r_base = 1.5, 
        m_cyl = 100., 
        n_cyl = 100., 
        direction='x', 
        m_remap = 0, 
        n_remap = 3
    ))

    cg.visualizeXY()