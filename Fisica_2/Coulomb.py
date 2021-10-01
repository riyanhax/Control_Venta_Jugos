def coulomb(q1, q2, r):
    k = 8.98*10**(9)

    F = ((k * q1 * q2) / r**(2))

    return F

def campo_electrico(q, r):
    k = 8.98*10**(9)

    F = ((k * q) / r**(2))

    return F
