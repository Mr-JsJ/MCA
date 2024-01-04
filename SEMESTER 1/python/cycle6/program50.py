class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name

class Book(Publisher):
    def __init__(self, publisher_id, publisher_name, title, author):
        super().__init__(publisher_id, publisher_name)
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPublisher ID: {self.publisher_id}\nPublisher Name: {self.publisher_name}")

class Python(Book):
    def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        super().__init__(publisher_id, publisher_name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display_info(self):
        super().display_info()
        print(f"Price: ${self.price}\nNumber of Pages: {self.no_of_pages}")

publisher_id = input("Enter Publisher ID: ")
publisher_name = input("Enter Publisher Name: ")
title = input("Enter Title of the book: ")
author = input("Enter Author of the book: ")
price = float(input("Enter Price of the book: "))
no_of_pages = int(input("Enter Number of Pages: "))

python_book = Python(publisher_id, publisher_name, title, author, price, no_of_pages)

print("\nInformation about the Python book:")
python_book.display_info()
