'''
Scenario: You have a log entry string. You need to identify if a specific "Danger Word" exists.

Input: A sentence (e.g., "2026-03-10 CRITICAL Unauthorized access detected on Server01")

Task: Ask the user for a "Search Term" (e.g., "CRITICAL").

Output: Tell the user if the word was found, and at what position (index) in the list it was found.
==============================================================================
we  will try this code by Example
'''
found=False # for tracking
log=("2026-03-10 CRITICAL Unauthorized access detected on Server01").lower()
words=log.split()

#search_term=input("Enter Term you are looking for: ").lower()
search_term="access"
for word in words:
    if word==search_term:
        print(f'Found { search_term} in logs at {words.index(search_term)} before Term {words[words.index(search_term)-1]}')
        found=True
    
if not found:
    print('Not Found')