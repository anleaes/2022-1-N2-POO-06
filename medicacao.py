class Medicacao:

    def __init__ (self, classe, tempo, nome, motivo):
        self.classe = classe
        self.tempo = tempo
        self.nome = nome
        self.motivo = motivo

    def create_medicacao(self):
        print('== MEDICACAO == ')
        classe = input('Informe o campo classe: ')
        tempo = input('Informe o campo tempo: ')
        nome = input('Informe o campo nome: ')
        motivo = input('Informe o campo motivo: ')
        return Medicacao(classe, tempo, nome, motivo)

#medicacao1 = Medicacao("Analgésico", "3 a 5 vezes ao dia", "Paracetamol", "Gripe ou resfriado")