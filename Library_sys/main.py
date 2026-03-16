''''
Challenge: The Library System
Scenario:
You are managing a Library. Instead of just a name and a count, each book has a Title, an Author, and a Status (Available or Checked Out).
library = [
    {"title": "Python Basics", "author": "mohsan", "available": True},
    {"title": "AI Future", "author": "noni", "available": True},
    {"title": "Data Science", "author": "cyberex", "available": False}
]
Search: Let the user type a book title.

Loop through the list: You have to use for book in library: and then check if book["title"] == user_input:.

Update: If the book is found and available is True, change it to False (check it out). 

Add: Let the user add a new dictionary (a new book) to the list using .append().
'''
library = [
    {"title": "Python Basics", "author": "mohsan", "available": True},
    {"title": "AI Future", "author": "noni", "available": True},
    {"title": "Data Science", "author": "cyberex", "available": False}
]
try:
    print('Welcome to Python Library System\n')
    print('Following Books are Available:\n')
    
    for i,book in enumerate(library,start=1):
        print(f"{i}-->{book['title']} by {book['author']}-{"Available" if book['available'] else 'Sold out' }")
    option=input('Enter Book name or number  you want: ').lower()
    found=False
    for i,book in enumerate(library,start=1):
        if book['title'].lower()==option or str(i)==option:
            if book["available"]:
                book['available']=False
                found=True
                print(f'You successfully, got book.Details are below:\n{book['title']} by {book["author"]}')
    if not found:
        
        print(f"Sorry we dont  have this book-->{option}")
    choice=input('Would you like  to add  Book to our Library. (y/n)')
    if choice.lower()=='y':
        title=input('Enter title: ')
        writer=input('Enter author: ')
        library.append({"title":title,'author':writer,'available':True})
        print(f'You have successfully added following book/books:\n{title} by {writer}')
    else:
        print('Thanks for visting us.\nHave a  nice day (*_*)')
except Exception as e: 
    print(f'error Occured-->{e}')