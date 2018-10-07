'''
 __  __     __         ______   ______     ______     __     ______     ______
/\ \/\ \   /\ \       /\__  _\ /\  ___\   /\  == \   /\ \   /\  __ \   /\  == \
\ \ \_\ \  \ \ \____  \/_/\ \/ \ \  __\   \ \  __<   \ \ \  \ \ \/\ \  \ \  __<
 \ \_____\  \ \_____\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\  \ \_____\  \ \_\ \_\
  \/_____/   \/_____/     \/_/   \/_____/   \/_/ /_/   \/_/   \/_____/   \/_/ /_/

Description: Convert zero width characters to binary to ascii then back to zero width characters

Author: Trenches of IT

Version: 1.0

'''
import binascii
import re
import sys

#Allows user input to select path
def menu():

    print("     __  __     __         ______   ______     ______     __     ______     ______ \n",
          "   /\ \/\ \   /\ \       /\__  _\ /\  ___\   /\  == \   /\ \   /\  __ \   /\  == \ \n",
          "   \ \ \_\ \  \ \ \____  \/_/\ \/ \ \  __\   \ \  __<   \ \ \  \ \ \/\ \  \ \  __< \n",
          "    \ \_____\  \ \_____\    \ \_\  \ \_____\  \ \_\ \_\  \ \_\  \ \_____\  \ \_\ \_\ \n",
          "     \/_____/   \/_____/     \/_/   \/_____/   \/_/ /_/   \/_/   \/_____/   \/_/ /_/ \n",
          "Author: Trenches of IT \n",
          "Version: 1.0 \n\n",
          "Primary Functions: \n",
          "  (1) Convert zero-width characters into message \n",
          "  (2) Convert message into zero width characters \n\n",
          "Secondary Functions: \n",
          "  (a) Convert copied zero-width text into binary \n",
          "  (b) Convert binary into ascii \n",
          "  (c) Convert ascii into binary \n",
          "  (d) Convert binary into zero-width characters \n\n",
          "(x) Exit \n")
    userInput = input("Please Enter an option: ")

    if userInput == "a":
        convertBin()
    elif userInput == "b":
        binAsc()
    elif userInput == "c":
        ascBin()
    elif userInput == "d":
        binZero()
    elif userInput == "1":
        zeroMessage()
    elif userInput == "2":
        messageZero()
    elif userInput == "x":
        print("Goodbye!")
        sys.exit()
    else:
        print("Please enter a valid option: ")
        menu()

#Converts zero-width characters within string to hidden message(if possible)
def zeroMessage():
    input("Paste text with suspected zero width characters into input.txt, then press enter to continue...")


    try:
        with open('input.txt', 'r') as file:
            filedata = file.read()
    except:
        print("Error: File could not be found, or message is not found.")
        runAgain()

    try:
        punctRemove = re.sub("\d+", "", filedata)
        bs = bytes(punctRemove, encoding='utf-8')
        filedataStripped = bs.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\xb9', b'1')
        finalfiledata = filedataStripped.replace(b'\xc3\xa2\xe2\x82\xac\xc5\x92', b'0')

        decodedata = finalfiledata.decode("utf-8")

        binInput = re.sub("\D", "", decodedata)
        print("Binary: " + binInput)

        n = int(binInput, 2)
        output = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        print("Hidden Message: " + output)

        file.close()

    except:
        print("No hidden message found.  Check input.txt for accuracy.")
        runAgain()

    runAgain()
#Converts ascii to zero-width characters
def messageZero():
    try:
        textToBinary = input("Please enter the message to convert into zero width: ")
        asciiToBinary = bin(int.from_bytes(textToBinary.encode(), "big"))
        n = asciiToBinary[2:]
        zeroReplaced = n.replace("0", "&zwnj;")
        output = zeroReplaced.replace("1", '&#8203;')
        print("Converted string: " + output)
    except:
        print("Error: Try Again.")
    runAgain()

#Converts text with zero width characters into binary
def convertBin():
    input("Paste text with suspected zero width characters into input.txt, then press enter to continue...")
    try:
        with open('input.txt', 'r') as file :
            filedata = file.read()
            filedataStripped = re.sub("\d+", "", filedata)
    except:
        print("Error: File could not be found, or message is not found.")
        runAgain()
    bs = bytes(filedataStripped, encoding='utf-8')

    filedataStripped = bs.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\xb9', b'1')
    finalfiledata = filedataStripped.replace(b'\xc3\xa2\xe2\x82\xac\xc5\x92', b'0')

    decodedata = finalfiledata.decode("utf-8")

    finalMessage = re.sub("\D", "", decodedata)

    print("Converted Value: " + finalMessage)
    file.close()
    runAgain()

#Converts Binary to zero width characters
def binZero():
    binaryInput = input("Enter binary to convert into zero width characters: ")
    zeroReplaced = binaryInput.replace("0", "&zwnj;")
    output = zeroReplaced.replace("1", '&#8203;')
    print("Converted string: " + output)
    runAgain()

#ascii to binary conversion
def ascBin():
    try:
        textToBinary = input("Please enter the message to convert into binary: ")
        asciiToBinary = bin(int.from_bytes(textToBinary.encode(), "big"))
        n = asciiToBinary[2:]
        print("Converted string: " + n)

    except:
        invalidInput = input("Error: Invalid input.  Would you like to try again? (y/n)")
        if invalidInput == "y":
            ascBin()
        else:
            menu()
    runAgain()

#Binary to ascii conversion
def binAsc():
    try:
        binInput = input("Please enter binary: ")
        n = int(binInput, 2)
        output = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        print("Message: " + output)

    except:
        print("Binary does not convert to ascii!")
        runAgain()

    runAgain()
#Re-runs the initial menu() function
def runAgain():
    answer = input("Would you like to run program again?(y/n): ")
    if answer == "y":
        menu()
    elif answer == "n":
        print("Goodbye!")
        sys.exit()
    else:
        print("Please enter a valid option: ")
        runAgain()

menu()