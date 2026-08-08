def char_stuffing(data,flag ="F" , esc = "E"):
    stuffed_data = flag
    for char in data:
        if char == flag or char == esc:
            stuffed_data += esc 
        stuffed_data += char
    stuffed_data += flag
    return stuffed_data
def char_unstuffing(data, flag="F", esc = "E"):
    unstuffed_data =""
    i = 1
    while i<len(data):
        if data[i] == esc:
            i += 1
        unstuffed_data += data[i]
        i +=1
    return unstuffed_data

#Example:


data = "ABCFDEFG"
stuffed = char_stuffing(data)
unstuffed = char_unstuffing(stuffed)

print("Original data : ", data)
print("Stuffed data : ", stuffed)
print("Unstuffed data : ", unstuffed)



