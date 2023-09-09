def decompress(s: str) -> str:
    decompressed = []
    i = 0
    while i < len(s):
        if s[i].isdigit():

            num_start = i
            while i + 1 < len(s) and s[i + 1].isdigit():
                i += 1
            repetitions = int(s[num_start:i + 1])

            decompressed.append(s[i + 1] * repetitions)
            i += 1
        else:
            decompressed.append(s[i])
        i += 1
    return ''.join(decompressed)


compressed_string = input()
print(decompress(compressed_string))
