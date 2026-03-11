''''
The "Factor Sum" (The Perfect Number)Challenge:
A "Perfect Number" is a positive integer that is equal to the sum of its proper divisors (excluding itself).
The Task:
Find the sum of all divisors of a number and check if it equals the original number.
Example:
6 is perfect because its divisors are 1, 2, 3, and $1 + 2 + 3 = 6.
Logic: Use a loop from 1 to number // 2 + 1 and use % to find divisors.
'''
import sys
if len(sys.argv)>1:
    number=int(sys.argv[1])
else:
    number=int(input('Enter Number: '))
divisor_sum=0
for i in range(1,(number//2)+1):
    if number%i==0:
        divisor_sum+=i      
if divisor_sum == number and number != 0:
    print(f"{number} is a perfect number!")
    print(f"Because the sum of its divisors is {divisor_sum}")
else:
    print(f"{number} is not a perfect number.")