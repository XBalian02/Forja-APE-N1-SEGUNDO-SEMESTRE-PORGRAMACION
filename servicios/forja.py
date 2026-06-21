class Forja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo_espadas = []
        self.soldados_registrados = []

    def forjar_espada(self, espada):
        self.catalogo_espadas.append(espada)
        print(f"[Forja] Se forjó chevere tu espada: {espada.nombre} con daño {espada.daño} y modelo {espada.modelo} por un precio de {espada.precio}.")

    def registrar_soldado(self, soldado):
        self.soldados_registrados.append(soldado)
        print(f"[Forja] Soldado registrado: {soldado.nombre} con rango {soldado.rango}.")

    def mostrar_catalogo(self):
        print(f"[Forja] Catálogo de Espadas en {self.nombre}:")
        for espada in self.catalogo_espadas:
            print(f" - {espada}")
        print("=" * 60) 

    def mostrar_reporte_armerería(self):
        print(f"\n[Forja] Reporte de Armería en {self.nombre}:")
        for soldado in self.soldados_registrados:
            print(f"\n * {soldado}")
            print("   Armas en su inventario:")
            for arma in soldado.inventario:
                print(f"    - {arma.nombre} (Modelo: {arma.modelo})")
            print(f"   Total gastado: {soldado.calcular_gasto_total()} monedas")
        print("=" * 60)
