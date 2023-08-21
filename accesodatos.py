from M4ActividadIndividual6 import PerfilAsesor, PerfilCliente
import csv

def cargar_asesores_desde_csv():
    asesores = []
    with open('colaboradores.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            id_usuario = row[0]
            rut = row[1]
            edad = int(row[2])
            comision = float(row[3])
            asesor = PerfilAsesor(id_usuario, None, None)
            asesor.rut = rut
            asesor.edad = edad
            asesor.comision = comision
            asesores.append(asesor)
    return asesores

asesores_cargados = cargar_asesores_desde_csv()

# En un script diferente, acceda a los diferentes datos registrados
for asesor in asesores_cargados:
    print(f"ID: {asesor.id_usuario}")
    print(f"RUT: {asesor.rut}")
    print(f"Edad: {asesor.edad}")
    print(f"Comisión: {asesor.comision}")
    print("-------------------")


def cargar_clientes_desde_csv():
    clientes = []
    with open('clientes.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera
        for row in reader:
            id_usuario = row[0]
            nombre_cliente = row[1]
            rut = row[2]
            patente = row[3]
            marca = row[4]
            modelo = row[5]
            kilometraje = int(row[6])
            fono = row[7]
            servicio = row[8]
            cliente = PerfilCliente(id_usuario, None, nombre_cliente, rut, patente, marca, modelo, kilometraje, fono, servicio)
            clientes.append(cliente)
    return clientes

# Cargar información de clientes desde el archivo CSV
clientes_cargados = cargar_clientes_desde_csv()

# Imprimir información de los clientes
for cliente in clientes_cargados:
    print(f"ID: {cliente.id_usuario}")
    print(f"Nombre: {cliente.nombre_cliente}")
    print(f"RUT: {cliente.rut}")
    print(f"Teléfono: {cliente.fono}")
    print(f"Marca: {cliente.marca}")
    print(f"Modelo: {cliente.modelo}")
    print(f"Patente: {cliente.patente}")
    print(f"Kilometraje: {cliente.kilometraje}")
    print("-------------------")