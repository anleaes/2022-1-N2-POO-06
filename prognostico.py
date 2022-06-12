from medicacao import Medicacao
from exame import Exame

class Prognostico(Medicacao, Exame):

    def __init__ (self, classe, tempo, nome, motivo, data, tipo, resultado, avaliacao, especificadores, encaminhamentos):
        Medicacao.__init__ (self, classe, tempo, nome, motivo)
        Exame.__init__(self, data, tipo, resultado, avaliacao)
        self.especificadores = especificadores
        self.encaminhamentos = encaminhamentos


    def create_prognostico(self):
        especificadores = input('Informe o campo especificadores: ')
        encaminhamentos = input('Informe o campo encaminhamentos: ')
        print('\t== MEDICACAO == ')
        classe = input('Informe o campo classe: ')
        tempo = input('Informe o campo tempo: ')
        nome = input('Informe o campo nome: ')
        motivo = input('Informe o campo motivo: ')

        print('== EXAME ==')
        data = input('Informe o campo data: ')
        tipo = input('Informe o campo tipo: ')
        resultado = input('Informe o campo resultado: ')
        avaliacao = input('Informe o campo avaliacao: ')


        return Prognostico(classe, tempo, nome, motivo, data, tipo, resultado, avaliacao, especificadores, encaminhamentos)

    def adicionar_ao_prognostico(self):
        self.especificadores += '\n- ' + input("Informe doenca previa que deseja adicionar ao prontuario: ")
        self.encaminhamentos += '\n- ' + input("Informe o campo doenca tratada que deseja adicionar ao prontuario: ")
        self.adicionar_a_medicacao()
        self.adicionar_ao_exame()

    def print_prognostico(self):
        print('\t== PROGNOSTICO ==')
        print(f'\nEspecificadores:\n- {self.especificadores}')
        print(f'\nencaminhamentos:\n- {self.encaminhamentos}')        
        self.print_medicacao()
        self.print_exame()

        

#objeto teste:
#prognosticoT = Prognostico(medicacao1, exame1, "Crônico", "Encaminhado atráves do DrLaureate")