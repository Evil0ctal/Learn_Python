def main():
    line = input("Enter the file name here: ")
    # line = "Explore infinite worlds and build everything from the simplest of homes to the grandest of castles."
    counts = 0
    for words in line.split(' '):
        counts += 1
        #print(words)
    print("\nTotal words: " + str(counts))

if __name__ == '__main__':
    main()

"""
Enter the file name here: Explore infinite worlds and build everything from the simplest of homes to the grandest of castles

Total words: 16
"""