print("*******Crystal Calculator*******")

crysFreq = float(input("\nEnter the printed crystal/receive frequency: "))
intFreq = float(input("\nEnter the intermediate frequency (10.7 for Regency/generic or 10.8MHz for Bearcat): "))
band = str(input("\nEnter the band of operation (VHF-Low (30-50MHz), VHF-Hi (150-175MHz), or UHF (450-470MHz), VL, VH, or U): "))

if (band == 'VL'):
    calc = (crysFreq + intFreq)
    
if (band == 'VH'):
    calc = (crysFreq -intFreq)/3
    
elif (band == 'U'):
    calc = (crysFreq - intFreq)/9


print("")
print(calc, "MHz is the fundamental frequency")