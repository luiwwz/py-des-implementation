from des import encrypt_block, format_bits, decrypt_block, bits_to_text

def main():
    plaintext = input("Type text: ")
    key = input("Type key: ")

    ciphertext = encrypt_block(plaintext, key)

    print(format_bits(ciphertext))

    print(bits_to_text(decrypt_block(ciphertext, key)))

if __name__ == "__main__":
    main()