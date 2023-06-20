roll=int(input("Enter roll no:"))
name=input("Enter name :")
d={
   "roll no":roll,
   "name":name
 }
# Lists
l = []
 
# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)
 
# Set
s = set()
 
# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)
 
# Tuple
t = tuple(l)
  
# Dictionary
d= {}
 
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
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