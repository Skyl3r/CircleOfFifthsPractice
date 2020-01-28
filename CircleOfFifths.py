import sys
import random

circle_of_fifths = [
    'F',
    'C',
    'G',
    'D',
    'A',
    'E',
    'B',
    'Gb',
    'Db',
    'Ab',
    'Eb',
    'Bb'
]

flat_order = [
    'B',
    'E',
    'A',
    'D',
    'G',
    'C',
    'F'
]

intervals = [
    ['Minor Third', 9],
    ['Major Third', 4],
    ['Fifth', 1],
    ['Major Seventh', 5],
    ['Minor Seventh', 10]
]

print("Welcome to Circle of Fifths Practice")
print("")
print("Choose one of the following:")
print("1. Key Signature Identification")
print("2. Interval Identification (Triads and Sevenths)")

test_mode = int(sys.stdin.readline())
mode_choices = range(1, 3)

if test_mode not in mode_choices:
    print("Not a valid choice!")
    exit(0)


# Key signature test
if test_mode == 1:
    key = random.randint(0, len(circle_of_fifths) - 1)
    correct_answer = []

    print("What are the sharps or flats in " + circle_of_fifths[key] + "?")
    print("List them like this:")
    print("Bb, Eb, Ab  or  F#, C#, G#")
    print("")

    # Construct correct answers:
    if 1 <= key <= 6:
        for i in range(key):
            if i > 0:
                correct_answer.append(circle_of_fifths[i-1] + "#")
    elif key > 6:
        for i in range(len(circle_of_fifths) - (key - 1)):
            correct_answer.append(flat_order[i % 6] + "b")
    elif key == 0:
        correct_answer.append(flat_order[0] + "b")

    user_answer_raw = str(sys.stdin.readline())
    user_answer_raw = user_answer_raw.replace(' ', '').replace('\n', '')
    user_answer = user_answer_raw.split(',')

    wrong = False

    if len(user_answer) == len(correct_answer):
        for i in user_answer:
            if i not in correct_answer:
                wrong = True
    else:
        wrong = True

    if wrong:
        print("Wrong answer!")
        print("The correct answer is: " + ", ".join(correct_answer))
    else:
        print("Correct!")

# Interval test
if test_mode == 2:
    root = random.randint(0, len(circle_of_fifths) - 1)
    interval = random.randint(0, len(intervals) - 1)

    correct_answer = circle_of_fifths[(root + intervals[interval][1]) % len(circle_of_fifths)]

    print("What is the " + intervals[interval][0] + " of " + circle_of_fifths[root] + "?")

    user_answer = str(sys.stdin.readline())
    user_answer = user_answer.replace('\n', '')

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Wrong! The " + intervals[interval][0] + " of " + circle_of_fifths[root] + " is " + correct_answer)