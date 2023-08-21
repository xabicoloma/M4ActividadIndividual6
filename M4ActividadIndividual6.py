import random
import csv


dataclientestaller = {
    'clte1':{'rut':'17389564-9', 'patente':'BH1834', 'marca': 'Toyota', 'modelo':'Corolla', 'kilometraje':350000, 'fono': '+56987654321',},
    'clte2':{'rut':'20675156-0', 'patente':'CD5678', 'marca': 'Chevrolet', 'modelo':'Spark', 'kilometraje':180000, 'fono': '+56912345678',},
    'clte3':{'rut':'18362490-7', 'patente':'GHLT56', 'marca': 'Hyundai', 'modelo':'Tucson', 'kilometraje':70000, 'fono': '+56987654321',},
    'clte4':{'rut':'15743953-1', 'patente':'IJ7890', 'marca': 'Kia', 'modelo':'Sportage', 'kilometraje':240000, 'fono': '+56923456789',},
    'clte5':{'rut':'21908614-5', 'patente':'KLRT34', 'marca': 'Nissan', 'modelo':'Versa', 'kilometraje':25000, 'fono': '+56987654321',},
    'clte6':{'rut':'16477298-3', 'patente':'MNPG78', 'marca': 'Volkswagen', 'modelo':'Golf', 'kilometraje':60000, 'fono': '+56934567890',},
    'clte7':{'rut':'19325876-2', 'patente':'OPGC12', 'marca': 'Peugeot', 'modelo':'308', 'kilometraje':55000,'fono': '+56967890123',}
}

databodega = {
    'W610/80': {'sku': 'W61080', 'tipo': 'filtro', 'valor_neto': 8500, 'stock': 60, 'proveedor': 'Mann'},
    'W67/81': {'sku': 'W6781', 'tipo': 'filtro', 'valor_neto': 7500, 'stock': 40, 'proveedor': 'Mann'},
    'W818/8': {'sku': 'W8188', 'tipo': 'filtro', 'valor_neto': 9200, 'stock': 55, 'proveedor': 'Mann'},
    'W719/2': {'sku': 'W7192', 'tipo': 'filtro', 'valor_neto': 6900, 'stock': 30, 'proveedor': 'Mann'},
    'C2513': {'sku': 'C2513', 'tipo': 'filtro', 'valor_neto': 8000, 'stock': 50, 'proveedor': 'Mann'},
    'C2214': {'sku': 'C2214', 'tipo': 'filtro', 'valor_neto': 7800, 'stock': 35, 'proveedor': 'Mann'},
    'C28035': {'sku': 'C28035', 'tipo': 'filtro', 'valor_neto': 9100, 'stock': 45, 'proveedor': 'Mann'},
    'C2631': {'sku': 'C2631', 'tipo': 'filtro', 'valor_neto': 7200, 'stock': 25, 'proveedor': 'Mann'},
    'C2340': {'sku': 'C2340', 'tipo': 'filtro', 'valor_neto': 8800, 'stock': 52, 'proveedor': 'Mann'},
    'CU1919': {'sku': 'cu1919', 'tipo': 'filtro', 'valor_neto': 9000, 'stock': 58, 'proveedor': 'Mann'},
    'CU2336/2': {'sku': 'CU2336/2', 'tipo': 'filtro', 'valor_neto': 7300, 'stock': 28, 'proveedor': 'Mann'},
    'CU22011': {'sku': 'CU22011', 'tipo': 'filtro', 'valor_neto': 8400, 'stock': 42, 'proveedor': 'Mann'},
    '10w40': {'sku': '10w40', 'tipo': 'aceite', 'valor_neto': 7100, 'stock': 200, 'proveedor': 'Mann'},
    '5w30': {'sku': '5w30', 'tipo': 'aceite', 'valor_neto': 8300, 'stock': 250, 'proveedor': 'Mann'},
    '20w50': {'sku': '20w50', 'tipo': 'aceite', 'valor_neto': 7600, 'stock': 150, 'proveedor': 'Mann'},
    'H4': {'sku': 'h4', 'tipo': 'ampolleta', 'valor_neto': 7700, 'stock': 37, 'proveedor': 'Bosch'},
    'H1': {'sku': 'h1', 'tipo': 'ampolleta', 'valor_neto': 7000, 'stock': 32, 'proveedor': 'Bosch'},
    'H16': {'sku': 'h16', 'tipo': 'ampolleta', 'valor_neto': 8600, 'stock': 48, 'proveedor': 'Mann'},
    'H15': {'sku': 'h15', 'tipo': 'ampolleta', 'valor_neto': 7400, 'stock': 27, 'proveedor': 'Mann'}
}
reservas=[]

