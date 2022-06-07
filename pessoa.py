class Pessoa():

    def __init__(self, nome, idade, cpf, peso, altura):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.peso = peso
        self.altura = altura

    def validar_cpf(cpf=None):
        if cpf is not None:
            return True
            print ("cpf válido")
        else:
            return False
            print("cpf inválido")
    