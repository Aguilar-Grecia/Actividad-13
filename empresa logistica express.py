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
        if repartidor.nombre == "" or repartidor.paquetes <= 0 or repartidor.zona =="":
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

        return self.quick_sort(mayores) + [pivote] + self.quick_sort(menores)
    def ordenar_paquetes(self):
        self.repartidores= self.quick_sort(self.repartidores)
    def buscar_repartidor(self,nombre):
        for i in self.repartidores:
            if i.nombre == nombre:
                return i
        return None
    def mostrar_ranking(self):
        for i in self.repartidores:
            print(f"{i.nombre} - {i.paquetes} paquetes - zona: {i.zona}")
    def estadistica(self):
        if len(self.repartidores) == 0:
            print("No hay datos registrados no se pueden mostrar estadisticas.")
            return
        total = sum(i.paquetes for i in self.repartidores)
        promedio = total/len(self.repartidores)
        maximo_paquetes = max(i.paquetes for i in self.repartidores)
        minimo_paquetes = min(i.paquetes for i in self.repartidores)
        mayores = [i.nombre for i in self.repartidores if i.paquetes == maximo_paquetes]
        menores = [i.nombre for i in self.repartidores if i.paquetes == minimo_paquetes]
        print(f"\n---ESTADISTICA---")
        print(f"Total de paquetes: {total}")
        print(f"Promedio de paquetes: {promedio}")
        print(f"Mayor número de entregas: ")
        for i in mayores:
            print(f"{i.nombre}  ({i.paquetes})")
        print(f"Menor número de entregas: ")
        for i in menores:
            print(f"{i.nombre}  ({i.paquetes})")

empresa = Empresa()
n = int(input("Cantidad de repartidores: "))
for i in range (n):
    print(f"\nIngrese los datos de repartidores {i+1}: ")
    nombre = input("Ingrese el nombre: ")
    paquetes = input("Ingrese los paquetes: ")
    zona = input("Ingrese el zona: ")
    empresa.agregar_repartidor(Repartidor(nombre, paquetes, zona))

print("\n---LISTA ORIGINAL---")
empresa.mostrar_ranking()
empresa.ordenar_paquetes()
print("\n---RANKING---")
empresa.mostrar_ranking()
nombre_buscar = input("\nBuscar repartidor: ")
encontrado= empresa.buscar_repartidor(nombre_buscar)
if encontrado:
    print(f"{encontrado.nombre} - {encontrado.paquetes} paquetes - Zona: {encontrado.zona}")
else:
    print("Lo siento no se encontro al repartidor.")
empresa.estadistica()