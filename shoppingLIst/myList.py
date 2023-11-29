def my_List():
    while True:
        with open('shoppingList.txt', 'a+') as file:                        # ensuring file is opened with the specifed mode and closed when the indented block is exited ('a' - open the file for writing, '+' - open the file for both writing and reading)
            file.seek(0)                                                    # moving the cursor/pointer to offset 0 (specific position)
            print("Type 'done' anytime to exit. ")
            print("Type 'list' to read and delete items. ")

            item = input("Enter item: ").strip()

            if item.lower() == 'done':
                break
            elif item.lower()=='list':
                items = list(enumerate(file.read().split(), 1))             # enumerate(____, 1) - adding a counter to an iterable, split - spliting the string into a list of substrings
                file.seek(0)
                print(file.read())                                          # reading the content file as a string

                while True:
                    try:
                        remove = int(input("Enter number to delete or 0 to continue: "))
                        if remove==0:
                            break
                        else:
                            del items[remove-1]
                            file.seek(0)                                    # moves the file cursor to the beggining of the file
                            file.truncate()                                 # truncates the file at the current position of the file cursor (removes all content from the current position to the end of the file)
                            for _, item_text in items:
                                file.write(item_text + '\n')
                    except (ValueError, IndexError):
                        print("Invalid input. Enter a valid number o 0 to continue. ")



            else:
                file.write(item + '\n')

if __name__ == "__main__":                                                   # variable set to __main__ when the script is executed directly
 my_List()