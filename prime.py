#here we will check the number is prime or not>
x = 7
for i in range(2,x):
    if(x%i==0):
        print("not prime")
        break

else:
    print("prime:")        