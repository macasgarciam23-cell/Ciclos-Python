1. Diferencia principal entre for y while
for:
•	El ciclo for es ideal cuando sabes cuántas veces quieres que se ejecute el ciclo.
•	Se usa típicamente cuando se tiene una secuencia o un rango predefinido de elementos (por ejemplo, una lista, un rango de números, un conjunto de objetos, etc.).
•	El ciclo for itera automáticamente sobre cada elemento de la secuencia, sin necesidad de manejar la condición de terminación explícitamente.
Ejemplo: Recorriendo una lista de números.
for i in range(1, 6):
    print(i)
Salida:
1
2
3
4
5
while:
•	El ciclo while es más flexible y se usa cuando no sabes cuántas veces necesitarás que el ciclo se repita, pero sí sabes qué condición debe cumplirse para seguir ejecutándose.
•	El ciclo while sigue ejecutándose mientras la condición sea verdadera, y la condición es evaluada antes de cada iteración.
Ejemplo: Ejecutar un ciclo mientras una variable sea menor que 10.
i = 1
while i < 6:
    print(i)
    i += 1
Salida:
1
2
3
4
5
Resumen de la diferencia:
•	for es más adecuado cuando sabes el número de iteraciones (por ejemplo, iterar sobre una lista o un rango).
•	while es útil cuando no sabes cuántas veces debe repetirse el ciclo, pero sí tienes una condición para continuar ejecutando el ciclo.
2. ¿Fue útil el uso de break y continue? ¿Por qué?
break:
•	El break se usa para salir de un ciclo antes de que termine de manera natural, cuando se cumple una condición específica.
•	Es útil cuando necesitas terminar un ciclo de forma anticipada, por ejemplo, si estás buscando un valor específico en una lista y, una vez que lo encuentras, ya no necesitas seguir buscando.
Ejemplo: Buscar un número específico en una lista y detenerse tan pronto como lo encuentres.
numeros = [1, 3, 5, 7, 9, 10]
for num in numeros:
    if num == 7:
        print("Encontrado el número 7")
        break  # Sale del ciclo cuando encuentra el 7
Salida:
Encontrado el número 7
continue:
•	El continue se usa para saltarse el resto del código en la iteración actual y pasar a la siguiente iteración del ciclo.
•	Es útil cuando deseas omitir un conjunto de operaciones en ciertas iteraciones sin detener completamente el ciclo.
Ejemplo: Imprimir solo los números impares de una lista.
numeros = [1, 2, 3, 4, 5, 6]
for num in numeros:
    if num % 2 == 0:  # Si el número es par
        continue  # Saltar al siguiente número
    print(num)
Salida:
1
3
5
¿Por qué son útiles?:
•	break es útil cuando necesitas detener un ciclo cuando se cumple una condición específica, ahorrando recursos y evitando iteraciones innecesarias.
•	continue es útil cuando necesitas omitir algunas iteraciones en un ciclo sin interrumpir todo el ciclo. Esto es especialmente útil cuando estás trabajando con condiciones dentro del ciclo que no necesitan ser evaluadas completamente.
Resumen:
•	for se usa cuando conoces el número de iteraciones o cuando trabajas con secuencias.
•	while es útil cuando no sabes cuántas iteraciones serán necesarias, pero tienes una condición para seguir ejecutando el ciclo.
•	break es útil cuando necesitas salir de un ciclo de manera anticipada.
•	continue es útil cuando necesitas saltarte ciertas iteraciones de un ciclo sin detenerlo por completo.
Ambos, break y continue, son herramientas poderosas que nos permiten tener un mayor control sobre el flujo del ciclo, haciéndolo más flexible y eficiente según las condiciones que queramos manejar.

