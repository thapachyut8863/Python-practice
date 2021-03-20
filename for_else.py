#here we will using for and else at a same time:
nums = [12,15,18,21,26]
for num in nums:
    if(num % 12==0):
        print(num)
        break

else:
        print("not found:")