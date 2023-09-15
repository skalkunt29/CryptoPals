def xor_hex_strings(hex_str1, hex_str2):
    # Convert the hexadecimal strings to bytes
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)

    # Perform the XOR operation
    xor_result = bytes(x ^ y for x, y in zip(bytes1, bytes2))

    # Convert the result back to a hexadecimal string
    result_hex = xor_result.hex()

    return result_hex



hex_str1 = "1c0111001f010100061a024b53535009181c"
hex_str2 = "686974207468652062756c6c277320657965"
result = xor_hex_strings(hex_str1, hex_str2)
print(result)
#print("746865206b696420646f6e277420706c6179")