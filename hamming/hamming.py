
def distance(strand1, strand2):
    distance = 0
    if len(strand1) != len(strand2):
        raise ValueError("Strands must be the same length")
    for x in range(0, len(strand1)):
        if strand1[x] != strand2[x]:
            distance += 1
    return distance
