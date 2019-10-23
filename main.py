"""
main file
"""

import menu
import analyzer


def main():
    """
    runs menu and functions
    """
    while True:
        menu.menu_here()

        choice = input()
        choice.lower()

        if choice == "q":
            print("Bye Bye")
            break

        elif choice == "lines":
            print()
            print("Number of lines: " + str(analyzer.lines()))
            print()

        elif choice == "words":
            print()
            print("Number of words: " + str(analyzer.word_count()))
            print()

        elif choice == "letters":
            print()
            print("Number of letters: " + str(analyzer.letters()))
            print()

        elif choice == "word frequency":
            print()
            analyzer.word_frequency()
            print()

        elif choice == "letter frequency":
            print()
            analyzer.letter_frequency()
            print()

        elif choice == "all":
            analyzer.do_all()

        elif choice == "change":
            print(analyzer.change())

        else:
            print("You inserted something strange")


if __name__ == "__main__":
    main()
