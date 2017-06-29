alphabet =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def decrypt():
        string = (input("Enter the cipher text:")).upper()
        shift = int(input(" What is the shift amount:"))
        for i in (string):
                if i in alphabet:
                        print(alphabet[(alphabet.index(i)-shift)%26],end='')
                else:
                        print(i,end='')
def encrypt():
        string = (input("Enter the plaintext:")).upper()
        shift = int(input(" What is the shift amount:"))
        for i in (string):
                if i in alphabet:
                        print(alphabet[(alphabet.index(i)+shift)%26],end='')
                else:
                        print(i, end='')
        print("")

def main():
        while(True):
                choice = input("Would you like to encrypt of decrypt")
                if (choice.lower() == "encrypt"):
                        encrypt()
                elif (choice.lower() == "decrypt"):
                        decrypt()
                else:
                        print("invalid input")
main()
