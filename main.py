print('hello')

#var declaration
num1=10
num2=20
sum=num1+num2
print(sum)

#printing
print('om' 'patel')
print('om'*5)
name='om'
#comment
print('name :',name)

#input from user
# print('what is your name?')
# myName=input()
# print('your name :',myName)

#some imp functions
print(int(7.7))
print(type(str(29)))
print(len(str(29)))

#conditions
print('dog'!='Dog')
print(True is True or True is False)

#conditional statements
if name=='om':
    print('Hola!!')
elif name=='patel':
    print('Holaa!!')
else:
    print('bye')

#loops
spam=0
while spam<5:
    if spam==3:
        break
    print('while: hello',spam)
    spam+=1
else:
    print('this will be printed only if the loop if breaked')

for i in range(5):
    print('for loop : {}'.format(str(i)))

for i in range(0,10,2):
    print("forward step2:",i)

for i in range(10,-1,-1):
    print("rev:",i)

#random num
import random
for i in range(5):
    print('random number:{}'.format(str(random.randint(1,10))))

#functions
def sayHola(name):
    print("Hola",name,"how are you?")

sayHola('patel')

def getRandInt(l,h):
    return random.randint(l,h)

print('fun rand:',getRandInt(1,100))

def printData():
    global varx
    varx='demo'
    print('hello',end='')
    print('world')
    print('dog','cat','cow',sep=',')

varx='not demo'
printData()
print('varx:',varx)

def funDiv(x,y):
    try:
        print (x/y)
    except ZeroDivisionError as e:
        print('error:',e)
    finally:
        print("divfun finished")

funDiv(5,0)