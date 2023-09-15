def single_byte_xor(hex_string, char):
    byte_string = bytes.fromhex(hex_string)
    result = bytes(b ^ char for b in byte_string)
    return result.decode('utf-8', errors='ignore')

def score_text(text):
    english_letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    return sum(1 for char in text if char in english_letters)

def find_xor_key(hex_string):
    best_key = 0
    max_score = 0
    decrypted_text = ""

    for possible_key in range(256): 
        decrypted = single_byte_xor(hex_string, possible_key)
        score = score_text(decrypted)

        if score > max_score:
            max_score = score
            best_key = possible_key
            decrypted_text = decrypted

    return best_key, decrypted_text


hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

key, decrypted_message = find_xor_key(hex_string)

print("Key:", key)
print("Decrypted Message:", decrypted_message)
