a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']


def encrypt(inp, s, name):
    f = open(name + "_enc.txt", "a") # adding the _name 

    for each in inp:
        for i in each:  # read every character in input file
            if i in a:  # check if it is small letter
                if a.index(i) + s > 25:  # check if after shifting it goes out of index
                    f.write(a[a.index(i) + s - 26])
                else:
                    f.write(a[a.index(i) + s])
            elif i in A:  # check if it is capital letter
                if A.index(i) + s > 25:
                    f.write(A[A.index(i) + s - 26])
                else:
                    f.write(A[A.index(i) + s])
            else:
                f.write(i)
    f.close


def decrypt(inp, s, name):
    f = open(name + "_dec.txt", "a") # adding the _name 

    for each in inp:
        for i in each:  # read every character in input file
            if i in a:  # check if it is small letter
                f.write(a[a.index(i) - s])
            elif i in A:  # check if it is capital letter
                f.write(A[A.index(i) - s])
            else:
                f.write(i)
    f.close

def start():
    
    key = 3
    input_name = input("Please enter the input file name with extension: ")
    file = open(input_name, 'r')
    shift = key #fixed to key 3 according to the instructions given by our professor 
    print("1.Encrypt\n2.Decrypt")
    choice = int(input("Your choice: "))

    if choice == 1:
        print("Successfully Encrypted")
        encrypt(file, shift, input_name[:-4])
    else:
        print("Successfully Decrypted")
        decrypt(file, shift, input_name[:-4]) # Passing only the textfile name, not the extension and print
    cont=input("Press q to quit or any other letter to start a new inquire ")
    if cont=='q':
        return
    else:
        start()
print("Welcome to the encryption/decryption app for files, please input a file name and follow instructions")
start()
