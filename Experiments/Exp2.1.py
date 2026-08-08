def bit_stuffing(data):
    stuffed_data = ''
    count = 0
    for bit in data:
        stuffed_data += bit
        if bit == '1':
            count += 1
            if count == 5:
                stuffed_data += '0'  # Stuffing '0' after five 1s
                count = 0
        else:
            count = 0 # Reset counter if a '0' is encountered
    return stuffed_data

def bit_unstuffing(data):
    unstuffed_data = ''
    count = 0
    i = 0
    while i < len(data):
        bit = data[i]
        unstuffed_data += bit
        if bit == '1':
            count += 1
            if count == 5:
                # The next bit is the stuffed 0, so we skip it
                i += 1 
                count = 0
        else:
            count = 0 # Reset counter if a '0' is encountered
        i += 1
    return unstuffed_data

# Example Test
data = "11111011111"
stuffed = bit_stuffing(data)
unstuffed = bit_unstuffing(stuffed)

print(f"Original Data:  {data}")
print(f"Stuffed Data:   {stuffed}")
print(f"Unstuffed Data: {unstuffed}")

