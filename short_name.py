def short_name(name):
    # Remove extra spaces and split into words
    words = name.strip().split()

    # If it's a single word like "Mehboob"
    if len(words) == 1:
        word = words[0].upper()
        # Take first 3 consonants or first 3 letters if not enough consonants
        short = ''.join([c for c in word if c not in 'AEIOU'])[:3]
        if len(short) < 3:
            short = word[:3]  # fallback to first 3 letters
        return short

    # If it's multiple words like "John Michael Doe"
    initials = ''.join(word[0].upper() for word in words)
    return initials





def short_name(name):
    words = name.strip().split()

    if len(words) == 1:
        word = words[0].upper()
        if len(word) >= 3:
            return word[0] + word[len(word)//2] + word[-1]
        else:
            return word  # fallback for short names like "Al"
    else:
        # Take first letter of first, middle, and last word
        first = words[0][0].upper()
        middle = words[len(words)//2][0].upper()
        last = words[-1][0].upper()
        return first + middle + last



print(short_name('Aslam'))