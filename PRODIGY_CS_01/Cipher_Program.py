def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = (ord(char.lower()) - ord('a') + shift) % 26
            encrypted_char = chr(ord('a') + shift_amount) if char.islower() else chr(ord('A') + shift_amount)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = (ord(char.lower()) - ord('a') - shift) % 26
            decrypted_char = chr(ord('a') + shift_amount) if char.islower() else chr(ord('A') + shift_amount)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
        if choice == 'q':
            break
        elif choice == 'e':
            plaintext = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            encrypted_text = caesar_cipher_encrypt(plaintext, shift)
            print(f"Encrypted text: {encrypted_text}")
        elif choice == 'd':
            ciphertext = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
            print(f"Decrypted text: {decrypted_text}")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
