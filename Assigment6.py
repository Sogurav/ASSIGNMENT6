roll=int(input("Enter roll no:"))
name=input("Enter name :")
ds={
   "roll no":roll,
   "name":name
 }
# Lists
l= []
 
# Adding Element into list
l.append(ds)
print(l)
 
# Set
s = set()
 
# Adding element into set
s.add(l)
print(s)
 
# Tuple
t = tuple(l)
  
# Dictionary
d= {}
 
# Adding the key value pair

d[s]
print("Dictionary", d)
 
d["key"]="val"
print(d)

d.update({"key1":"val"})
print(d)

#adding elements
d["key3"]="val"
print(d)

d.update({"key3":"val","key4":"val"})
print(d)
del d
print(d)