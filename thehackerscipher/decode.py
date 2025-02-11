 
import base64

# Step 1: Reverse Character Substitution
def reverse_substitution(encoded_text, substitution_table):
    reversed_table = {v: k for k, v in substitution_table.items()}  # Reverse mapping
    return "".join(reversed_table.get(c, c) for c in encoded_text)

# Step 2: Reverse Bitwise Rotation
def reverse_bitwise_rotation(byte_data, shift=2):
    return bytes(((b >> shift) | (b << (8 - shift)) & 0xFF) for b in byte_data)

# Step 3: XOR Decryption
def xor_decrypt(data, key):
    return bytes(b ^ key for b in data)

# Step 4: Base64 Decoding
def base64_decode(encoded_text):
    try:
        return base64.b64decode(encoded_text)
    except Exception as e:
        print(f"Base64 decoding error: {e}")
        return None

# Known Substitution Table (for reversal)
substitution_table = {
    'H': 'X', 'E': 'M', 'L': 'P', 'O': 'Q', 'W': 'Y', 'R': 'F', 'D': 'T', 
    '!': '@', ' ': '%'
}

# Encoded message (Generated from encoding script)
encoded_message = "M5f/k7u+r5O7vuOX/5O7Kw=="

# Step 1: Reverse Base64 Encoding
decoded_bytes = base64_decode(encoded_message)

if decoded_bytes:
    # Step 2: Reverse XOR
    xor_decrypted = xor_decrypt(decoded_bytes, key=42)

    # Step 3: Reverse Bitwise Rotation
    bitwise_restored = reverse_bitwise_rotation(xor_decrypted)

    # Step 4: Reverse Character Substitution
    plaintext = reverse_substitution(bitwise_restored.decode(errors="ignore"), substitution_table)

    print(f"Decoded Message: {plaintext}")  

swatimac@Swatis-MacBook-Air keys % python3 dec
