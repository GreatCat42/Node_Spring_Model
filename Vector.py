#Tired of deaing with x/y variables, wrote this
from math import sqrt
from __main__ import d as main_d

class vector:
    def __init__(this,arg0,arg1,mode='xy'):
        if mode == 'xy':
            this.x=arg0
            this.y=arg1
        if mode == 'dr':
            this.d=arg0
            this.r=arg1
        this.update(mode)

    def update(this,mode):
        if mode == 'xy':
            this.r=sqrt(this.x**2+this.y**2)
            try:
                this.d=[this.x/this.r,this.y/this.r]
            except ZeroDivisionError:
                this.d=[1,0]
        if mode == 'dr':
            this.x=this.r*this.d[0]
            this.y=this.r*this.d[1]

    def add(this,vec):
        this.x+=vec.x
        this.y+=vec.y
        this.update('xy')

    def mult(this,num):
        this.r*=num
        this.update('dr')

    def alt(this,vec,d=main_d):
        avec=vector(vec.d,vec.r*d,'dr')
        this.add(avec)
        del avec

def sum(v0,v1):
    v=vector(0,0)
    v.add(v0)
    v.add(v1)
    return v

def diff(v0,v1):
    return sum(v0,vector(-v1.x,-v1.y))
