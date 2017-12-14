# array allocation test code 

i=0; a=[]
while i < 5:
  print(i)
  a=a+[(i+1)*111]
  print(a)
  i=i+1

del a[2]
print(a)
print(a[2])

del a
a=[[],[]]
print(a)
j=0
while j < 2:
  i=0
  print("{0:1d}".format(j),end="")
  while i < 5:
    a[j]=a[j]+[i*111]
    print(" {0:4d}".format(a[j][i]),end="")
    i=i+1
  print("")
  j=j+1
print(a)

print("---"); del a;
a=[]
print(a)
for i in range(2):
  a=a+[[]]
  print(a)
  for j in range(3):
      a[i]=a[i]+[100+10*i+j]
      print(a)
print(a)

print("---"); del a;
a=[]
print(a)
for i in range(2):
  a=a+[[]]
  print(a)
  for j in range(2):
      a[i]=a[i]+[[]]
      print(a)
      for k in range(2):
          a[i][j]=a[i][j]+[1000+100*i+10*j+k]
          print(a)
print(a)
