# slicing
n= "i am java trainer" 
print(n)
print("n[2:4]",n[2:4])
print("n[5:9]",n[5:9])
print("n[:15]",n[:15])
print("n[2:]",n[2:])
print("n[:]",n[:])
print("n[0:17:3]",n[0:17:3])
print("n[ : : ]",n[ : : ]) 
print("n[: :-1]",n[: :-1])


# is operator 
x=["word","words"]
y=["word","words"]
z=x
print(x is y)
print(x is z)

# capitalize
str= "rahul tiwari"
print(str)
str=str.capitalize()
print(str)
print(id(str))

# center 
str = "rahul"
str=str.center(15,"*")
print(str)

# count string 
str = "second a start index and third "
oc = str.count("a")
print(oc)

str = "second a start index and third "
oc = str.count("a",8,15)
print(oc)
# endswith ()
str = "second a start index and third "
isends = str.endswith(".")
print(isends)

str = "second a start index and third "
isends = str.endswith(".",0,6)
print(isends)

str = "second a start index and third "
isends = str.startswith(".",0,6)
print(isends)

# find method give -1 if not find
str = " welcome to my class"
str2=str.find("t")
print(str2)


str = " welcome to my class"
str2=str.find("t",10,13)
print(str2)

# index method give error if not find
# str = " welcome to my class"
# str2=str.index("t",10,13)
# print(str2)


# isalnum

str = "welcometomyclass"
str2=str.isalnum()
print(str2)

str = "welcome to myclass"
str2=str.isalnum()
print(str2)

# isalpha

str = "welcome to myclass"
str2=str.isalpha()
print(str2)

#isnumric

str = "welcome to myclass"
str2=str.isnumeric()
print(str2)

#islower
str = "welcome to myclass"
str2=str.islower()
print(str2)

# isupper
str = "welcome to myclass"
str2=str.isupper()
print(str2)


# lower
str = "welcOME to myclass"
str2=str.lower()
print(str2)

#upper
str = "welcOME to myclass"
str2=str.upper()
print(str2)

#lstrip
str = "               welcOME to myclass"
str2=str.lstrip()
print(str2)

str = "---------------welcOME to myclass-------------------"
str2=str.lstrip("-")
print(str2)

str = "---------------welcOME to myclass-------------------"
str2=str.rstrip("-")
print(str2)


str = "---------------welcOME to myclass-------------------"
str2=str.strip("-")
print(str2)


# replace
str = "---------------welcOME to myclass-------------------"
str2=str.replace("-","")
print(str2)


str = "java---java------welcOME to myclass----java-------------"
str2=str.replace("java","",2)
print(str2)
#old
#new
#count

#swapcase()
str = "java---welcOME to myclass---JAVA-------------"
str2=str.swapcase()
print(str2)

#title
str = "java---welcOME to myclass---JAVA-------------"
str2=str.title()
print(str2)