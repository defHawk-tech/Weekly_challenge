import base64

# Step 1: Character Substitution
substitution_table = {
    'H': 'X', 'E': 'M', 'L': 'P', 'O': 'Q', 'W': 'Y', 'R': 'F', 'D': 'T', 
    '!': '@', ' ': '%'
}  # Example simple substitution

def substitute(text, table):
    return "".join(table.get(c, c) for c in text)

# Step 2: Bitwise Rotation
def bitwise_rotate(byte_data, shift=2):
    return bytes(((b << shift) & 0xFF) | (b >> (8 - shift)) for b in byte_data)

# Step 3: XOR Encryption
def xor_encrypt(data, key):
    return bytes(b ^ key for b in data)

# Original message
plaintext = "HELLO"

# Apply substitution
substituted_text = substitute(plaintext, substitution_table)

# Convert to bytes
byte_data = substituted_text.encode()

# Apply bitwise rotation
rotated_bytes = bitwise_rotate(byte_data)

# Apply XOR encryption
xor_bytes = xor_encrypt(rotated_bytes, key=42)

# Apply Base64 encoding
encoded_message = base64.b64encode(xor_bytes).decode()

print(f"Encoded Message: {encoded_message}")
