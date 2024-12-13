from collections import defaultdict, deque
from arg_utils import get_file_name

# Use the utility function to get the file name
file_name = get_file_name(__file__)

sort_orders = []
books = []

with open(file_name, 'r') as file:
    for line in file:
        if "|" in line:
            sort_orders.append(tuple(map(int, line.split('|'))))
            continue
        if "," in line:
            books.append(list(map(int, line.strip().split(","))))

def is_ordered(book, rules):
        for i in range(len(book)):
            for j in range(i + 1, len(book)):
                if (book[j], book[i]) in rules:  # Check for reverse rule
                    return False
        return True

def order_book(book, rules):
    n = len(book)
    ordered = False
    while not ordered:
        ordered = True
        for i in range(n):
            for j in range(i + 1, n):
                if (book[j], book[i]) in rules:
                    book[i], book[j] = book[j], book[i]
                    ordered = False
    return book

incorrectly_ordered_books = []
for book in books:
    if not is_ordered(book, sort_orders):
        incorrectly_ordered_books.append(book)

middle_page_sum = 0
for book in incorrectly_ordered_books:
    ordered_book = order_book(list(book), sort_orders)  # Create a copy
    middle_index = len(ordered_book) // 2
    middle_page_sum += ordered_book[middle_index]

print(middle_page_sum)