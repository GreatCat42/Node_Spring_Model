#Finally a better version...

from Vector import *
from __main__ import stroke, fill, ellipse

class node:
    def __init__(this,position,mass,max_fric):
        this.position=position
        this.mass=mass
        this.max_fric=max_fric

        this.forces=[]
        this.velocity=vector(0,0)

    def show(this):
        x=this.position.x
        y=this.position.y
        stroke('')
        fill('#00cc00')
        ellipse(x*100,y*100,5,5)

    def move(this):
        this.get_fric()
        sum_forces=vector(0,0)

        for force in this.forces:
            sum_forces.add(force)

        this.forces=[]

        sum_forces.mult(1/this.mass)
        this.velocity.alt(sum_forces)
        this.position.alt(this.velocity)

    def get_fric(this):
        f=vector(this.velocity.d,this.max_fric*-1,'dr')
        this.forces.append(f)
