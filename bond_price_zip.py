def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0
    c = couponRate * face  

    for t, y in zip(times, yc):
        if t < max(times):
            bondPrice += (c / ((1 + y) ** t))
        else:
            bondPrice += ((c + face) / ((1 + y) ** t))

    return bondPrice

# Test values
yc = [0.010, 0.015, 0.020, 0.025, 0.030]
times = [1, 1.5, 3, 4, 7]
face = 2000000
couponRate = 0.04

# Compute bond price
print("Bond Price:", getBondPrice_Z(face, couponRate, times, yc))
