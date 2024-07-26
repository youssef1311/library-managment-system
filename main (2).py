# step1 :Define data structures
books = {
    "9780316769488": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "is_borrowed": False},
    "9780061120084": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "is_borrowed": False}
}

#step 2 membership 
members = {
    "M1001": {"name": "Ahmed", "borrowed_books": []},
    "M1002": {"name": "Mohamed", "borrowed_books": []}
}

# step3 : Define function for add book 
def add_book(isbn, title, author):
    if isbn not in books:
        books[isbn] = {"title": title, "author": author, "is_borrowed": False}
    else:
        print("Book already exists.")


# step4 : Define function for add member 
def add_member(member_id, name):
    if member_id not in members:
        members[member_id] = {"name": name, "borrowed_books": []}
    else:
        print("Member already exists.")
        
        
        
def borrowed_books(member_id,isbn):
    if member_id in members and isbn in books:
        member=members[member_id]
        book=books[isbn]
        if not book["is_borrowed"]:
            book ["is_borrowed"]=True
            member["borrowed_books"].append(isbn)
        else:
            print ("book is not here")
    else:
        print("member_id is not invalid")
        
        
def return_book(member_id,isbn):
    if member_id in members and isbn in books:
        member=members[member_id]
        book=books[isbn]
        if isbn in member["borrowed_books"]:
            book ["is_borrowed"]=False
            member["borrowed_books"].remove(isbn)
        else:
            print ("book borrowed by different member")
    else:
        print("invalid book_id member_id")
        
def dispLAY_BOOKS():
    print (books)
def dispLAY_MEMBERS():
    print (members)
dispLAY_BOOKS()
dispLAY_MEMBERS()
        
            
            
def main():
    while True:
        print("***************************************************************")
        print("***************************************************************")    
        print(          "WELCOME TO LIBRARY MANGEMENT SYSTEM                     ")   
        print("***************************************************************")
        print("***************************************************************")
        print("1 to add book")
        print("2 to add member")
        print("3 to borrow book")
        print("4 to return book")
        print("5 to display book")
        print("6 to display member")
        print("7 to exit")
        choice=input("choose ur choice:___")
main()        
        