from Art import logo, alphabets


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f'The {cipher_direction}d word is {end_text}\n')


print(logo)
condition = True

while condition:
    direction = input("type 'encode' to encode or type 'decode' to decode\n").lower()
    text = input("Enter a text : \n").lower()
    shift = int(input("Enter shift amount : \n"))
    shift %= 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    go_again = input("type 'yes' to continue, otherwise type 'no'\n")
    if go_again == 'no':
        condition = False
