from Vehiculo import vehiculo

class Moto(vehiculo):
    
    freno = "abs"

    def _init_(self, marca, modelo, color, categoria):
        super()._init_(marca, modelo, color)
        self.categoria = categoria
        
    def ver_vehiculo(self):
        super(Moto, self).ver_vehiculo()
        print(f"Categoria: {self.categoria} \nTipo freno: {self.freno} \n")
        
mt09 = Moto("Yamaha", "2023", "Negro mate", "Scooter")

mt09.ver_vehiculo()