class Book:
    def __init__(self, title, author, isbn,quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = int(quantity)

    def mark_as_borrowed(self):
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False

    def mark_as_returned(self):
        self.quantity += 1

    def __str__(self):
        status = "Borrowed" if self.quantity==0 else "Available"
        return f"{self.title} by {self.author} [ISBN: {self.isbn}] — ({status})"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.max_limit = 2        

    def can_borrow(self):
        if len(self.borrowed_books) < self.max_limit:
            return True
        return False

    def remove_book(self, book):
        self.borrowed_books.remove(book)

class PremiumMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.max_limit = 5


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, isbn,quantity):
        if isbn in self.books:
            print(f"This book (ISBN: {isbn}) already exists!")
            return 
            
        new_book = Book(title, author, isbn,quantity)
        self.books[isbn] = new_book
        print(f"Book '{title}' added successfully!")

    def register_member(self, member_id, member_name, is_premium=False):
        if member_id in self.members:
            print("This user already exists!")
            return 
      
        if is_premium:
            new_member = PremiumMember(member_id, member_name)
        else:
            new_member = Member(member_id, member_name)
            
        self.members[member_id] = new_member
        print(f"User '{member_name}' created successfully!")

    def lend_book(self, member_id, isbn):
        
        if member_id not in self.members:
            print(f"Error: Member ID {member_id} not found.")
            return
        if isbn not in self.books:
            print(f"Error: Book ISBN {isbn} not found.")
            return
            
        member = self.members[member_id]
        book = self.books[isbn]
        
        if not member.can_borrow():
            print(f"Error: {member.name} has reached their limit of {member.max_limit} books.")
            return
            
        if book.mark_as_borrowed():
            member.add_book(book)
            print(f"Success: '{book.title}' has been lent to {member.name}.")

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            print(f"Error: Member ID {member_id} not found.")
            return
        if isbn not in self.books:
            print(f"Error: Book ISBN {isbn} not found.")
            return
        member = self.members[member_id]
        book = self.books[isbn]
        
        if book not in member.borrowed_books:
            print(f"Error: {member.name} does not currently have '{book.title}' checked out.")
            return
            
        member.remove_book(book)
        book.mark_as_returned()
        
        print(f"Success: '{book.title}' has been successfully returned by {member.name}!")



    def display_books(self):
        print("Available Books:")
        for book in self.books.values():
            print(book)
