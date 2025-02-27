def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    c = couponRate * face  

    for t, y in enumerate(yc, start=1):
        if t < m:
            bondPrice += (c / ((1 + y) ** t))
        else:
            bondPrice += ((c + face) / ((1 + y) ** t))

    return bondPrice

# Test values
yc = [0.010, 0.015, 0.020, 0.025, 0.030]
face = 2000000
couponRate = 0.04
m = 5

# Compute bond price
print("Bond Price:", getBondPrice_E(face, couponRate, m, yc))
