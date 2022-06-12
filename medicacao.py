class Medicacao:

    def __init__ (self, classe, tempo, nome, motivo):
        self.classe = classe
        self.tempo = tempo
        self.nome = nome
        self.motivo = motivo

    def adicionar_a_medicacao(self):
        print('\t== MEDICACAO == ')
        self.classe += '\n- ' + input("Informe classe que deseja adicionar ao prontuario: ")
        self.tempo += '\n- ' + input("Informe tempo que deseja adicionar ao prontuario: ")
        self.nome += '\n- ' + input("Informe nome do medicamento que deseja adicionar ao prontuario: ")
        self.motivo += '\n- ' + input("Informe motivo que deseja adicionar ao prontuario: ")


    def print_medicacao(self):
        print('== MEDICACAO == ')
        print(f'\nClasse:\n- {self.classe}')
        print(f'\nTempo:\n- {self.tempo}')
        print(f'\nNome:\n- {self.nome}')
        print(f'\nMotivo:\n- {self.motivo}')
        

#objeto teste:
#medicacao1 = Medicacao("Analgésico", "3 a 5 vezes ao dia", "Paracetamol", "Gripe ou resfriado")