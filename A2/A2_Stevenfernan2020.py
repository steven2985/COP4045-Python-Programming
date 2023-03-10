# Steven Fernandez Z23571583 COP4045 A2

# This program prompts the user for a choice between encrypt and decrypt a message then the user input a 
# message after this the message is either encrypted or decrypted based on the user's choice finally 
# the program prompts the user for another try or exit the program

# The decrypt function will decrypt the messages 
def decrypted(string,shift):
    ciper = ''
    for char in string:
        if char == ' ':
            ciper = ciper + char
        elif char.isupper():
            ciper = ciper + chr((ord(char) - shift - 65) % 26 + 65) # Reason to substract 65 is that the ASCII 
                                                                    # values for the alphabet starts at 65 for upper case letters and end in 97
        else:
            ciper = ciper + chr((ord(char) - shift - 97) % 26 + 97) # Reason to substract 97 is that the ASCII 
                                                                    # values for the alphabet starts at 97 for the lower case letters and en in 123
    return ciper


#The encrtpt function will encrypt the message
def encrypt(string,shift):
    ciper = ''
    for char in string:
        if char ==' ':
            ciper = ciper + char
        elif char.isupper():
            ciper = ciper + chr((ord(char) + shift - 65) % 26 + 65) # Reason to substract 65 is that the ASCII 
                                                                    # values for the alphabet starts at 65 for upper case letters and end in 97
        else:
            ciper = ciper + chr((ord(char) + shift - 97) % 26 + 97) # Reason to substract 97 is that the ASCII 
                                                                    # values for the alphabet starts at 97 for the lower case letters and en in 123
    return ciper

# Welcoming message 
choice = int(input("Welcome to the Caesar cipher app. Would you like to start? (Enter 1 for yes. Enter 2 to end program)  "))

# While loop to check for user's choice 
while choice == 1:
    select = int(input("Enter 1 for decryption and 2 for encryption: "))

    if select == 1:
        text=input("Enter your text: ")
        s=int(input("please enter the key: "))
        print("The original message is: ",text," !")
        print("The encripted message is : ",decrypted(text,s))
        print("Would you like to try another? If not please enter 3")

    elif select == 2:
        text=input("Enter your text: ")
        s=int(input("Please enter the key: "))
        print("The original message is: ",text," !")
        print("The Decrypted message is : ",encrypt(text,s))
        print("Would you like to try another? If not please enter 3")

    else:
        print("Have a good day")
        break
else:
    print("Thank you for using this app have a good day.")