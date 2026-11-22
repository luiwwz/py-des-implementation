from des import encrypt_block

def main():
    plaintext = input("Type text: ")
    key = input("Type key: ")

    ciphertext = encrypt_block(plaintext, key)

    print(ciphertext)

if __name__ == "__main__":
    main()