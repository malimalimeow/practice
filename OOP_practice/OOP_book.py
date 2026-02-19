class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
        self.is_borrowed = False 
    
    def book_info(self):
        print(f"Book information:{self.title}({self.year}),author:{self.author}")

    
    
        
class Library:
    def __init__(self):
        self.library=[]
        
    def add_book(self,book):
        self.library.append(book)
    
    def show_books(self):
        if not self.library:
            print("No books found in the library.")
        
            return
        for book in self.library:
            book.book_info()
    
    def find_book(self,title):
        if not self.library:
            print("No books found in the library.")
            
            return
        for book in self.library:
            if book.title==title:
                book.book_info()
    
    def del_book(self,title):
        if not self.library:
            print("No books found in the library.")
            
            return
        for book in self.library:
            if book.title==title:
                self.library.remove(book)
                print(f"{book.title} is removed!")
    
    def borrow_book(self,title):
        if not self.library:
            print("No books found in the library.")
            
            return
        for book in self.library:
            if book.title==title:
                book.is_borrowed=True 
                print(f"You have borrowed {book.title} successfully.")  
    
    def return_book(self,title):
        if not self.library:
            print("No books found in the library.")
            
            return
        for book in self.library:
            if book.title==title:
                book.is_borrowed=False
                print(f"Thankyou for returning {book.title}.")
    
    def check_status(self,title):
        if not self.library:
            print("No books found in the library.")
            
            return
        for book in self.library:
            if book.title==title:
                if book.is_borrowed:
                    print(f"{book.title} is not available at the moment.")
                if not book.is_borrowed:
                    print(f"{book.title}is available in the library.")
                
                
        
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)

lib = Library()
lib.add_book(book1)
lib.add_book(book2)

lib.check_status("1984")
lib.borrow_book("1984")
lib.check_status("1984")
lib.return_book("1984")
lib.check_status("1984")

