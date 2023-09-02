a1,b1,c1 = 3,-1,7
a2,b2,c2 = 2,1,8

y = (a1*c2 - a2*c1)/(a1*b2 - a2*b1)
x = (c1-b1*y)/a1
print(y,x)