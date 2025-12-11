# Ciclo anidado
# Escribe un programa que imprima una tabla de multiplicar del 1 al 3,
# usando un ciclo for dentro de otro for.


for i in range(
    1, 4
):  # se elige un rango donde se tome el 1 pero no se toma el 4 para ingresar al otro bucle y se guarda en i
    for j in range(
        3, 4
    ):  # aqui pasa lo mismo para que el numero sea solo el 3 que se guarda en j
        print(
            f"{i}*{j}"
        )  # imprimir todos los numero iterados del rango (1,4) que serian 1,2,3 * J que es 3 mostrando de esta forma una tabla de multiplicar
