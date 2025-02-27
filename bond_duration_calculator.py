def getBondDuration(y, face, couponRate, m, ppy=1):
    c = (couponRate * face) / ppy  
    r = y / ppy  
    n = m * ppy  

    pvcf_t = sum([(t * c) / ((1 + r) ** t) for t in range(1, n + 1)])
    pvcf_t += (n * face) / ((1 + r) ** n)

    bondPrice = sum([(c) / ((1 + r) ** t) for t in range(1, n + 1)])
    bondPrice += face / ((1 + r) ** n)

    bondDuration = pvcf_t / bondPrice
    return bondDuration

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10

print("Bond Duration (ppy=1):", getBondDuration(y, face, couponRate, m))
print("Bond Duration (ppy=2):", getBondDuration(y, face, couponRate, m, ppy=2))
