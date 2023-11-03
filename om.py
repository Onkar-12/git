#import math

#r=int(input("enter your radius: "))
#print(r)
#a=math.pi*r*r
#print("Area of circle= ",a)
'''from tkinter import *
from tkinter import messagebox


a=[1,2.3,24,28,'raju',True,"jadu"]
def rocket():
	messagebox.showinfo('info','are you sure')
	
	print(a)
	root.destroy()
root=Tk()
root.geometry('320x300')
btn=Button(root,text='data',command=rocket)
btn.place(x='50',y='50')

root.mainloop()'''

'''# Python Program to Reverse Given Number

# Reading Number and Converting to Integer
number = int(input('Enter Number: '))
copy = number

# Set Reverse variable to 0
reverse = 0

# Finding Reverse
while number != 0:
    remainder = number%10
    reverse = reverse *10 + remainder
    number = number//10

# Displaying Reverse
print('Reverse of %d is %d' %(copy, reverse))'''




'''# Reading Three Sides
a = float(input('Enter length of side a: '))
b = float(input('Enter length of side b: '))
c = float(input('Enter length of side c: '))

if a==b==c:
	print('trangel is equilateral')
elif a==b or b==c or a==c:
	print('trangle is isoscalane')
elif a=='' or b=='' or c=='':
	print('trangle is not possible')
else:
	print('trangel is scalane')'''


'''h=float(input('Enter the rectangle height: '))
b=float(input('Enter the rectangle breadth: '))
half=float(0.5)
area=half*h*b
print('Area of traiangle is: ',area)'''


'''a=[2,4.2,5.6,False,'the boys','avi is sad']
print(len(a))
#a.insert(1,'jadu')
#print(a)
#a.pop()
#a.pop(2)
b=[3,4,2]
#a.extend(b)
#c=a.copy()
#b.sort()
#b.sort(reverse=True)
#print(b)
b.reverse()
print(b)'''

'''a=int(input('Enter a value to be calculated: '))
b=int(input('Enter a second value for calculation: '))
#choice=[1,2,3,4]
c=input('Enter your choice: ')
if c   =='1':
	print(a+b)
elif c=='2':
	print(a-b)
elif c=='3':
	print(a*b)
elif c=='4':
	print(a/b)
else:
	print('invalid choice')'''

'''import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
a=['science','commarce','arts','nalla']
plt.pie(y,labels=a,startangle=90)
plt.show()'''

'''a=int(input('Enter a number for table: '))
i=1
while i<10:
	print(a,'x',i,'=',a*i)
	i+=1'''


#a=['jadu','avi','omi','onkar']
#c=[word for word in a if word.startswith('o')]	
#b=[word for word in a if word.endswith('r')]
#print(b)
#print(c)

#for set purpose

'''a=set()
b={1,2.3,'jadu',1,True}
#print(type(a))
#print(type(b))
#print(b)
#b.add('learn coding')
#print(b) 
b.update(['omi','avi'])
print(b)
a.add(2)
print(a)'''

import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
a=['science','commarce','arts ','nalla']
plt.pie(y,labels=a,height=45,startangle=90)
plt.show()


'''def odd():
	a=i
	for i in range(a,b+1):
		if i % 2==0:
			print(i)
			print('no. is odd')	
a=input("Enter a number: ")
b=input('enter a num: ')
a=odd()

a=[2,'jk',4,4.5]
b=[4,5.6,'jalva']
b.pop(2)
print(b)'''











