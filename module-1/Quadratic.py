import math

a = float(input("A = ")) #get user input for a
b = float(input("B = ")) #get user input for b
c = float(input("C = ")) #get user input for c

sol1 = (-b + math.sqrt(b**2 -4*a*c)) / (2*a) #calculate first solution
sol2 = (-b - math.sqrt(b**2 -4*a*c)) / (2*a) #calculate second solution

print(f"The solutions are {sol1} and {sol2}") #print the solutions