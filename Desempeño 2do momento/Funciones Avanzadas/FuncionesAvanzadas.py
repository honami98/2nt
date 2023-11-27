#Debemos de calcular los descuentos de ley de pago de nomina de un empleado

#Tomar salario-pension-salud

salario = 0

salario = float(input(" Ingrese su salario: "))

def descontarSalud(salario):
    return salario * 0.04

def descontarPension(salario):
    return salario * 0.04

eps = descontarSalud (salario)

pension = descontarPension (salario)

def pagoNominaEmpleado(salario, eps, pension):
    salario_neto= salario - eps - pension
    print(salario_neto)
    
pagoNominaEmpleado (salario, eps, pension)


def imprimirSalario(valor):
    print(f"El salario neto es: {valor}")
    #Esta es la funcion principal
    
def pagoNominaEmpleado2(salario, imprimirSalario):
    eps = descontarSalud(salario)
    pension = descontarPension(salario)
    salario_neto= salario - eps - pension
    imprimirSalario(salario_neto)
    
pagoNominaEmpleado2 (salario, imprimirSalario)

def pagoNominaEmpleado3(salario):
    eps = lambda salary: salary * 0.04
    pension = lambda salary: salary * 0.04
    salario_neto = salario - eps(salario) - pension(salario)
    print(salario_neto)

pagoNominaEmpleado3 (salario)    
    
    
    

