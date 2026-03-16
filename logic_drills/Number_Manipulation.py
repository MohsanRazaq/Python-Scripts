'''
*Challenge*:
Take a number as input and print its digits in reverse order without converting it to a string.

Example: Input 1234 → Output 4321.

'''
import sys
if len(sys.argv)>1:
    number=int(sys.argv[1])
else:
    number=int(input("Enter Number: "))
rev=0
while number!=0:
    digit=number%10
    rev=rev*10+digit
    number//=10
print(f'Reverse Numnber is: {rev}')
    