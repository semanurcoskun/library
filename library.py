def student_Dict():
    new_file = open("students.txt", "r")
    students_ = new_file.readlines()
    myDict = {}
    for line in students_:
        myList = line.split(",")
        length = len(myList)
        for i in range(length):
            myList[i] = myList[i].strip()
        myDict[myList[0]] = myList[1:]
    new_file.close()
    return myDict


def books_Dict():
    new_file = open("books.txt", "r")
    books_ = new_file.readlines()
    myDict = {}
    for line in books_:
        myList = line.split(",")
        length = len(myList)
        for i in range(length):
            myList[i] = myList[i].strip()
        myDict[myList[0]] = myList[1:]
    new_file.close()
    return myDict


def student_menu():
    choose = input(
        """What would you like to do?
list books, list available books, search by ISBN, search by book name or log out. """
    )
    print()
    if choose == "list books":
        print("Listing all the books...")
        list_books()
    elif choose == "list available books":
        print("Listing all the available books for you to check...")
        list_available()
    elif choose == "search by ISBN":
        search_isbn()
    elif choose == "search by book name":
        search_book()
    elif choose == "log out":
        logout()
    else:
        print("Undefined request.\n")
        student_menu()


def librarian_menu():
    choose = input(
        """What would you like to do?
list books, list checked books, add a book, delete a book,
search by ISBN, search by book name, check a book, list students or log out. """
    )
    print()
    if choose == "list books":
        print("Listing all the books:")
        list_books()
    elif choose == "list checked books":
        print("Listing all the checked books: ")
        list_checked()
    elif choose == "add a book":
        add_book()
    elif choose == "delete a book":
        delete_book()
    elif choose == "search by ISBN":
        search_isbn()
    elif choose == "search by book name":
        search_book()
    elif choose == "check a book":
        check_book()
    elif choose == "list students":
        print("Listing all the students...")
        list_students()
    elif choose == "log out":
        logout()
    else:
        print("Undefined request.\n")
        librarian_menu()


def list_books():
    for i in books.values():
        print(f"{i[0]} by {i[1]}")
    print()
    remenu()


def list_checked():
    for i in books.values():
        if i[2] == "T":
            print(f"{i[0]} by {i[1]}")
    print()
    remenu()


def list_available():
    for i in books.values():
        if i[2] == "F":
            print(f"{i[0]} by {i[1]}")
    print()
    remenu()


def add_book():
    new_file = open("books.txt", "a")
    isbn = input("Enter the ISBN number: ")
    name = input("Enter the book's name: ")
    author = input("Enter the author's name: ")
    new_file.write(
        f"""
{isbn}, {name}, {author}, F"""
    )
    new_file.close()
    print("Please know that your progress will be saved after you log out.\n")
    check_newline()
    remenu()


def check_newline():
    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("books.txt", "w")
    for line in lines:
        if line.strip() != "":
            file.write(line)
    file.close()


def delete_book():
    new_file = open("books.txt", "w")
    delete = input(
        "Enter the ISBN number of the book that you want to delete from the library: "
    )
    if (delete in books) and (books[delete][2] == "F"):
        del books[delete]
    else:
        print("Book is either checked out or doesn't exist in the library.\n")
    for key, value in books.items():
        if len(value) == 3:
            new_file.write(f"{key}, {value[0]}, {value[1]}, {value[2]}\n")
        else:
            new_file.write(f"{key}, {value[0]}, {value[1]}, {value[2]}, {value[3]}\n")
    print("")
    new_file.close()
    remenu()


def search_isbn():
    isbn = input("Enter the ISBN number of the book you want to search for: ")
    print("Searching for the ISBN number...")
    if isbn in books:
        print(
            f"{books[isbn][0]} by {books[isbn][1]} is the book you were looking for.\n"
        )
    remenu()


def search_book():
    name = input("Enter the name of the book you want to search for: ")
    print("Searching for the book name...")
    for i in books.values():
        if name in i[0]:
            print(f"{i[0]} by {i[1]} might be the book you are looking for.")
    print()
    remenu()


def check_book():
    print(
        """Know that if you try to check an already checked book
or to check it to someone who doesn't exist; you will be sent to menu.\n"""
    )
    book = input("Which book do you want to check? ")
    for i in books.values():
        if (book in i[0]) and (i[2] == "F"):
            student = input("Which student do you want to check it to? ")
            for j in students.values():
                if student in j[0]:
                    book_file = open("books.txt", "w")
                    # student_file = open("students.txt", "w")
                    i[2] = "T"
                    # j.append("T")
                    i.append(student)
                    for key, value in books.items():
                        if len(value) == 3:
                            book_file.write(
                                f"{key}, {value[0]}, {value[1]}, {value[2]}\n"
                            )
                        else:
                            book_file.write(
                                f"{key}, {value[0]}, {value[1]}, {value[2]}, {value[3]}\n"
                            )
                    book_file.close()
                    # for key, value in students.items():
                    # if len(value) == 1:
                    # student_file.write(f"{key}, {value[0]}\n")
                    # else:
                    # student_file.write(f"{key}, {value[0]}, {i[0]}\n")
                    # student_file.close()
    print("")
    remenu()


def list_students():
    for i in students.values():
        print(i[0], end="")
        for j in books.values():
            if (len(j) == 4) and (i[0] == j[3]):
                print(":")
                print(j[0], end="")
        print("\n")
    remenu()


def exit_():
    print(
        """Log in failed!
Have a good day."""
    )
    return 0  # as an exit code 0; meaning there was something wrong


def logout():
    print(
        """Log out is successful.
Have a good day."""
    )
    return 1  # as an exit code 1; meaning the user chose to log out


def remenu():
    if user == "student":
        student_menu()
    elif user == "librarian":
        librarian_menu()


students = student_Dict()
books = books_Dict()
print("Please log in!")
librarian = "librarian"
l_password = "msku92.library"
username = input("Please enter your ID: ")
if username in students.keys():
    user = "student"
    print("Log in successful!")
    print(f"Welcome, {students[username][0]}!\n")
    student_menu()
elif username == librarian:
    password = input("Please enter your password: ")
    if password == l_password:
        user = "librarian"
        print("Log in successful!")
        print("Welcome Librarian!")
        librarian_menu()
    else:
        exit_()
else:
    exit_()
