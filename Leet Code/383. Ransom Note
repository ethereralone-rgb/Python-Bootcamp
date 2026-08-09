def main():
    counts = {}
    ransomNote = "aabbc"
    magazine = "aabbbbcccdd"
    for char in magazine:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char in ransomNote:
        if char  not in counts:
            return False
        elif counts[char] == 0:
            return False
        else:
            counts[char] -= 1
    return True 

if __name__ == "__main__":
    print(main())