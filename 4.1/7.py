def can_eat(horse, figure):
    s1 = (abs(horse[0] - figure[0]) == 2 and abs(horse[1] - figure[1]) == 1)
    s2 = (abs(horse[0] - figure[0]) == 1 and abs(horse[1] - figure[1]) == 2)
    if s1 or s2:
        return True
    return False

