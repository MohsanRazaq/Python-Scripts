''''
There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. 
You are in trouble if both of them are angry or no one of them is angry.
Url=https://www.geeksforgeeks.org/problems/if-loop-python/1?page=1&category=python&sortBy=submissions
Now, complete the function which returns true if you are in trouble, else return false.'''

#first we have to check for both cases like divisible by 3 or 5..if we check either by 5 or 3 this is True so our main condition will be null void 

def friends_in_trouble(j_angry, s_angry):
    if j_angry==True and s_angry==True:
        return True
    elif j_angry==False and s_angry==False:
        return True
    else:
        return False
#Test cases
'''
Example 1:

Input:
j_angry = True, s_angry = True
Output:
True
Explanation:
Since both of them are angry, you are in trouble.
'''
print(f'When Both  angry: {friends_in_trouble(True,True)}')
 

'''
Example 2:

Input:
j_angry = True, s_angry = False
Output:
False
Explanation:
Only one of them is angry, you are not in trouble.'''
print(f'When Both  angry: {friends_in_trouble(True,False)}')
 