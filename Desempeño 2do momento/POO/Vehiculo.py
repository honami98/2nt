class vehiculo:
    
    def __init__(self, marca, modelo, color ):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        
    def ver_vehiculo(self):
        print(f"Marca{self.marca} \n modelo{self.modelo} \n color{self.color} \n")
            
vehiculo1= vehiculo("Toyota",2023,"Gris plata")

if __name__ == '__main__':
    
    
    print(vehiculo1.marca)
    print(vehiculo1.modelo)
    print(vehiculo1.color)

vehiculo1.modelo = "Tesla"

ver = vehiculo1.ver_vehiculo()


    
    



            
