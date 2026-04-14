
def orden_copilacion(dependencias: list):
    if not dependencias:
        return []
    conteo = {}
    resultado = []
    for dep in dependencias:
        if dep[0] not in conteo:
            conteo[dep[0]] = 0
        if dep[1] not in conteo:
            conteo[dep[1]] = 1
        else:
            conteo[dep[1]] += 1
    for clave, valor in conteo.items():
        if valor == 0:
            resultado.append(clave)
    dependencias = list(filter(lambda dep: conteo[dep[0]], dependencias))
    if not dependencias:
        for clave, valor in conteo.items():
            if valor:
                resultado.append(clave)
    return resultado + orden_copilacion(dependencias)

print(orden_copilacion([(1,3), (1,4), (2,4), (2,5), (3,6), (4,6), (5,6)]))
print(orden_copilacion([(4,6), (5,6), (1,3), (1,4), (2,4), (2,5), (3,6), (5,7)]))
print(orden_copilacion([('A','B'), ('A','F'), ('F','D'), ('D','B'), ('X','D'), ('C','B'), ('C','D')]))
print(orden_copilacion([('A','F'), ('F','D'), ('D','B'), ('C','B'), ('C','D'), ('A','B'), ('X','D')]))
