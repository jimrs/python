x = 0

def nastav_x(hodnota):
    x = hodnota  # Přiřazení do lokální proměnné!

nastav_x(40)
print(x)

def nastav_x(hodnota):
    global x
    x = hodnota  # Přiřazení do globalni proměnné!

nastav_x(40)
print(x)