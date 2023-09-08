def can_become_palindrome(s):
    left, right = 0, len(s) - 1

    while left <= right:
        if s[left] == 'a' and s[right] != 'a':
            return False
        if s[right] == 'a' and s[left] != 'a':
            right -= 1
            continue
        if s[left] == 'a' and s[right] == 'a':
            left += 1
            right -= 1
            continue
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


s = input()
if can_become_palindrome(s):
    print("Yes")
else:
    print("No")
