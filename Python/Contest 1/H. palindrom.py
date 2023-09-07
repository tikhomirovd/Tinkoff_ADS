def is_palindrome(s):
    return s == s[::-1]


def can_become_palindrome(s):
    if is_palindrome(s):
        return True

    # Проверяем подстроки s, начиная с первого символа и до последнего, затем до предпоследнего и так далее
    for i in range(len(s) - 1, 2, -1):
        sub_s = s[:i]
        if s[i] != "a":
            break
        if is_palindrome(sub_s):
            return True

    return False


s = input()
# s = "acbcaa"

if can_become_palindrome(s):
    print("Yes")
else:
    print("No")
