def encode(data):
    encode_data = ""
    for letter in data:
        #Checks if letter is a number and is near the end, if value is 7,8,9 it turns into 0,1,2
        if ord(letter) <= 57 and ord(letter) >= 55:
            encode_data += chr(ord(letter) + 3 - 10)
        #number is not near the end 
        else:
            encode_data += chr(ord(letter) + 3)
    return encode_data
    

def decode(data):
    #implement decoder logic
    password = ""
    for digit in data:
        shifted_digit = str((int(digit) - 3) % 10)
        password += shifted_digit
    return password


def main():
    encoded_password = ""
    while True:
        user_input = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        #Encode menu option
        if user_input == '1':
            user_password = input("Please enter your password to encode: ")
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")
        #Decode menu option
        elif user_input == '2':
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        #Exit
        elif user_input == '3':
            return
        #Invalid Input
        else:
            print("Invalivd Input")


if __name__ == '__main__':
    main()
