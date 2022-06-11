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

#prognosticoT = Prognostico(medicacao1, exame1, "Crônico", "Encaminhado atráves do DrLaureate")