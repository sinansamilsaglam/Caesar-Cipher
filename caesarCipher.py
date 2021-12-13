alphabet = "abcçdefgğhıijklmnoöprsştuüvyz "

letterIndex = dict(zip(alphabet, range(len(alphabet))))
indexLetter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, shift=3):
    cipher = ""

    for letter in message:
        number = (letterIndex[letter] + shift) % len(letterIndex)
        letter = indexLetter[number]
        cipher += letter

    return cipher


def decrypt(cipher, shift=3):
    decrypted = ""

    for letter in cipher:
        number = (letterIndex[letter] - shift) % len(letterIndex)
        letter = indexLetter[number]
        decrypted += letter

    return decrypted


def main():
    #if you want any message to encrypt run this
    #message = input("Input your message ")
    
    #if you want learn to mean of encrypted message run this
    cipher = input("Input your encrypted message: ")
    decrypted = decrypt(cipher, shift=3)

    #print('Original message: ' + message)
    print('Encrypted message: ' + cipher)
    print('Decrypted message: ' + decrypted)

main()
