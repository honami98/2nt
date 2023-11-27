import sys
import os

# Importar los módulos necesarios (sys y os) para interactuar con el sistema y limpiar la pantalla de la consola.

# Definir una función para limpiar la pantalla de la consola.
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola usando 'cls' en Windows y 'clear' en Unix/Linux.

# Llamar a la función limpiar_consola para limpiar la pantalla de la consola.
limpiar_consola()

# Crear dos listas vacías para almacenar información de empleados y colillas de pago.
empleados = []
colillas_pago = []

# Definir una función lambda para calcular el salario neto de los empleados.
calcular_salario_neto_lambda = lambda salario, salario_minimo: salario + 140000 if salario < 2 * salario_minimo else salario

# Definir una función para agregar empleados a la lista de empleados.
def agregar_empleado(id, nombre, apellido, cargo, area, salario):
    empleado = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "area": area,
        "salario": salario
    }
    empleados.append(empleado)

# Definir una función para listar a todos los empleados.
def listar_empleados():
    for empleado in empleados:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}")

# Definir una función para calcular el salario neto de los empleados y agregarlo a la lista de colillas de pago.
def calcular_salario_neto():
    salario_minimo = 1160000  # Valor del salario mínimo vigente (ejemplo)
    for empleado in empleados:
        salario_neto = calcular_salario_neto_lambda(empleado['salario'], salario_minimo)  # Utilizar la función lambda
        empleado['salario_neto'] = salario_neto  # Agregar salario neto al empleado
        colillas_pago.append((empleado, salario_neto))

# Definir una función para imprimir las colillas de pago de los empleados.
def imprimir_colilla_pago():
    for empleado, salario_neto in colillas_pago:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}, Salario Neto: {salario_neto}")

# Definir una función para buscar a un empleado por su ID y mostrar su información.
def buscar_empleado_por_id(id):
    for empleado in empleados:
        if empleado['id'] == id:
            print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}, Salario Neto: {empleado['salario_neto']}")
            return
    print("Empleado no encontrado")

# Definir una función para registrar un nuevo empleado.
def registrar_empleado():
    id = int(input("Ingrese el ID del empleado: "))
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    area = input("Ingrese el área del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    limpiar_consola()
    agregar_empleado(id, nombre, apellido, cargo, area, salario)
    print(f"Empleado {nombre} {apellido} registrado con éxito.")
    after_action_callback()

# Definir una función para mostrar el menú de listar empleados y llamar a la función de listar empleados.
def menu_listar_empleados():
    print("\nEmpleados:")
    listar_empleados()
    after_action_callback()

# Definir una función para mostrar el menú de calcular salarios netos y llamar a la función de calcular salarios netos.
def menu_calcular_salarios():
    calcular_salario_neto()
    print("\nSalarios netos calculados.")
    after_action_callback()

# Definir una función para mostrar el menú de imprimir colillas de pago y llamar a la función de imprimir colillas de pago.
def menu_imprimir_colillas():
    print("\nColillas de Pago:")
    imprimir_colilla_pago()
    after_action_callback()

# Definir una función para mostrar el menú de buscar empleado por ID y llamar a la función de buscar empleado por ID.
def menu_buscar_empleado():
    id_buscado = int(input("Ingrese el ID del empleado a buscar: "))
    buscar_empleado_por_id(id_buscado)
    after_action_callback()

# Definir una función para el rol de "analista" que muestra un menú de opciones.
def analista():
    while True:
        print("\nMenú:")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Calcular salarios netos")
        print("4. Imprimir colillas de pago")
        print("5. Buscar empleado por ID")
        print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ")
        limpiar_consola()

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            menu_listar_empleados()
        elif opcion == "3":
            menu_calcular_salarios()
        elif opcion == "4":
            menu_imprimir_colillas()
        elif opcion == "5":
            menu_buscar_empleado()
        elif opcion == "6":
            login()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Definir una función para el rol de "empleado" que muestra un menú de opciones.
def empleado():
    while True:
        print("\n🟩 MENU 🟩")
        print("1. Buscar colilla de pago con tu cédula")
        print("2. Cerrar sesión")

        opcion = input("Seleccione una opción: ")
        limpiar_consola()

        if opcion == "1":
            calcular_salario_neto()  # Calcular salarios antes de buscar
            id_buscado = int(input("Ingrese el ID del empleado a buscar: "))
            buscar_empleado_por_id(id_buscado)
            after_action_callback()
        elif opcion == "2":
            login()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Definir una función para el inicio de sesión que permite a los usuarios iniciar sesión como "analista" o "empleado".
def login():
    print("\n" + "🟪 INICIO DE SESIÓN 🟪")
    print("1. Iniciar sesión como analista")
    print("2. Iniciar sesión como empleado")
    print("3. Salir")

    modo = input("Ingrese el modo deseado: ")

    if modo == "1":
        usuario_Analista = "Analista"
        contraseña_Analista = "111"

        usuario_a = input("Nombre de usuario: ")
        contraseña_a = input("Contraseña: ")
        limpiar_consola()

        if usuario_a == usuario_Analista and contraseña_a == contraseña_Analista:
            print("\nInicio de sesión exitoso.\n")
            analista()
        else:
            print("\nError: Nombre de usuario o contraseña incorrectos.\n")

    elif modo == "2":
        usuario_empleado = "Empleado"
        contraseña_empleado = "222"

        usuario_e = input("Nombre de usuario: ")
        contraseña_e = input("Contraseña: ")
        limpiar_consola()

        if usuario_e == usuario_empleado and contraseña_e == contraseña_empleado:
            print("\nInicio de sesión exitoso.\n")
            empleado()
        else:
            print("\nError: Nombre de usuario o contraseña incorrectos.\n")
            login()
    else:
        print("\nSaliendo del programa.")
        sys.exit()
          

# Definir una función para esperar a que el usuario presione Enter antes de continuar.
def after_action_callback():
    input("\nPresiona Enter para continuar...")
    limpiar_consola()

# Iniciar el programa llamando a la función de inicio de sesión.
login()
