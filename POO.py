class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # Não é obrigatório ser self mas é boa prática
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Bibibibi')

    def parar(self):
        print('Parei porra, que é???')

    def correr(self):
        print('Sai do mei que eu tô passando')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}'

# B1 = Bicicleta('Vermelha','Caloi', 2023, 1500)

# B1.buzinar()
# B1.correr()
# B1.parar()
# print(B1.cor, B1.modelo, B1.ano, B1.valor)
# print(B1) # Quando for só assim vai imprimir oq estiver no __str__

cor = input('Qual a cor da sua bicicleta? ').capitalize()
modelo = input('De que marca é ela? ').capitalize()
ano = input('Em que ano comprou ela? ')
valor = input('E por quanto comprou? ')

B1 = Bicicleta(cor, modelo, ano, valor)
print(B1)