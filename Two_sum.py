''''num=input("Enter a number: ").split()
target=int(input("Enter the target digit: "))
for i in range(len(num)):
   for j in range(i+1,len(num)):
         if int(num[i])+int(num[j])==target:
              print(f"Pair found: ({num[i]}, {num[j]})")
              exit()
         else:
              print("No pair found")'''

'''x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] for i in range(x + 1)
                      for j in range(y + 1)
                      for k in range(z + 1)
                      if i + j + k != n]
print(result)'''
'''n = int(input())
arr = map(int, input().split())
x=sorted(arr)
y=max(x)
second=x[0]
print(x)
'''


'''

for _ in range(int(input('m5'))):
        name = input()
        score = float(input())'''
list1=[]
list2=[]
for _ in range(int(input())):
 name = input()
 score = float(input())
 x=[name,score]
 list2.append(score)
 list1.append(x)
x=sorted(list2)

a=[]
for i in range(len(list2)):
     if list1[i][1]==x[i]:
          a.append(list1[i][0])
          b=sorted(a)
for j in range(len(a)):
     print(b[j])

