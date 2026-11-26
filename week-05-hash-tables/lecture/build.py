def hash_function(key, size):
    total = 0
    for ch in key:
        total += ord(ch)        # Unicode number of each character
    return total % size         # hash code = bucket index 0...size-1

print(hash_function("cat", 7))  # 99 + 97 + 116 = 312 -> 312 % 7 = 4


