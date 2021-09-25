class Harsh_libs :
    def __init__(self , list , name):
        self.booklist = list
        self.name = name
        self.dict = {}
    def display_books(self):
        print("We have the following books in " ,self.name ,":")
        for Books in self.booklist:
            print(Books)

    def Lend_books(self , user , book):

        if book not in self.dict.keys():
            self.dict.update({book:user})
            print("Borrowed the book successfully")

        else :
            print("Book is already borrowed by" , self.dict[book])


    def Return_books(self,book):
        self.dict.pop(book)
        print("Returned the book successfully")


    def Donate_books(self, book):
        self.booklist.append(book)
        print("Donated the book successfully")

if __name__== '__main__':
    harsh = Harsh_libs(['Calculus','Algebra','Statistics','Arithmetics','logarithms'] ,'Maths Library')
    while (True) :
        print(f"Welcome to the {harsh.name}. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Return a Book")
        print("4. Donate a Book")

        user_choice = int(input())

        if user_choice == 1:
            harsh.display_books()

        if user_choice == 2 :
            harsh.display_books()
            user = input("Please enter the name of the user:\n")
            book = input("Please enter the name of the book you want to Borrow:\n")
            harsh.Lend_books(user,book )

        if user_choice == 3 :
            book = input("Enter the name of the book you want to return.\n")
            harsh.Return_books(book)

        if user_choice == 4 :
            book = input("Enter the name of the book you want to Donate : \n")
            harsh.Donate_books(book)
            continue

        user_choice2 = input("Press Q to quit and C for continue.")


        if user_choice2=="Q" :
            exit()

        elif user_choice2 !="Q":
            continue