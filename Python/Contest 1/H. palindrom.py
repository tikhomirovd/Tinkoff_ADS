def is_palindrome(s):
    return s == s[::-1]


def can_become_palindrome(s):
    if is_palindrome(s):
        return True

    # Проверяем подстроки s, начиная с первого символа и до последнего, затем до предпоследнего и так далее
    for i in range(len(s), len(s) - 1):
        if is_palindrome(s[i:]):
            return True

    return False


s = input()

if can_become_palindrome(s):
    print("Yes")
else:
    print("No")
