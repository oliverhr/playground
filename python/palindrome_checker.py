'''
In this case, N is the size of the string passed to this function.
The guts of the algorithm takes place within the while loop.
Now, this loop is somewhat interesting because it only runs until
it reaches the midpoint of the string, that would mean that the
loop runs N / 2 steps.

However, Big O ignores constants, so because of this, we drop the
division by 2, and our algorithm is O(N).
'''


def is_palindrome(word: str) -> bool:
    half = len(word) / 2
    left_index: int = 0
    right_index: int = len(word) - 1

    while left_index < half:
        if word[left_index] != word[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


def main() -> None:
    words: list[str]= [
            'kayak',
            'oliver',
            'deified',
            'peep',
            'racecar',
            ]
    for word in words:
        print(f'The word "{word}" is palindrome?: ', is_palindrome(word))


if __name__ == '__main__':
    main()

