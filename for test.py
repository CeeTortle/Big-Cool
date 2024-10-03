x=int(input("length of field>"))
y=int(input("width of field>"))
cost=int(input("cost per sq ft>"))
area=x*y
pmtr=(2*x)+(2*y)
cost=area*cost
print("area is",area)
print("perimiter is",pmtr)
print("cost is",cost)