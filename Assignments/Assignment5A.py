def rearrange(sentence):
    wordBankS = []
    wordBankM = []
    wordBankL = []
    words = sentence.split(" ")
    for word in words:
        if len(word) <= 3:
            wordBankS.append(word)
        elif len(word) <= 6:
            wordBankM.append(word)
        else:
            wordBankL.append(word)
    all_words = wordBankS + wordBankM + wordBankL
    return " ".join(all_words)
    



def main():
    sentence = input("Enter a sentence: ")
    sentence = rearrange(sentence)
    print(f"Rearranged sentence: {sentence}")

if __name__ == "__main__":
    main()