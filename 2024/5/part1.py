from arg_utils import get_file_name

# Use the utility function to get the file name
file_name = get_file_name(__file__)

sort_orders = []
books = []
with open(file_name, 'r') as file:
    for line in file:
        if "|" in line:
            sort_orders.append(line.strip())
            continue
        if "," in line:
            books.append(line.strip().split(","))

valid_books = []
for pages in books:
    prev_page = 0
    valid = True

    for page in pages:
        if prev_page == 0:
            prev_page = page
            continue
        
        if str(prev_page) + "|" + str(page) in sort_orders:
            prev_page = page
            continue

        valid = False
    
    if valid:
        valid_books.append(pages)

total = 0
for book in valid_books:
    middle_value = book[len(book) // 2]
    total += int(middle_value)


print("Total number: ", total)