from medicacao import Medicacao
from exame import Exame

class Prognostico:

    def __init__ (self, medicacao, exame, especificadores, encaminhamentos):
        self.medicacao = medicacao
        self.exame = exame
        self.especificadores = especificadores
        self.encaminhamentos = encaminhamentos


    def create_prognostico(self):
        especificadores = input('Informe o campo especificadores: ')
        encaminhamentos = input('Informe o campo encaminhamentos: ')
        medicacao = Medicacao.create_medicacao(self)
        exame = Exame.create_exame(self)
        return Prognostico(medicacao, exame, especificadores, encaminhamentos)

    def adicionar_ao_prognostico(self):
        self.especificadores += '\n- ' + input("Informe doenca previa que deseja adicionar ao prontuario: ")
        self.encaminhamentos += '\n- ' + input("Informe o campo doenca tratada que deseja adicionar ao prontuario: ")
        #self.medicacao += '\n- ' + input("Informe o historico familiar que deseja adicionar ao prontuario: ")
        #self.exame += '\n- ' + input("Informe o grau de parentesco que deseja adicionar ao prontuario: ")
        

    def print_prognostico(self):
        print('\t== PROGNOSTICO ==')
        print(f'\nEspecificadores:\n- {self.especificadores}')
        print(f'\nencaminhamentos:\n- {self.encaminhamentos}')
       # print(f'\nHistorico familiar:\n- {self.historico_familiar}')
       # print(f'\nGrau parentesco:\n- {self.grau_parentesco}')
        


#prognosticoT = Prognostico(medicacao1, exame1, "Crônico", "Encaminhado atráves do DrLaureate")