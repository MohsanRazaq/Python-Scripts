'''
Challenge: An Armstrong number (like 153) is a number where the sum of its own digits, each raised to the power of the number of digits, equals the number itself.
The Task:
Check if a number is an Armstrong number.Example: For 153, $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153. (Since 153 has 3 digits, we use the power of 3).

'''
import sys
if len(sys.argv)>1:
    number=int(sys.argv[1])
else:
    number=int(input("Enter Number: "))

pwr=len(str(number))
sum=0
temp=number
 
while temp>0:
    digit=temp%10
    sum+=digit**pwr
    temp//=10
    
if sum==number:
    print(f'{number} is Arm Strong Number')
else:
    print(f'{number} is not Arm Strong Number')
