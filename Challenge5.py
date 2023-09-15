def repeating_key_xor(plaintext, key):
    encrypted_bytes = bytearray()
    key_length = len(key)

    for i in range(len(plaintext)):
        encrypted_byte = plaintext[i] ^ ord(key[i % key_length])
        encrypted_bytes.append(encrypted_byte)

    return encrypted_bytes.hex()

# Input plaintext and key
plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

# Encrypt the plaintext
encrypted_text = repeating_key_xor(plaintext.encode(), key)

# Print the encrypted text in hexadecimal format
print(encrypted_text)
