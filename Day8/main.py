from art import logo

def ceaser_cipher(letter, shift, direction):
    if letter == "":
        print("You have entered an empty message.")
        return ""

    if direction == "decode":
        shift = -shift

    result = ""
    for char in letter:
        if char.isalpha():
            index =ord(char) - ord('a')
            new_index = (index + shift) % 26
            result  += chr(new_index + ord('a'))
        else:
            result += char
    return result

run = True
while run:
    print(logo)
    op_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    op_letter = input('Type your message: ').lower()
    op_shift = int(input('Type your shift number: '))
    print(ceaser_cipher(op_letter, op_shift, op_direction))

    choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
    if choice == 'no':
        run = False
        print("Goodbye.")