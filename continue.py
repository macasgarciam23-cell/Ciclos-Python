# 6. Uso de continue
# Recorre una lista de nombres. Si el nombre es "Juan", omítelo usando continue. Imprime todos los demás.
# Recuerda aplicar snake_case para las variables y comentar cada ejercicio explicando qué hace el
# ciclo y qué controla su finalización.


nombres = ["Jose", "Juan", "Maria", "Alejandra", "Marisol"]

for nombre in nombres:
    if (
        nombre == "Juan"
    ):  # si la variable iterable "nombre" es igual a Juan, comtinua (pasalo de largo)e impreme los demas nombres
        continue
    print(nombre)
