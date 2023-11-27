from persona import Persona

class Empleado(Persona):
    
    def __init__(self, id, nombre, apellido, correo, contrasena, cargo, salario):
        
        super().__init__(id, nombre, apellido, correo, contrasena)
        
        self._cargo = cargo
        self._salario = salario
        
    # Getter and Setter (cargo)

    @property 
    def cargo(self):
        return self._cargo
    
    @cargo.setter 
    def cargo(self, cargo):
        self._cargo = cargo
        
    # Getter and Setter (salario)

    @property 
    def salario(self):
        return self._salario
    
    @salario.setter 
    def salario(self, salario):
        self._salario = salario
        
        
    def registrar(self):
        
        super().registrar()
        
        self.cargo = input("Ingrese el cargo: ")
        self.salario = float(input("Ingrese el salario: "))
        
    def ver_registro(self):
        
        super().ver_registro()
        
        print(f" Cargo: {self.cargo} \n Salario: {self.salario} \n")
        
    def iniciar_sesion(self):
        correo_reg= input("Ingrese el correo registrado")
        contra_reg = input("Ingrese la contrasela registrada")
        
        if correo_reg==self.correo and contra_reg == self.contrasena:
            print(f"Bienvenido {self.nombre}")   
            return True
        
    def iniciar_negocio(self, iniciar_sesion):
        init = iniciar_sesion()
        
        
        while init==True:
            print("1: Ver datos usuario 2: Hcer otra cosa 3: Salir")
            opc= int(input("Seleccione una opcion"))
            
            if opc==1:
             print("Ver datos usuarios")
             ver_registro()
             
            elif opc == 2:
                print("opc2")
                
            else:
                print("Seleccione opcion correcta")
                iniciar_sesion()    
                
            
                
             
             
            
            