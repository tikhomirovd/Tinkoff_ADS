def count_amount_substr(s: str) -> int:
    i = 0
    j = 1
    counter = 0
    ans = 0
    while i < len(s):
        while j < len(s):
            subs = s[i:j]
            no_sub = s[:i] + s[j:]
            if subs in no_sub:
                pass
            else:
                ans = j - i
            j += 1
        i += 1
        j = i + 1
    return ans


s = input()
print(count_amount_substr(s))
