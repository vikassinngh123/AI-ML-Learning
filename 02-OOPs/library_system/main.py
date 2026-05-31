from library_models import Library

def run_library_system():
    my_library = Library()
    
    while True:
        print("\n" + "="*30)
        print(" 📚 LIBRARY ADMIN DASHBOARD ")
        print("="*30)
        print("1. Add a New Book")
        print("2. Register a New Member")
        print("3. Lend a Book")
        print("4. Return a Book")
        print("5. Display All Books")
        print("6. Exit System")
        print("="*30)
        
        choice = input("Select an admin action (1-6): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            my_library.add_book(title, author, isbn)
            
        elif choice == '2':
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            is_premium = input("Is this a Premium Member? (y/n): ").lower().strip() == 'y'
            my_library.register_member(member_id, name, is_premium)
            
        elif choice == '3':
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN to lend: ")
            my_library.lend_book(member_id, isbn)
            
        elif choice == '4':
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN to return: ")
            my_library.return_book(member_id, isbn)
            
        elif choice == '5':
            my_library.display_books()
            
        elif choice == '6':
            print("Shutting down Library Admin System. Goodbye!")
            break
            
        else:
            print("Invalid input. Please select a number from 1 to 6.")

if __name__ == "__main__":
    run_library_system()
