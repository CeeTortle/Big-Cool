import math
def heron(a,b,c):
    s=(a+b+c)/2
    a=s*(s-a)*(s-b)*(s-c)
    if a<=0:
      return "triangle impossible"
    else:
      return math.sqrt(a)
i1=input("cuts?(seperate with ,)>")
i1=i1.split(",")
c1=int(i1[0])
c2=int(i1[1])-int(i1[0])
c3=10-int(i1[1])
area=heron(int(c1),int(c2),int(c3))
print("the area of the triangle is",area,"ft^2")