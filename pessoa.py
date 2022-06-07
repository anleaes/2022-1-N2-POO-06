class Pessoa():

    def __init__(self, nome, idade, cpf, peso, altura):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._peso = peso
        self._altura = altura

    def validar_cpf(cpf=None):
        if cpf is not None:
            return print ("cpf válido")

        else:
            return print("cpf inválido")
            
    