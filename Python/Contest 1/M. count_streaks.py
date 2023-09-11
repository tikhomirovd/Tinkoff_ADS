def count_streaks(n, sequence):
    streaks = []
    current_streak = 0

    for i in range(n):
        if sequence[i] == 1:
            if current_streak != 0:
                streaks.append(current_streak)
            current_streak = 1
        else:
            current_streak += 1

    if current_streak != 0:
        streaks.append(current_streak)

    return len(streaks), streaks


n = int(input())
sequence = list(map(int, input().split()))

num_streaks, streak_lengths = count_streaks(n, sequence)

print(num_streaks)
print(' '.join(map(str, streak_lengths)))
