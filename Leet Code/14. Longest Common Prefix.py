def main():

    shortest = len(strs[0])
    for word in strs:
        if len(word) < shortest: 
            shortest = len(word)
    for i in range(shortest):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[0][i]:
                return strs[0][:i]

    return strs[0][:shortest]
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
        



if __name__ == "__main__":
    main()