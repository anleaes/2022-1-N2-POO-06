class Pessoa:

    def __init__(self, nome, idade, cpf, peso, altura):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.peso = peso
        self.altura = altura

    def validar_cpf(cpf=None):
        if cpf is not None:
            return print ("cpf válido")
        else:
            return print("cpf inválido")
            
#pessoaT = Pessoa("Thales", 23, 123456789, 76, 173)
#pessoaG = Pessoa("Gabriel", 21, 987654321, 70, 180)
