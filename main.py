import time
x=[]
length = int(input("how long array"))
for abc in range(length):
  c= int(input("enter integer"))
  x.append(c)
#BUBBLE SORT
start= time.time()
for e in range(len(x)):

  for i in range(len(x)-1):
    u=x[i]
    f=x[i+1]
    if  x[i]>x[i+1]:
      x[i]=f
      x[i+1]=u
end= time.time()
print(x)
print(f"{end - start:.10f}, seconds taken in bubble sort")
h = []
length = int(input("how long array"))
for ghj in range(length):
  j = int(input("enter integer"))
  h.append(j)
# INSERTION SORT
newstart = time.time()
for o in range(1, len(h)):
  x = h[o]
  l = o - 1
  while l >= 0 and h[l] > x:
    h[l + 1] = h[l]
    l = l - 1
  h[l + 1] = x
newend = time.time()

print(f"{newend - newstart:.10f}, seconds taken in insertion sort")
print(h)

