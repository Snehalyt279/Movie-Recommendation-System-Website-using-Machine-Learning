'''story="\'\\Mari had a little lamb, her \ fur was as white as snow\'\\"
print(story)
print(len(story))
print(story.endswith("fur"))
print(story.count("Mari"))
print(story.capitalize())
print(story.find("lamb"))
print(story.replace("lamb","pony"))

name=input("Enter your name : \n")
print("Good Morning ! "+name)

letter=' Dear <|NAME|>,
You are Selected ! Let's Partyyy
Date: <|DATE|>'
name = input("Enter your Name :\n")
date = input("Enter today's date :\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)

str="Program to find double  spaces"
ds=str.replace("  "," ")
print(ds)

letter="Dear Snehal, \n \t This Python course is cool, Thanks.\n K Bye !"
print(letter)

a=[1,2,4,56,6]
a[3]=5
print(a)

b=[6,"Snehal",6.5]
print(b[-1:])

l1=[1,8,7,2,21,15]
print(l1)
l1.remove(2)
print(l1)

t=(1,2,4,5,4,1,2,1,1)
print(t.count(1))
print(t.index(5))

f1=input("Enter marks for student number 1 : ")
f2=input("Enter marks for student number 2 : ")
f3=input("Enter marks for student number 3 : ")
f4=input("Enter marks for student number 4 : ")
marks=[f1,f2,f3,f4]
print(marks)
marks.sort()
print(marks)

a=(1,2,3,4,5)
print(a[0])

a=[65,23,12,74,42]
print(a[0]+a[1]+a[2]+a[3]+a[4])
print(sum(a))

a=(7,0,8,0,0,9)
print(a.count(0))

myDict = {
    "Fast": "In a quick manner",
    "Snehal": "Aspirant",
    "Marks": [1,2,5],
    "anothaDict": {"Snehal":"Jumpman"},
    1:2
    }
#print(myDict["Fast"])
#print(myDict["Snehal"])
#myDict["Marks"]=[45,78]
#print(myDict["Marks"])
#print(myDict['anothaDict']['Snehal'])
#print(tuple(myDict.values()))
print(myDict.items())
updateDict={"SubeSube":"mikemike",
            "Rambo":"Rainbow",
            "peepee":"poopoo"}
myDict.update(updateDict)
print(myDict)
print(myDict.get("peepee"))
print(myDict["Rambo"])
a={1,2,3,4,5,1}
print(type(a))
print(a)

b=set()
print(type(b))
b.add(4)
b.add(5)
b.add(5)
b.add((4,5,6))
print(b)
print(len(b))
b.remove(5)
print(b)
print(b.pop())
print(b)

myDict = {
    "Bheja" : "Brain",
    "Keeda" : "Insect",
    "Samosa" : "Tasty"
    }
a=input("Enter a hindi word : \n")
print("Options are : ",myDict.keys())
print("The meaning of the word is : ",myDict[a])

num1 = int(input("Enter Number 1 : \n"))
num2 = int(input("Enter Number 2 : \n"))
num3 = int(input("Enter Number 3 : \n"))
num4 = int(input("Enter Number 4 : \n"))
num5 = int(input("Enter Number 5 : \n"))
num6 = int(input("Enter Number 6 : \n"))
num7 = int(input("Enter Number 7 : \n"))
num8 = int(input("Enter Number 8 : \n"))

s={num1,num2,num3,num4,num5,num6,num7,num8}
print(s)

s = {32,32.0,'32',45,32}
print(len(s))'''

s=[]
print(type(s))
