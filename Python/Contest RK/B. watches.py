def watches(n: int) -> str:
    hours = n // (60 * 60) % 24
    minutes = (n - hours * 60 * 60) // 60 % 60
    seconds = (n - minutes * 60 - hours * 60 * 24) % 60

    minutes = "0" + str(minutes) if len(str(minutes)) == 1 else minutes
    seconds = "0" + str(seconds) if len(str(seconds)) == 1 else seconds
    return f"{hours}:{minutes}:{seconds}"


n = int(input())

print(watches(n))