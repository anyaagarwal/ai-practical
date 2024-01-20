a=str(input("enter 1st name "))
b=str(input("enter 2nd name "))
c=str(input("enter 3rd name "))

l1=[a,b,c]
print(l1)

l1.remove(a)
l1.remove(b)
l1.remove(c)
l1.extend(["a","b","c"])
print(l1)
del l1
