# project Idea

''''
Input : number

Constraints: No built IN FUNCTION

Output : 
..even/odd
..prime
..digit count

Concepts : input() if/else loops modulus

#we start from Simple Concepts WIthout Using Advanced Modules,buil in functionality,libraries
# we also do this by  functions but we bound to use only concepts listed above
'''

# ================1 condition==================================

number=int(input("Enter Number: "))
print("Condition 1:\n")
if  number==0:
    print('Number must be  greater than 0 ')
elif number%2==0:
    print(f'The {number} is exactly Divisible by 2 so it is even\n')
else:
    print(f'The {number} is Not  exactly Divisible by 2 so it is  not even\n')
 
# ================2 condition==================================
if number>1:
    for i in range(2,int(number**0.5+1)): # as loops stop n-1
        if number%i==0:
            print("Condition 2:\nNot Prime Number\n")
            print(f'PROOF:\n{i} times {number//i} is {number}')
            break
    else:
        print(f' condition 2:\n{number} is a prime number\n')
else:
   print(f' Condition 2:\n{number} is not a prime number.\n')   
   # ================3 condition==================================
count=0
temp=number
if temp==0:
    count=1
else:
    while temp!=0:
        temp//=10
        count+=1
print('Condition 3')  
print(f' The Total digits in number are: {count}')