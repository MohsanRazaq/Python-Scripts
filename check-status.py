'''
PROBLEM: Integer Status Check
URL: https://www.geeksforgeeks.org/problems/check-the-status/1?page=1&category=python&sortBy=submissions
DESCRIPTION:
Given two integer variables a and b, and a boolean variable flag. 
Return True if:
1. Either a or b (not both) is non-negative and flag is False.
2. Both a and b are negative and flag is True.
Otherwise, return False.
'''

def check_status(x,y,flag):
#we will first check 2 conditions because if we try by 1 condition, the result will be wrong ,un expected behaviour.
# 2) both variables -tive and flag is true
    if flag:
        return x<0 and y<0
    # Either one is -tive and one is positive and flag is  False
    else:
        return x<0 or y<0 or (x <0 and y<0)     

# Practice Test Cases
print(f"Test 1: {check_status(-1, -1, False)}")   # Expected: True
print(f"Test 2: {check_status(-182, -9121, True)}") # Expected: True
print(f"Test 3: {check_status(5, 3, True)}")      # Expected: False