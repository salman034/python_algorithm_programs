def anagram_check(string1, string2):

    if sorted(string1) == sorted(string2):
        return "The string are anagram"
    else:
        return "The string is not anagram"


if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"
    print(anagram_check(str1, str2))