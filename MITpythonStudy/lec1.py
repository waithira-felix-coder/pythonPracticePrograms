float(123)
print(float(123))
type(float(123))
print(type(float(123)))
print(type(round(7.3)))
print(round(7.3)) 
print(int(7.2))
print(type(int(7.2)))
print(type(round(7.2)))

## EXPRESSIONS ###
print("----------")
print((13 - 4)/(12 * 12))
print(type(4 * 3))
print(type(4.00 * 3))
print(int(1 / 2))

print(2**3) #power
print(2*2) #multiplication
print(2/2) #division
print(5 //3) #floor division
print(5 % 3) #modulo

xy = 10
print(xy)
print(xy *3)
xy = 5
print(xy)


### AREA OF A CIRCLE ###
pi= 3.14
radius = float(input("Radius of the circle: "))
area = pi * (radius ** 2)
print("Area of the circle is: ", area)
radius = radius + 1
area = pi * (radius ** 2)
print("Area of the circle with increased radius is: ", area)

radius = 2.2
area = pi * (radius ** 2)
print("Area of the circle is: ", area)

## Exercise ##
meter = 100
feet = meter * 100
meter = 200
print(meter)
print(feet)