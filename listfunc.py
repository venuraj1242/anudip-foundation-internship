
#append function
list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
x=int(input("enter the number"))
list.append(x)
print(list)

# extend function 

list1=[110,120,130]
list.extend(list1)
print(list)

# insert function 

print ( "insert 200 at 2 ")
list.insert(2,200)
print (list)

#find a method to insert all the elements of another squence datatype at particular index in the list 
#but all the elelments must be inserted one by one 

l=list[0:3]+[120,130,140]+list[3:]
print(l)

#pop function 
print ( "remove at 2 ")
list.pop(2)
print (list)

print ( "remove at last")
list.pop()
print (list)

# remove()
list.remove(90)
print(list)
