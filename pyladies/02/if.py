strana = float(input('Mrdko zadej cislo: '))
positive = strana > 0

if positive:
    print("Obvod ctverce se stranou", strana, "cm je", 4 * strana, "cm")
    print("Obsah ctverce se stranou", strana, "cm je", strana**2, "cm2")

else:
    print("Strana musi byt kladna!")

print("A ted pakuj do pici nez te odpakuju sam mrdko")