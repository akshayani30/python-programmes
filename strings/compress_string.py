def compress_string(text):
    if not text:
        return""
    compressed=""
    count=1
    prev_char=text[0]

    for char in text[1:]:
        if char==prev_char:
            count+=1
        else:
            compressed +=prev_char+(str(count) if count>=1 else"")
            prev_char=char
            count=1
        
    compressed +=prev_char+(str(count) if count>1 else"")

    return compressed
input_string="aaabbbcca"
compressed_string=compress_string(input_string)
print(compressed_string)