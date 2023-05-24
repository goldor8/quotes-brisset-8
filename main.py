from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. Display quote")
    print("3. Add quote")
    print("4. Exit")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input(">> ")
        
        if choice == "random":
            print_quote(random_quote(quotes))
        elif choice == "display":
            count = int(input("Enter the number of quotes to display"))
            display_quotes(quotes,count)
        elif choice == "add":
            add_quote(quotes, "quotes.txt")
        elif choice == "exit:
            print("Good bye...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()