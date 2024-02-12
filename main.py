# def main():
#     path_to_file = "books/frankenstein.txt"
    
#     with open(path_to_file, 'r') as f:
#         file_content = f.read()
#         print(file_content)
        
# if __name__ == "__main__":
#     main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()