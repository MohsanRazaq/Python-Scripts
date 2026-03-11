''''The "Digit High-Low" (Comparison Logic)
Challenge: 
Without using max() or min(),
find the largest and smallest digit within a single number.

Example: Input 2815 → Output: "Largest is 8, Smallest is 1".

Hint: Initialize largest = 0 and smallest = 9.
As you peel off digits using % 10, compare each digit to your current largest and smallest and update them accordingly.
'''

number=int(input('Enter Number: '))
largest=0
smallest=9
while number>0:
    digit=number%10
    if digit<smallest:
        smallest=digit
    if digit>largest:
        largest=digit
    number//=10
print(f'The Largest Digit is {largest}\nThe smallest Digit is {smallest}')