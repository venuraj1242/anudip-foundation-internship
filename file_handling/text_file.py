# file handling

# write mode- overwrites an existing file or opens a new file if not found.
f=open("anudip.txt","w")
f.write("This is python class\n")
f.close()

# append mode- opens an existing file and appends new data at the end of it.
f=open("anudip.txt","a")
f.write("This is python class.\nTopic is file handling")
f.close()

# read mode- reads the specified number of characters
f=open("anudip.txt","r")
data=f.read(7)
print(data)
f.close()
print('--------------------------------------------------------------')

# tell()- it tells the position of file pointer
f=open("anudip.txt","r")
print("position of pointer=",f.tell())
data=f.read(7)
print(data)
print("position of pointer=",f.tell())
f.close()
print('---------------------------------------------------------------')

# seek()- it is used to change the position of the file pointer
f=open("anudip.txt","r")
print("position of pointer=",f.tell())
f.seek(12)
data=f.read(7)
print(data)
print("position of pointer=",f.tell())
f.close()
print('-----------------------------------------------------------------')