class Usuario:
    def __init__(self, id_usuario, password):
        self.id_usuario = id_usuario
        self.__password = password

    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password

class PerfilTaller(Usuario):
    def __init__(self, id_usuario, password, clave_autorizacion):
        super().__init__(id_usuario, password)
        self.clave_autorizacion = clave_autorizacion
    
    def eliminar_usuario(self, instanciaCuenta):
        try:
            if isinstance(instanciaCuenta, PerfilAsesor) or isinstance(instanciaCuenta, PerfilCliente):
                del instanciaCuenta
                print("Cuenta eliminada")
            else:
                raise TypeError("No se puede eliminar este tipo de cuenta.")
        except TypeError as e:
            print(f"Error: {e}")
        finally:
            print("Finalizando manejo de eliminar_usuario.")
    
    def modificar_usuario():
        cliente = input('Ingrese cliente a modificar: ')
        if cliente in dataclientestaller:
            nombre_usuario = input("Ingrese nombre de usuario: ")
            antiguedad = input("Ingrese antigüedad del cliente en años: ")
            fecha_de_incorporacion = input("Ingrese fecha de primer ingreso al taller (ejemplo: día/mes/año): ")
            id_unico = 'id_' + str(random.randint(1, 9999))

            dataclientestaller[cliente]['nombre_usuario']= nombre_usuario
            dataclientestaller[cliente]['antiguedad']= antiguedad
            dataclientestaller[cliente]['fecha_de_incorporacion']= fecha_de_incorporacion
            dataclientestaller[cliente]['id_unico']= id_unico
        else:
            print("Usuario no valido, favor volver a intentar")
            PerfilTaller.modificar_usuario()
    
    def ingresar_productos():
        print('productos ingresados')

