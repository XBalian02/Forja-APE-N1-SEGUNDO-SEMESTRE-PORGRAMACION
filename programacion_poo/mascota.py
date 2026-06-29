class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int):
        """
        Constructor de la clase. 
        Define los atributos del objeto (Abstracción).
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Método para mostrar los atributos del objeto organizado."""
        print(f"Mascota: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años")

    def hacer_sonido(self):
        """Método que simula el comportamiento/sonido según la especie."""
        especie_low = self.especie.lower()
        if "perro" in especie_low:
            sonido = "¡Guau Guau!"
        elif "gato" in especie_low:
            sonido = "¡Miau Miau!"
        else:
            sonido = "*Sonido de mascota desconocido*"
        
        print(f"{self.nombre} dice: {sonido}")