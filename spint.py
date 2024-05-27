import random
import string

# Lista de nombres de usuarios
nombres_usuarios = ["Nombre 1", "Nombre 2", "Nombre 3", "Nombre 4", "Nombre 5",
                    "Nombre 6", "Nombre 7", "Nombre 8", "Nombre 9", "Nombre 10"]

# Función para crear una contraseña segura
def generar_contrasena():
  longitud_contrasena = 12
  caracteres = string.ascii_letters + string.digits + string.punctuation
  contrasena_aleatoria = "".join(random.choice(caracteres) for i in range(longitud_contrasena))
  return contrasena_aleatoria

# Función para crear una cuenta de usuario
def crear_cuenta(nombre_usuario):
  contrasena = generar_contrasena()
  numero_telefonico = None
  while not numero_telefonico:
    numero_telefonico = input(f"Ingrese el número de teléfono de {nombre_usuario} (8 dígitos): ")
    if not numero_telefonico.isdigit() or len(numero_telefonico) != 8:
      print("Número de teléfono inválido. Debe tener 8 dígitos numéricos.")
  cuenta = {
    "nombre": nombre_usuario,
    "contrasena": contrasena,
    "numero_telefonico": numero_telefonico
  }
  print(f"Cuenta creada para {nombre_usuario}:")
  print(f"Contraseña: {contrasena}")
  print(f"Número de teléfono: {numero_telefonico}")
  return cuenta

# Creación de cuentas para todos los usuarios
cuentas_usuarios = []
for nombre_usuario in nombres_usuarios:
  cuenta = crear_cuenta(nombre_usuario)
  cuentas_usuarios.append(cuenta)

# Impresión de la información de las cuentas
print("\nInformación de las cuentas:")
for cuenta in cuentas_usuarios:
  print(f"Nombre: {cuenta['nombre']}")
  print(f"Contraseña: {cuenta['contrasena']}")
  print(f"Número de teléfono: {cuenta['numero_telefonico']}")
  print("-" * 20)


