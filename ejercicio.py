class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
    def __str__(self):
        return f'Usuario: {self.nombre}, Contraseña: {self.contraseña}'

pedro = Usuario('Pedro', 'Pedro123')
print(str(pedro))