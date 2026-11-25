from tables import IP, FP, E, P, PC1, PC2, SHIFTS, S_BOXES

def text_to_bits(text: str):
    raw_bytes = text.encode('ascii') # 'A' -> 65
    return ''.join(format(byte, '08b') for byte in raw_bytes) # '65' -> 01000001

def bits_to_text(bits:str):
    chars = [chr(int(bits[i:i + 8], 2)) for i in range(0, 64, 8)]
    return ''.join(chars)

def permute(block: str, table: list[int]):
    return ''.join(block[i - 1] for i in table)

def format_bits(bits: str):
    return ' '.join(bits[i:i + 8] for i in range(0, len(bits), 8))

def left_shift(bits: str, shifts: int):
    return bits[shifts:] + bits[:shifts]

def get_round_keys(key_64: str) -> list[str]:
    key_56 = permute(key_64, PC1)

    c = key_56[:28]
    d = key_56[28:]

    round_keys = []

    for shift in SHIFTS:
        c = left_shift(c, shift)
        d = left_shift(d, shift)
        round_key_48 = permute(c + d, PC2)
        round_keys.append(round_key_48)

    return round_keys

def xor(a: str, b: str):
    return ''.join('1' if bit_a != bit_b else '0' for bit_a, bit_b in zip(a, b))

def sbox_substitution(bits_48: str):
    result = []

    for i in range(8):
        chunk = bits_48[i * 6: (i + 1) * 6]
        row = int(chunk[0] + chunk[5], 2)
        col = int(chunk[1:5], 2)

        value = S_BOXES[i][row][col]
        result.append(format(value, '04b'))

    return ''.join(result)

def feistel(right_32: str, round_key: str):
    extended = permute(right_32, E)
    xored = xor(extended, round_key)
    substituted = sbox_substitution(xored)
    return permute(substituted, P)

def encrypt_block(plaintext: str, key: str):
    block_64 = text_to_bits(plaintext)
    key_64 = text_to_bits(key)

    round_keys = get_round_keys(key_64)

    permuted = permute(block_64, IP)
    left, right = permuted[:32], permuted[32:]

    for i in range(16):
        new_right = xor(left, feistel(right, round_keys[i]))
        left, right = right, new_right

    combined = right + left
    return permute(combined, FP)

def decrypt_block(block_64: str, key: str):
    key_64 = text_to_bits(key)

    round_keys = get_round_keys(key_64)
    round_keys = round_keys[::-1]

    permuted = permute(block_64, IP)
    left, right = permuted[:32], permuted[32:]

    for i in range(16):
        new_right = xor(left, feistel(right, round_keys[i]))
        left, right = right, new_right

    combined = right + left
    return permute(combined, FP)