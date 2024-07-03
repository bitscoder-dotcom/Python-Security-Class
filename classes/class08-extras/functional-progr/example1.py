def main():
    soft("Do", "nOT", "ShoUT")

def soft(*phrase):

    soft_words = list()
    for word in phrase:
        soft_words.append(word.lower())
    """
        Using iteration to change the structure of a string
    """
    soft_words1 = map(str.lower, phrase)
    """
        using map to change the structure of the phrase
    """
    soft_words2 = (word.lower() for word in phrase)
    """
        List comprenhension is used here to achieve the same purpose
    """
    print(*soft_words)

if __name__ == "__main__":
    main()