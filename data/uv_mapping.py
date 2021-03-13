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
