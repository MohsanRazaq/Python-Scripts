''''
There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. 
You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false.'''

#first we have to check for both cases like divisible by 3 or 5..if we check either by 5 or 3 this is True so our main condition will be null void 

def fizzBuzz(num):
    # Write your code here.
    if num%3==0 and num%5==0:
        return 'FizzBuzz'
    elif num%3==0:
        return 'Fizz'
    elif num%5==0:
        return 'Buzz'
    else:
        return num
        
        
#Test cases
# A dictionary of {Input: Expected Output}
test_data = {
    3: "Fizz",
    10: "Buzz",
    15: "FizzBuzz",
    7: "Error"
}
#  Tests
print("--- Running Tests ---")
for input_val, expected in test_data.items():
    result = fizzBuzz(input_val)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    print(f"Input: {input_val} | Result: {result} | {status}")

