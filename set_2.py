def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        return chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))

def caesar_cipher(message, shift):
    return "".join(shift_letter(char, shift) for char in message)

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    else:
        shift = ord(letter_shift) - ord("A")
        return shift_letter(letter, shift)

def vigenere_cipher(message, key):
    extended_key = ""
    key_index = 0
    for char in message:
        if char == " ":
            extended_key += " "
        else:
            extended_key += key[key_index % len(key)]
            key_index += 1

    result = ""
    for i in range(len(message)):
        if message[i] == " ":
            result += " "
        else:
            shift = ord(extended_key[i]) - ord("A")
            result += shift_letter(message[i], shift)
    return result

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    total_chars = len(message)
    cols = total_chars // shift
    return "".join(
        message[(i // shift) + cols * (i % shift)] for i in range(total_chars)
    )

def scytale_decipher(message, shift):
    total_chars = len(message)
    cols = total_chars // shift
    return "".join(
        message[(i % cols) * shift + (i // cols)] for i in range(total_chars)
    )