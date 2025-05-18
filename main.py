def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(text)
    print(f"{num_words} words found in the document")
 

def get_book_text(path):
    with open(path) as f:
        return f.read()
    



def word_count(text):
    num_words = len(text.split())
    return num_words

main()