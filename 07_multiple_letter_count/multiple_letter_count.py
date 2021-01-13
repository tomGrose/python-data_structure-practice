def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letters = {}
    for letter in phrase:
        if letters.get(letter):
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1
    return letters