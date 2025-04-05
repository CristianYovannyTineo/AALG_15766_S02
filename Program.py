#Supóngase que en una reciente elección hubo cuatro candidatos, con identificadores 1, 2, 3, 4. Usted habrá de encontrar mediante un programa, el número de votos correspondiente a cada candidato y el porcentaje que obtuvo respecto al total de los votantes. El usuario ingresara los votos de manera desorganizada, tal y como se obtuvieron en la elección, el final de datos está representado por un cero.
#Observe, como ejemplo, la siguiente lista.: 1 3 1 4 2 2 1 3 1 1 1 3 4 1 2 4 4 0

votos1 = 0
votos2 = 0
votos3 = 0
votos4 = 0
total = 0
voto = int(input("Ingresar voto (0 = Finalizar): "))
while voto != 0:
    if voto == 1:
        votos1 += 1
        total += 1
    elif voto == 2:
        votos2 += 1
        total += 1
    elif voto == 3:
        votos3 += 1
        total += 1
    elif voto == 4:
        votos4 += 1
        total += 1
    else:
        print("Vuelva a intentar.")
    
    voto = int(input("Ingrese voto (0 = Finalizar): "))
if total > 0:
    p1 = votos1 * 100 / total
    p2 = votos2 * 100 / total
    p3 = votos3 * 100 / total
    p4 = votos4 * 100 / total
else:
    p1 = p2 = p3 = p4 = 0
print(f"Candidato 1: {votos1} votos ({p1:.2f}%)")
print(f"Candidato 2: {votos2} votos ({p2:.2f}%)")
print(f"Candidato 3: {votos3} votos ({p3:.2f}%)")
print(f"Candidato 4: {votos4} votos ({p4:.2f}%)")
