from Tk2050 import *

d=0.1
from Node import node
from Spring import spring
from Vector import vector

n0=node(vector(1,0),1,0)
n1=node(vector(0,0.5),1,0)
n2=node(vector(1,1),1,0)
n3=node(vector(2,0.5),1,0)

n=[n0,n1,n2,n3]

s0=spring(20,1,n0,n1)
s1=spring(20,1,n1,n2)
s2=spring(20,1,n2,n3)
s3=spring(20,1,n3,n0)
s4=spring(20,1,n0,n2)

s=[s0,s1,s2,s3,s4]

def draw():
    fill('#000000')
    stroke('')
    rect(0,0,400,400)
    for Node in n:
        Node.show()
        Node.move()
    for Spring in s:
        Spring.show()
        Spring.set_force()

from Tk2050 import loop

loop()
