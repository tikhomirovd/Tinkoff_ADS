def can_read_word_in_circle(circle, word):
    n_circle = circle * (len(circle) // len(word) + 1) + circle * (len(word) // len(circle) + 1)

    if word in n_circle or word in n_circle[::-1]:
        return "YES"
    return "NO"


circle = input().strip()
word = input().strip()

print(can_read_word_in_circle(circle, word))
