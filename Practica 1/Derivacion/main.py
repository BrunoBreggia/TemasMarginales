from autodiff_forward import *

a1 = Variable(5,1)
a2 = Variable(10)
b = a1*a2
c = log(a1)
d = sin(a2)
e = b*c
f = e+d
print(f.val)
print(f.grad)

