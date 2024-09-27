#triple pythagorean states
m, n = map(int,input("Give 2 positif integer ").split())
side1 = m**2 - n**2
side2 = 2*m*n
hypotenuse = m**2 + n**2
print(f"Pythagorean triple {side1} {side2} {hypotenuse}")