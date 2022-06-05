def reverse(num):
    return num[::-1]

def palindrome(lower, upper):
    palindrome_list = []
    for i in range(lower, upper):
        if str(i) == reverse(str(i)):
            palindrome_list.append(i)
    prime_list = prime(palindrome_list)
    return prime_list


def prime(palindrome_list):
    dummy_list = []
    for number in palindrome_list:
        for j in range(2, number):
            if number % j == 0:
                break
        else:
            dummy_list.append(number)
    return dummy_list


if __name__ == "__main__":
    final_list = palindrome(0, 1000)
    print(final_list)