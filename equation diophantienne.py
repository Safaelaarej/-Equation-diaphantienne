def euclide_etendu(a, b):
    """Algorithme d'Euclide étendu"""
    if b == 0:
        return a, 1, 0
    else:
        pgcd, x1, y1 = euclide_etendu(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return pgcd, x, y

# Programme principal
print("=" * 50)
print("Résolution de l'équation diophantienne: a*x + b*y = c")
print("=" * 50)

a = int(input("\nEntrez la valeur de a: "))
b = int(input("Entrez la valeur de b: "))
c = int(input("Entrez la valeur de c: "))

pgcd, x0, y0 = euclide_etendu(a, b)

print(f"\nPGCD({a}, {b}) = {pgcd}")

if c % pgcd != 0:
    print("\n❌ L'équation n'a pas de solution entière.")
else:
    x = x0 * (c // pgcd)
    y = y0 * (c // pgcd)
    print(f"\n✅ Solution trouvée:")
    print(f"   x = {x}")
    print(f"   y = {y}")
    print(f"\nVérification: {a}*({x})
