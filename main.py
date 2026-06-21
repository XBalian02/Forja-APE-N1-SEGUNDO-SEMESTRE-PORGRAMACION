# main.py

# 1. IMPORTACIONES: Traemos los moldes de tus carpetas
from modelos.espada import Espada
from modelos.soldado import Soldado
from servicios.forja import Forja

def iniciar_programa():
    # 2. Creamos tu negocio (La Forja)
    mi_forja = Forja("La Forja Imperial")
    print("--- INICIANDO SISTEMA DE LA FORJA MODULAR ---\n")
    
    # 3. Creamos las espadas usando TU MOLDE EXACTO: (nombre, daño, modelo, precio)
    espada1 = Espada("Filo Nocturno", 85, "Katana", 120.0)
    espada2 = Espada("Guardia del Rey", 95, "Espada Larga", 150.0)
    espada3 = Espada("Aguijón Veloz", 60, "Ropera", 90.0)
    
    # 4. Forjamos las armas para meterlas al catálogo
    mi_forja.forjar_espada(espada1)
    mi_forja.forjar_espada(espada2)
    mi_forja.forjar_espada(espada3)
    
    # 5. Mostramos el catálogo disponible en la armería
    mi_forja.mostrar_catalogo()
    
    # 6. Creamos a los soldados clientes
    soldado1 = Soldado("Alaric", "Capitán")
    soldado2 = Soldado("Boran", "Recluta")
    
    print("\n--- REGISTRANDO CLIENTES ---")
    mi_forja.registrar_soldado(soldado1)
    mi_forja.registrar_soldado(soldado2)
    
    # 7. SIMULACIÓN DE COMPRA: Los soldados adquieren las armas
    soldado1.adquirir_arma(espada1)
    soldado1.adquirir_arma(espada2)
    soldado2.adquirir_arma(espada3)
    
    # 8. Desplegamos el reporte final con todo lo recaudado
    mi_forja.mostrar_reporte_armerería()

if __name__ == "__main__":
    iniciar_programa()
    