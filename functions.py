#Memrize
def myFunction (name):
    print (name +"Hadeel")

myFunction("Aldhafeeri ")
myFunction("Al ")

print ("***"*25)

# Function with two arguments
def addNumner (num1, num2):
    sum= num1+ num2
    print ("Sum",sum)

addNumner(4,5)

print ("***"*25)
# Function return Type
def squerFinder(num):
    squer= num**2
    return squer

result=squerFinder(5)#call
print (result)

print ("***"*25)

# Add Two Numbers

def addNumbers (number1, number2):
    numberAdder= number1+number2
    return numberAdder

resultAdd= addNumbers (4,5)
print (resultAdd)


print ("***"*25)
#Python Library Function
import math

squerRoot= math.sqrt(4)
print (squerRoot)


power= math.pow(2,3)
print (power)


print ("***"*25)

def findsqureUsingFor (numberA):
    whatSquer= numberA*numberA
    return whatSquer

for h in [1,2,3]:
    weFound= findsqureUsingFor(h)
    print (weFound)









