import sys, re

while True:
    firstAns = input("\nThis program will check wether a string contains a vowel or not."
                 "\nType 'q' to quit or press enter to continue")

    if firstAns.lower() == "q":
        print("-\nBye!")
        sys.exit()

    vowelNumber = 0  
    vowels = ["a", "e", "i", "o", "u"] 

    string = input("-\nEnter your string = ") 
    string = string.lower()

    for i in string:
        if i in vowels:
            vowelNumber += 1
    
    print("-\nThere are %d vowels in your string!" % vowelNumber)
            