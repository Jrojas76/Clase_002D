import csv
lista_trabajadores = []

def menu():
    print('Menu principal:')
    print('1. Registrar trabajador')
    print('2. Listar todos los trabajadores')
    print('3. Imprimir plantilla de sueldos')
    print('4. Salir')

def opcion1():
  print('Ha seleccionado la opcion 1, Registrar trabajador')
  nombre_apellido = input('Ingrese el nombre y apellido del trabajador: ')
  lista_trabajadores.append(nombre_apellido)
  cargo = input('Ingrese el cargo del trabajador: ')
  lista_trabajadores.append(cargo)
  sueldo_bruto = int(input('Ingrese el sueldo bruto del trabajador: '))
  lista_trabajadores.append(sueldo_bruto)
  desc_afp = 0.12
  desc_salud = 0.07
  sueldo_liquido = sueldo_bruto - ((desc_salud * sueldo_bruto) + (desc_afp * sueldo_bruto))
  lista_trabajadores.append(sueldo_liquido)
  print(f'El sueldo liquido es {sueldo_liquido}')


def opcion2():
  print('Ha seleccionado la opcion 2, Listar todos los trabajadores')
  print(lista_trabajadores)

def opcion3():
  print('Ha seleccionado la opcion 3, Imprimir plantilla de trabajadores')
  with open('tabla_t.txt', 'w') as archivo:
    contenido = archivo.write(tabla_t)
    print(contenido)


tabla_t = 'tabla_t.txt'
control = True

while control:
  menu()
  opcion = input('Seleccione una opcion (1, 2, 3, 4): ')
  if opcion == '1':
    opcion1()
  elif opcion == '2':
    opcion2()
  elif opcion == '3':
    opcion3()
  elif opcion == '4':
    print('Saliendo del programa...')
    control = False
  else:
    ValueError('Opcion no valida. Ingrese una opcion entre (1, 2, 3, 4)')