def encode(data):
    encode_data = ""
    for letter in data:
        if ord(letter) <= 57 and ord(letter) >= 55:
            encode_data += chr(ord(letter) + 3 - 10)
        elif ord(letter) <= 122 and ord(letter) >= 120:
            encode_data += chr(ord(letter) + 3 - 26)
        elif ord(letter) <= 90 and ord(letter) >= 88:
            encode_data += chr(ord(letter) + 3 - 26)
        else:
            encode_data += chr(ord(letter) + 3)
    return encode_data
def decode(data):
    #implement decoder logic
    return data


def main():
    encoded_password = ""
    while True:
        user_input = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")

        if user_input == '1':
            user_password = input("Please enter your password to encode: ")
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")
        elif user_input == '2':
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif user_input == '3':
            return
        else:
            print("Invalivd Input")


if __name__ == '__main__':
    main()
