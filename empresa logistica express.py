class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona
class Empresa:
    def __init__(self):
        self.repartidores = []
    def agregar_repartidor(self, repartidor):
        for i in self.repartidores:
            if i.nombre == repartidor.nombre:
                print(f"El nombre del repartidor es '{repartidor.nombre}' ya existe")
                return False
        if repartidor.nombre == ¨   or repartidor.paquetes <= 0 or repartior.zona =="":
            print("El nombre del repartidor es invalido. No es posible agregar.")
            return False
        self.repartidores.append(repartidor)
        return True
    def quick_sort(self,lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        mayores =[x for x in lista[1:] if x.paquetes > pivote.paquetes]
        iguales = [x for x in lista if x.paquetes == pivote.paquetes]
        menores = [x for x in lista[1:] if x.paquetes  <  pivote.paquetes]

        return quick_sort(menores) + iguales + quick_sort(mayores)
