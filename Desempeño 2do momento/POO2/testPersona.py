from persona import Persona

persona1 = Persona(id=None,
                   nombre=None,
                   apellido=None,
                   correo=None,
                   contrasena=None)

persona1._id = "1"
print(persona1._id)

persona1.registrar()
persona1.ver_registro()
