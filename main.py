
class Library:
    def __init__(self, listOfbooks):
        self.books=listOfbooks
  
    def displayavailBooks(self):
        print("Books Present in the Library are:  ")
        for book in self.books:
             print("* " +book)

    def borrowBooks(self ,bookName):
        if bookName in self.books:
            print(f"you issued {bookName}.Enjoy reading  and return after 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry the book is not available or has been issued someone else....")
            return False

    def returnBooks(self,bookNames):
        self.books.append(bookNames)
        print("Thank you for Returning the book. I hope you Enjoyed Reading.")


class Student:
    def reuestBook(self):
        self.book=input("Enter the Bookname you want to Borrow:")
        return self.book
    def returnBook(self):
         self.book=input("Enter the Bookname You want to Return:")
         return self.book

if __name__== "__main__":
    centralLibrary=Library(["javatpoint","Django","Python","Clrs","Servers"])
    student=Student()
    while(True):
        WelcomeMsg='''=======WELCOME TO LIBRARY=======
             1.List of all Books
             2.Request book
             3.Return Books 
             4.Exit
    '''
        print(WelcomeMsg)
        a=int(input("Enter Your Choice:"))
        if a==1:
            centralLibrary.displayavailBooks()
        elif a==2:
            centralLibrary.borrowBooks(student.reuestBook())
        elif a==3:
            centralLibrary.returnBooks(student.returnBook())
        elif a==4:
            print("Thanks For Choosing Library")
            exit()
        else:
            print("Invalid Choice")
