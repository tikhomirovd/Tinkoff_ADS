def check_string(s: str):
    if (s[0].isalpha() and s[1].isdigit()) or (s[0].isdigit() and s[1].isalpha()):
        print("YES")
    else:
        print("NO")


s = input()
check_string(s)
