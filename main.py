with open("books/frankenstein.txt") as f:
    file_contents = f.read()  
        

def main():

    def wordcount(book_contents : list) -> None:
        contents = book_contents.split()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(contents)} words found in the document.\n\n")
    
    # function call
    wordcount(file_contents)

    
    def char_count(book_content : str) -> None:
        letters = {}
        letters_list = []
        lowered_string = book_content.lower()
        for letter in lowered_string:
            if letter.isalpha() == True:

                letters |= {letter : lowered_string.count(letter)}
            else: continue

        # Creating a list of dictionaries.
        for k, v in letters.items():
            letters_list.append({"letter" : k, "count" : v})

        
        def sort_on(letters_list : list[dict]) -> int:
            return letters_list["count"]
        
        # Sorts the list by the "count" key in descending order.
        letters_list.sort(reverse=True, key=sort_on)
        for letter in letters_list:
            print(f"The '{letter['letter']}' letter was found {letter['count']} times.")
        print("\n--- End report ---")
            
    # function call
    char_count(file_contents)
# main function call    
main()

