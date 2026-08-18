def calculate_parity_bits(data_bits):
    """Return a Hamming code array for the given data bits string."""
    # Length of the data bits
    m = len(data_bits)
    r = 0

    # Find the number of redundant (parity) bits needed
    while (2 ** r) < (m + r + 1):
        r += 1

    n = m + r                          # Total length of Hamming code
    hamming_code = ['x'] * (n + 1)      # Indexing from 1, dummy 0‑th element

    # Place data bits in the non‑power‑of‑two positions
    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:         # i is NOT a power of two
            hamming_code[i] = int(data_bits[j])
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for k in range(1, n + 1):
            if (k & parity_pos) and k != parity_pos:
                if hamming_code[k] != 'x':
                    parity ^= hamming_code[k]
        hamming_code[parity_pos] = parity

    return hamming_code[1:]   # drop dummy index


def introduce_error(code, position):
    """Flip the bit at `position` (1‑based) to simulate an error."""
    if 1 <= position <= len(code):
        code[position - 1] ^= 1
    return code


def detect_error(received_code):
    """Return the 1‑based index of a single-bit error, or 0 if none detected."""
    n = len(received_code)
    r = 0
    while (2 ** r) < (n + 1):
        r += 1

    error_position = 0
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for k in range(1, n + 1):
            if k & parity_pos:
                parity ^= received_code[k - 1]
        if parity != 0:
            error_position += parity_pos

    return error_position


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    # Input binary data (e.g., '1011')
    data = input("Enter data bits (e.g., 1011): ")

    # Generate Hamming code
    hamming = calculate_parity_bits(data)
    print("Generated Hamming Code:", ''.join(map(str, hamming)))

    # Optionally introduce an error
    try:
        error_pos = int(input("Enter position to introduce error (0 for none): "))
    except ValueError:
        error_pos = 0

    if error_pos != 0:
        hamming = introduce_error(hamming, error_pos)
        print("Hamming Code with error introduced:", ''.join(map(str, hamming)))

    # Detect error
    detected_pos = detect_error(hamming)
    if detected_pos == 0:
        print("No error detected.")
    else:
        print(f"Error detected at position: {detected_pos}")
