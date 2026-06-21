class Soldado:
    def __init__(self, nombre, rango):
        self.nombre = nombre       
        self.rango = rango
        self.inventario = []       

    def adquirir_arma(self, arma):
        self.inventario.append(arma)

    def calcular_gasto_total(self):
        return sum(arma.precio for arma in self.inventario)
        
    def __str__(self):
        return f"Soldado: {self.nombre} [{self.rango}]"