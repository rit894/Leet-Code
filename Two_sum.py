num=input("Enter a number: ").split()
target=int(input("Enter the target digit: "))
for i in range(len(num)):
   for j in range(i+1,len(num)):
         if int(num[i])+int(num[j])==target:
              print(f"Pair found: ({num[i]}, {num[j]})")
              exit()
         else:
              print("No pair found")