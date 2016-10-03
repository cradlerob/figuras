result = [0, 0]
adj1 = 0
adj2 = 0


def score(jug1, jug2):
    global result
    global adj1
    global adj2
    res1 = result[0]
    res2 = result[1]
    if res1 == 30 or res2 == 30:
        result = [(res1 + 10 * jug1), (res2 + 10 * jug2)]
        res1 = result[0]
        res2 = result[1]
        adj1 += jug1
        adj2 += jug2
        if res1 == 40 and res2 == 40:
            result = [('deuce'), ('deuce')]
            adj1 = 0
            adj2 = 0
        if adj1 > 0 and res1 == 'deuce':
            result = ["adv" + str(adj1), 'deuce']
        if adj2 > 0 and res1 == 'deuce':
            result = ['deuce', "adv" + str(adj2)]
        if adj1 > 0 and adj2 > 0 and res1 == 'deuce':
            result = ["adv" + str(adj1), "adv" + str(adj2)]
    else:
        result = [(res1 + 15 * jug1), (res2 + 15 * jug2)]
        adj1 += jug1
        adj2 += jug2
    print result


if __name__ == "__main__":
    import doctest
    doctest.testfile("pruebatennis.txt")
