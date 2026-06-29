def registrar_mascota():
    print("--- Registro de Mascota ---")
    nombre = input("Ingrese el nombre de la mascota: ").strip()
    especie = input("Ingrese la especie (ej. Perro, Gato): ").strip()
    
    
    while True:
        try:
            edad = int(input("Ingrese la edad de la mascota (en años): "))
            if edad >= 0:
                break
            print("La edad no puede ser negativa.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            
    return {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }

def mostrar_mascota(mascota):
    print("\n=============================")
    print("   INFORMACIÓN DE LA MASCOTA ")
    print("=============================")
    print(f"Nombre:  {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad:    {mascota['edad']} años")
    print("=============================\n")

def main():
    # Flujo principal del programa tradicional
    mascota_registrada = registrar_mascota()
    mostrar_mascota(mascota_registrada)

if __name__ == "__main__":
    main()