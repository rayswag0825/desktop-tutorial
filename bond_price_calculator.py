def getBondPrice(y, face, couponRate, m, ppy=1):
    # Coupon payment per period
    c = (couponRate * face) / ppy  
    # Discount rate per period
    r = y / ppy  
    # Total number of periods
    n = m * ppy  
    
    # Check if yield is zero
    if r == 0:
        pv_coupons = c * n  
        pv_face = face  
    else:
        # Present value of annuity (coupon payments)
        pv_coupons = c * (1 - (1 + r) ** -n) / r
        # Present value of face value
        pv_face = face / ((1 + r) ** n)
    
    # Total bond price
    bondPrice = pv_coupons + pv_face
    return bondPrice

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10

# Testing different payment periods
print("Bond Price (ppy=1):", getBondPrice(y, face, couponRate, m))
print("Bond Price (ppy=2):", getBondPrice(y, face, couponRate, m, ppy=2))
