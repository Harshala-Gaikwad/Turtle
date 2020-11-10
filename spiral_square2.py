#spiral square Inside in 
import turtle

skk = turtle.Turtle()
skk.color("blue")
def sqr(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size+5
sqr(6)
sqr(26)
sqr(46)
sqr(66)
sqr(86)
sqr(106)    
sqr(126)
sqr(146)
turtle.done()
