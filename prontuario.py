from historico import Historico
from exames import Exames
from anamnese import Anamnese
from avaliacaoinicial import Avaliacaoinicial
from prognostico import Prognostico 
from medicacao import Medicacao

class Prontuario: 

    def __init__(self, historico, exames, anamnese, avalicaoinicial, prognostico, medicacao):
        self.historico = historico
        self.exames = exames
        self.anamnese = anamnese
        self.avaliacaoinicial = avalicaoinicial
        self.prognostico = prognostico
        self.medicacao = medicacao

        