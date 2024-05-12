'''
'''

def pick(resumes: list[str]) -> str:
    from_top: bool = True

    steps = 0
    while (size := len(resumes)) > 1:
        if from_top:
            resumes = resumes[:size//2]
            from_top = False
        else:
            resumes = resumes[(size // 2):]
            from_top = True
    return resumes[0]


def main() -> None:
    resumes: list[str] = [
        'uno',
        'dos',
        'tres',
        'cuatro',
        'cinco',
        'seis',
        'siete',
    ]
    print(f'Picked: {pick(resumes)}')


if __name__ == '__main__':
    main()

