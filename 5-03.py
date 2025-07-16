#1. Find the sum of odd digits in a given number

num = int(input("Enter a number : "))
string = str(num)
odd_sum = 0
for i in string :
    if int(i)%2 != 0 :
        odd_sum +=int(i)
print(odd_sum)

#2. Print all the Armstrong numbers in given range

start = int(input("Enter starting number from : "))
end = int(input("Enter ending number : "))
for num in range(start , end + 1):
    temp = num
    digits = len(str(temp))
    sum  = 0
    while( temp > 0):
        rem = temp%10
        sum = sum + rem**digits
        temp //=10
    if(num == sum ):
        print(num)

#or

def isarmstrong(n):
    temp = n 
    sum = 0
    while(temp > 0 ):
        rem  = temp%10
        sum = sum + rem**len(str(n))
        temp = temp // 10
    if(sum == n):
        return True
    return False

def armstrongRange(n1 , n2):
    for num in range(n1,n2+1):
        if isarmstrong(num) == True :
            print(num)
armstrongRange(1,200)

#3. Find the smallest prime digit in a given number

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("enter the number"))
prime_list=[]
while(number>0):
    rem=number%10
    if isprime(rem):
        prime_list.append(rem)
    number=number//10
if len(prime_list):
    print(min(prime_list), "is the smallest prime in a given number")
else:
    print("No prime digits are present in your number")
    

    



