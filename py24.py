#Print the following information in the following format.
books = [
        ("The 7 Habits of Highly Effective People", "Stephen R.Covey"),
        ("How to Win Friends and Influence People", "Dale Carnegie"),
        ("Atomic Habits", "James Clear"),
        ("The 4-Hour Work Week", "Tim Ferriss"),
        ("Deep Work", "Cal Newport"),
        ("So Good They Can't Ignore You", "Cal Newport"),
        ("Digital Minimalism", "Cal Newport"),]
for index,(book,author) in enumerate(books):
    print(f"{index+1}. Boook: {book} Author: {author} ")