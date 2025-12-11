# 3. Condición en un ciclo
# Crea un ciclo for que recorra los números del 1 al 10. Si encuentra un número par, imprime "Par", si es impar,
# imprime "Impar".

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for num in numero:  # for va hacer que se itere la variable numero que contiene los numeros del 1 al 10 y los guarda en num
    if (
        num % 2 == 0
    ):  # if es una condicion donde cada numeros guardado en num se dividira por 2, si el resto es cero es par y sino es impar
        print(f"{num} El número es par")
    else:
        print(f"{num} El número es impar")
