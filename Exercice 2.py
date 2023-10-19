n = int(input("Enter an integer:"))
Divider = 0
print("The divisors of",n,"are:")
for i in range(1,n+1) :
    if n % i == 0 :
        print(i)
        Divider = Divider+1
print("the number of divisors of",n,"is",Divider,".")

    
    



