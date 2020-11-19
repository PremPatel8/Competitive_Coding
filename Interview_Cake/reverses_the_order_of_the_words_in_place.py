

message = ['c', 'a', 'k', 'e', ' ', 'p', 'o',
           'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']


def reverse_word_util(msg, lt, rt):
    msg[lt:rt] = msg[lt:rt][::-1]


def reverse_words(msg):
    left = right = 0

    while right < len(msg) and left < len(msg):
        if msg[right] != ' ' and right != len(msg)-1:
            right += 1
        else:
            reverse_word_util(msg, left, right) if right != len(
                msg)-1 else reverse_word_util(msg, left, right+1)
            right += 1
            left = right

    msg.reverse()


reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))
