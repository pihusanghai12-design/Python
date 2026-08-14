books = ["The God of Small Things ", "The White Tiger", "Midnight's Children", "Godaan", "Train to Pakistan"]
copy_count = [5, 1, 0, 6, 2]


library = {book: count for book, count in zip(books, copy_count)}
print(" Library Stock: ", library)


available_books = [book for book in books if library[book] > 0]
print("Books that are available:", available_books)

User_book = input("Which book do you want to borrow? ")


if User_book not in library or library[User_book] == 0:
    print(User_book, "is not available in the libraray.")
    exit()


late_fees = [9, 1, 7, 3, 5]
extra_fee = int(input("Enter the extra library fee to add to every book: "))


updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print("Updated Late Fees are :", updated_fees)

books = books.index(User_book)
chosen_fee = updated_fees[books]
print("Late fee for", books, "after update:", chosen_fee)


library[User_book]=library[User_book] - 1
print(User_book, "borrowed! Remaining copies are:", library[User_book])


