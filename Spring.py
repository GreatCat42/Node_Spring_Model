
from Tk2050 import stroke, fill, line
from Vector import *

class spring:
    def __init__(this,k,x0,N0,N1):
        this.k=k
        this.x0=x0
        this.N0=N0
        this.N1=N1

    def get_force(this):
        p0=this.N0.position
        p1=this.N1.position
        dx=diff(p1,p0)
        r=dx.r-this.x0
        d=dx.d
        return vector(d,r,'dr')

    def set_force(this):
        F0=this.get_force()
        this.N0.forces.append(F0)
        F1=diff(vector(0,0),F0)
        this.N1.forces.append(F1)

    def show(this):
        p0=this.N0.position
        p1=this.N1.position
        stroke('')
        fill('#008800')
        line(p0.x*100,p0.y*100,p1.x*100,p1.y*100)

#Complete
