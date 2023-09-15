import binascii
import base64

# Input hexadecimal string
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"  

# Convert hex string to bytes
hex_bytes = binascii.unhexlify(hex_string)

# Encode the bytes as base64
base64_encoded = base64.b64encode(hex_bytes).decode('utf-8')
print(base64_encoded)
