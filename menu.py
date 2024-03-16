def mostrar_menu():
 print("Menú:")
 print("1. Personas")
 print("2. Vehículos")
 print("3. Universidades")
 print("4. Notas")
 print("5. Salir")

def main():
  mostrar_menu()
opcion = input("Selecciona una opción (1-5): ")

if opcion == "1":
 print("Hola, has presionado la opción Personas.")
elif opcion == "2":
 print("Hola, has presionado la opción Vehículos.")
elif opcion == "3":
 print("Hola, has presionado la opción Universidades.")
elif opcion == "4":
 print("Hola, has presionado la opción Notas.")
elif opcion == "5":
 print("¡Hasta luego! El programa ha finalizado.")
else:
 print("Opción inválida. Por favor, selecciona una opción válida (1,5).")

if __name__ == "__main__":
  main()