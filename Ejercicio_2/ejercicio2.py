# EJERCICIO 2 - PRODUCTOS, EXCEPCIONES Y PERSISTENCIA
import json


class StockInvalidoError(Exception):
    """Error que aparece cuando se intenta usar un stock negativo."""
    pass


class DispositivoEcologico:
    def __init__(self, modelo, precio, stock):
        self.modelo = modelo
        self.precio = precio
        self.set_stock(stock)

    # Getter: permite consultar el stock.
    def get_stock(self):
        return self.__stock

    # Setter: permite cambiar el stock y controla que no sea negativo.
    def set_stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede ser negativo.")
        self.__stock = nuevo_stock

    def obtener_ficha_tecnica(self):
        return f"Modelo: {self.modelo} | Precio: ${self.precio} | Stock: {self.get_stock()}"

    def a_diccionario(self):
        return {
            "tipo": "DispositivoEcologico",
            "modelo": self.modelo,
            "precio": self.precio,
            "stock": self.get_stock()
        }


class PanelSolar(DispositivoEcologico):
    def __init__(self, modelo, precio, stock, eficiencia_watts):
        super().__init__(modelo, precio, stock)
        self.eficiencia_watts = eficiencia_watts

    # Polimorfismo: este metodo muestra una ficha diferente.
    def obtener_ficha_tecnica(self):
        ficha = super().obtener_ficha_tecnica()
        return ficha + f" | Potencia: {self.eficiencia_watts}W | Panel solar"

    def a_diccionario(self):
        return {
            "tipo": "PanelSolar",
            "modelo": self.modelo,
            "precio": self.precio,
            "stock": self.get_stock(),
            "eficiencia_watts": self.eficiencia_watts
        }


class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        catalogo = []

        for dispositivo in lista_dispositivos:
            catalogo.append(dispositivo.a_diccionario())

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)

        print("Catalogo guardado correctamente en", ruta_archivo)


if __name__ == "__main__":
    # Creamos productos validos.
    dispositivo1 = DispositivoEcologico("Termostato Eco", 350.0, 8)
    panel1 = PanelSolar("SolarMax-500", 1200.0, 10, 500)

    # Probamos que el error de stock se capture sin cerrar el programa.
    try:
        dispositivo1.set_stock(-5)
    except StockInvalidoError as error:
        print("Error controlado:", error)

    # Mostramos las fichas de los productos.
    print(dispositivo1.obtener_ficha_tecnica())
    print(panel1.obtener_ficha_tecnica())

    # Guardamos solamente los productos validos.
    inventario = [dispositivo1, panel1]
    gestor = GestorInventario()
    gestor.guardar_catalogo_json(inventario, "catalogo_ecotech.json")
