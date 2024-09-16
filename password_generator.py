import random

outputFile = open("random_password.txt", "w")

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Generate random uppercase and lowercase letters, digits, and punctuation signs
uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
lowercaseLetter3 = chr(random.randint(97,122))
lowercaseLetter4 = chr(random.randint(97,122))
lowercaseLetter5 = chr(random.randint(97,122))
lowercaseLetter6 = chr(random.randint(97,122))
lowercaseLetter7 = chr(random.randint(97,122))
lowercaseLetter8 = chr(random.randint(97,122))
lowercaseLetter9 = chr(random.randint(97,122))
lowercaseLetter10 = chr(random.randint(97,122))
digit1 = str(random.randint(0,9))
digit2 = str(random.randint(0,9))
digit3 = str(random.randint(0,9))
digit4 = str(random.randint(0,9))
digit5 = str(random.randint(0,9))
digit6 = str(random.randint(0,9))
punctuationSign1 = random.choice(['!', '@', '#', '$', '%', '&', '*', '.'])
punctuationSign2 = random.choice(['!', '@', '#', '$', '%', '&', '*', '.'])

# Shuffle the characters to create a random password without a specified pattern
password1 = shuffle(uppercaseLetter1 + (uppercaseLetter2)*2 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + lowercaseLetter5 + (digit1)*2 + digit2 + punctuationSign1 + punctuationSign2)
password2 = shuffle(lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + lowercaseLetter5 + lowercaseLetter6 + lowercaseLetter7 + lowercaseLetter8 + lowercaseLetter9 + lowercaseLetter10)
password3 = shuffle(digit1 + digit2 + digit3 + digit4)
password4 = shuffle(uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4)
password5 = shuffle(digit1 + digit2 + digit3 + digit4 + digit5 + digit6)


def run():
    #Output the generated password
    print("\nPassword Types:  1 - Multi-Scramble, 2 - Lowercase Only, 3 - PIN, 4 - Letters only, 5 - Numbers only")
    print("\tChoose Password type: ")
    choice = input()

    if choice == "1":
        print("Generated password:", password1)
        outputFile.write(password1 + "\n")
    elif choice == "2":
        # Remove the characters that are not required (punctuation, comma, underscore etc...)
        print("Generated password:", password2)
        outputFile.write(password2 + "\n")
    elif choice == "3":
        # 4 Numbers
        print("Generated password:", password3)
        outputFile.write(password3 + "\n")
    elif choice == "4":
        # Letters only, removes punctuation and numbers
        print("Generated password:", password4)
        outputFile.write(password4 + "\n")
    elif choice == "5":
        # Numbers only, removes punctuation and letters
        print("Generated password:", password5)
        outputFile.write(password5 + "\n")
    else:
        print("Invalid choice, please try again!")
        run()

run()