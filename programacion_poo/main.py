from mascota import Mascota

def main():
    print("--- Creación de Objetos (Instanciación) ---\n")
    
    # Instanciamos el primer objeto de la clase Mascota
    mascota1 = Mascota("Luna", "Perro", 3)
    # Instanciamos el segundo objeto de la clase Mascota
    mascota2 = Mascota("Oliver", "Gato", 2)

    # Ejecución de métodos para el Objeto 1
    print("Datos del Primer Objeto:")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    print("-" * 40)

    # Ejecución de métodos para el Objeto 2
    print("Datos del Segundo Objeto:")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()
    print("-" * 40)

if __name__ == "__main__":
    main()