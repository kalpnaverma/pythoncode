def cal_sum(number):
    return sum( int(digit) **2 for digit in str(number))
# lets n=2**2=4
# set(4)

def happy(n):
    seen=set()
    while n!=1 and  n not in seen:
        seen.add(n)
        n=cal_sum(n)
       
    if (n==1):
        return True

n=int(input("enter a number"))
if happy(n) :
    print(f"{n} is happy number")
else:
    print(f"{n} is not happy number")    
     