class PerfilAsesor(Usuario):
    def __init__(self, id_usuario, password, comision):
        super().__init__(id_usuario, password)
        self.comision = comision
    
    def consultar_stock(self):
        try:
            productos = ["Producto1", "Producto2", "Producto3"]
            producto_consultado = productos[10]  
            print(f"Stock del producto consultado: {producto_consultado}")
        except IndexError:
            print("Error: Se intentó acceder a un índice inválido en la lista de productos.")
        finally:
            print("Finalizando manejo de consultar_stock.")

    def eliminar_reserva():
        print('Reserva Eliminada')
    
    def generar_ot():
        print('OT Generada')

    def generar_boleta():
        print('Boleta')
    
    def guardar_en_csv(self):
        with open('colaboradores.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.id_usuario, self.rut, self.edad,self.comision])

    def cargar_desde_csv(self, id_usuario):
        with open('colaboradores.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                if row[0] == id_usuario:
                    self.rut = row[1]
                    self.edad = row[2]
                    self.comision = row[3]
                    break


class PerfilCliente(Usuario):
    def __init__(self, id_usuario, password, nombre_cliente, rut, patente, marca, modelo, kilometraje, fono, servicio):
        super().__init__(id_usuario, password)
        self.nombre_cliente = nombre_cliente
        self.rut = rut
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje
        self.fono = fono
        self.servicio = servicio

    def generar_reserva(self):
        try:
            cliente = input('Ingrese su nombre de cliente: ')
            if cliente in dataclientestaller:
                servicio = input('Ingrese Servicio Solicitado: ')
                fecha = input('Ingrese Fecha para realizar Servicio: ')
                horario = input('Ingrese Horario para realizar Servicio: ')
                reserva = {
                    'cliente' : cliente,
                    'servicio': servicio,
                    'fecha': fecha,
                    'hora': horario
                    }
                reservas.append(reserva)
                print('Rerserva registrada')
                print(reservas)
            else:
                print("Cliente no valido, favor volver a intentar")
                PerfilCliente.generar_reserva()
        except KeyError:
            print("Error: Clave no encontrada en el diccionario.")
        finally:
            print("Finalizando manejo de generar_reserva.")
        
    def imprimir_ot():
        print('Orden De trabajo')
    
    def imprimir_boleta():
        print('Boleta')
    
    def obtener_descuento(self):
        print(f"Información del cliente:\nID de usuario: {self.id_usuario}\nNombre: {self.nombre_cliente}\nRUT: {self.rut}")
        return 0
    
    def guardar_en_csv(self):
        with open('clientes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.id_usuario, self.nombre_cliente, self.rut, self.patente, self.marca, self.modelo, self.kilometraje, self.fono, self.servicio])

    def cargar_desde_csv(self, id_usuario):
        with open('clientes.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row[0] == id_usuario:
                    self.nombre_cliente = row[1]
                    self.rut = row[2]
                    self.patente = row[3]
                    self.marca = row[4]
                    self.modelo = row[5]
                    self.kilometraje = int(row[6])
                    self.fono = row[7]
                    self.servicio = row[8]
                    break

class Reserva:
    def __init__(self, id_reserva, id_usuario, repuestos_reservados=None):
        self.id_reserva = id_reserva
        self.id_usuario = id_usuario
        self.repuestos_reservados = repuestos_reservados if repuestos_reservados is not None else []

    def agregar_repuesto(self, repuesto):
        self.repuestos_reservados.append(repuesto)
        print("Repuesto agregado a la reserva.")

    def eliminar_repuesto(self, repuesto):
        if repuesto in self.repuestos_reservados:
            self.repuestos_reservados.remove(repuesto)
            print("Repuesto eliminado de la reserva.")
        else:
            print("El repuesto no se encuentra en la reserva.")

    def cambiar_id_reserva(self, nuevo_id):
        if isinstance(nuevo_id, int):
            self.id_reserva = nuevo_id
            print("ID de reserva actualizado.")
        else:
            print("El nuevo ID debe ser un número.")

    def cambiar_usuario(self, nuevo_usuario):
        if isinstance(nuevo_usuario, str):
            self.id_usuario = nuevo_usuario
            print("Usuario de reserva actualizado.")
        else:
            print("El nuevo usuario debe ser un string.")

    def agregar_elemento(self, elemento):
        if isinstance(elemento, int):
            self.cambiar_id_reserva(elemento)
        elif isinstance(elemento, str):
            self.cambiar_usuario(elemento)
        else:
            print("Tipo de elemento no válido.")
    
    def calcular_valor_total(self):
        valor_total = 0
        for repuesto in self.repuestos_reservados:
            valor_total += repuesto.valor_neto
        return valor_total

class Repuestos:
    def __init__(self, sku, tipo, stock, valor_neto,proveedor, costo):
        self.sku = sku
        self.tipo = tipo
        self.stock = stock
        self.valor_neto = valor_neto
        self.__proveedor = proveedor
        self.__costo = costo

class Bodega:
    def __init__(self, stock):
        self.stock = stock

class Proveedor:
    def __init__(self,id_proveedor,rut,razon_social):
        self.id_proveedor = id_proveedor
        self.rut = rut
        self.razon_social = razon_social

class Orden_de_Trabajo:
    def __init__(self,id_ot,servicio,id_mecanico):
        self.id_ot = id_ot
        self.servicio = servicio
        self.id_mecanico = id_mecanico

class Boleta:
    def __init__(self,numero_documento,valor_neto, iva, valor_total):
        self.numero_documento = numero_documento
        self.valor_neto = valor_neto
        self.iva = iva
        self.valor_total = valor_total

class PerfilClienteEspecial(PerfilCliente):
    def obtener_descuento(self):
        try:
            print(f"Información del cliente especial:\nID de usuario: {self.id_usuario}\nNombre: {self.nombre_cliente}\nRUT: {self.rut}")
            return 10 
        except KeyError:
            print("Error: Clave no encontrada en el diccionario.")
            return 10
        finally:
            print("Finalizando manejo de obtener_descuento.")




asesor1 = PerfilAsesor('asesor1', 'asesorpass', 5)
asesor1.rut = '26171951-2'
asesor1.edad = 30
asesor1.comision = .1

asesor2 = PerfilAsesor('asesor2', 'asesorpass2', 7)
asesor2.rut = '30658807-K'
asesor2.edad = 28
asesor2.comision = .8

asesor3 = PerfilAsesor('asesor3', 'asesorpass3', 6)
asesor3.rut = '15590224-5'
asesor3.edad = 35
asesor3.comision = 0.6

asesor4 = PerfilAsesor('asesor4', 'asesorpass4', 4)
asesor4.rut = '18765432-1'
asesor4.edad = 32
asesor4.comision = 0.4

asesor5 = PerfilAsesor('asesor5', 'asesorpass5', 8)
asesor5.rut = '12345678-9'
asesor5.edad = 29
asesor5.comision = 0.7

asesor6 = PerfilAsesor('asesor6', 'asesorpass6', 3)
asesor6.rut = '22334455-6'
asesor6.edad = 27
asesor6.comision = 0.5

asesor7 = PerfilAsesor('asesor7', 'asesorpass7', 5)
asesor7.rut = '19876543-2'
asesor7.edad = 31
asesor7.comision = 0.9

asesor8 = PerfilAsesor('asesor8', 'asesorpass8', 7)
asesor8.rut = '17654321-8'
asesor8.edad = 34
asesor8.comision = 0.2

asesor9 = PerfilAsesor('asesor9', 'asesorpass9', 5)
asesor9.rut = '23334455-6'
asesor9.edad = 28
asesor9.comision = 0.8

asesor10 = PerfilAsesor('asesor10', 'asesorpass10', 6)
asesor10.rut = '18907654-3'
asesor10.edad = 33
asesor10.comision = 0.3


# Guardar información de asesores en archivo CSV
asesor1.guardar_en_csv()
asesor2.guardar_en_csv()
asesor3.guardar_en_csv()
asesor4.guardar_en_csv()
asesor5.guardar_en_csv()
asesor6.guardar_en_csv()
asesor7.guardar_en_csv()
asesor8.guardar_en_csv()
asesor9.guardar_en_csv()
asesor10.guardar_en_csv()

cliente1 = PerfilCliente('cliente1', 'clientepass', 'Juan Pérez', '12345678-9', 'ABC123', 'Toyota', 'Corolla', 50000, '+56912345678', 'Cambio de aceite')
cliente2 = PerfilCliente('cliente2', 'clientepass2', 'María González', '98765432-1', 'XYZ789', 'Ford', 'Focus', 60000, '+56998765432', 'Revisión')
cliente3 = PerfilCliente('cliente3', 'clientepass3', 'Pedro Martínez', '76543210-8', 'PQR567', 'Honda', 'Civic', 80000, '+56976543210', 'Mantenimiento')
cliente4 = PerfilCliente('cliente4', 'clientepass4', 'Luisa Rodríguez', '54321098-7', 'LMN432', 'Mazda', 'CX-5', 30000, '+56954321098', 'Reparación')
cliente5 = PerfilCliente('cliente5', 'clientepass5', 'Jorge Silva', '34567890-6', 'JKL678', 'Chevrolet', 'Cruze', 75000, '+56934567890', 'Cambio de aceite')
cliente6 = PerfilCliente('cliente6', 'clientepass6', 'Ana López', '87654321-5', 'DEF456', 'Nissan', 'Sentra', 40000, '+56987654321', 'Alineación')
cliente7 = PerfilCliente('cliente7', 'clientepass7', 'Mario Ramírez', '67890123-4', 'OPQ901', 'Kia', 'Rio', 55000, '+56967890123', 'Frenos')
cliente8 = PerfilCliente('cliente8', 'clientepass8', 'Carla Fernández', '10987654-3', 'RST123', 'Volkswagen', 'Jetta', 20000, '+56910987654', 'Diagnóstico')
cliente9 = PerfilCliente('cliente9', 'clientepass9', 'Roberto Pérez', '98765432-1', 'UVW456', 'Toyota', 'Yaris', 65000, '+56998765432', 'Aire Acondicionado')
cliente10 = PerfilCliente('cliente10', 'clientepass10', 'María Martínez', '43210987-0', 'XYZ678', 'Ford', 'Fiesta', 35000, '+56943210987', 'Inspección')

cliente1.guardar_en_csv()
cliente2.guardar_en_csv()
cliente3.guardar_en_csv()
cliente4.guardar_en_csv()
cliente5.guardar_en_csv()
cliente6.guardar_en_csv()
cliente7.guardar_en_csv()
cliente8.guardar_en_csv()
cliente9.guardar_en_csv()
cliente10.guardar_en_csv()



#----------------------------------------------------------------------------------------------------#
#                                                                                                    #
#                                               Class User                                           #
#                                                   |                                                #
#----------------------------------------------------------------------------------------------------#
#                         |                         |                         |                      #
#                         |                         |                         |                      #
#                 Class Cliente                 Class Asesor            Class Jefe_Taller            #
#                         |                         |                         |                      #
#                 dataclientestaller  <-------------+-------------------def eliminar_usuario         #
#   (Nueva Clase)         |                         |                         |                      #
# Class Reserva--def generar_reserva -----------> def eliminar_reserva        |                      #
#                         |                     def generar_ot                |                      #
#               def imprimir_Ot    <-----------     |                         |                      #
#                         |                         |------ Class Bodega----- |   Class Proveedor    #
#                         |                         |           |             |          |           #
#                         |                         |-----> Reduce Stock      |--> Solicitar Stock   #
#                         |                         |---- Solicitar Stock---> |          |           #
#                         |                         |      Aumenta Stock <--- |<--- Class Producto   #
#                         |                         |                         |                      #
#                   imprimir_Boleta  <------- generar_boleta                  |                      #