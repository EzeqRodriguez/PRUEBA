class Clientes():

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


class Black(Clientes):

    
    def __init__(self, nombre, apellido, dni):

        super().__init__(nombre, apellido, dni)

        self.tipo = "Black"
        self.chequera = 2
        self.tarjetaC = 5
        self.retiroMax = 100000

class Classic(Clientes):

    def __init__(self, nombre, apellido, dni):

        super().__init__(nombre, apellido, dni)

        self.tipo = "Classic"
        self.chequera = False
        self.dolar = False
        self.tarjetaC = False
        self.retiroMax = 10000
        self.transMax = 150000

class Gold(Clientes):
    
    def __init__(self, nombre, apellido, dni):
        
        super().__init__(nombre, apellido, dni)
        
        self.tipo = "Gold"
        self.chequera = 1
        self.tarjetaC = 1
        self.dolar = True
        self.retiroMax = 20000
        self.transMax = 500000