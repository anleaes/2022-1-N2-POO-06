from paciente import Paciente
from historico import Historico
from anamnese import Anamnese
from avaliacao_inicial import AvaliacaoInicial
from prognostico import Prognostico

class Prontuario: 

    def __init__(self, historico, anamnese, avalicaoinicial, prognostico):
        #self.paciente = paciente
        self.historico = historico
        self.anamnese = anamnese
        self.avaliacaoinicial = avalicaoinicial
        self.prognostico = prognostico


#prontuario1 = Prontuario(pacienteT, historico1, anam_paci_T, av_ini_paci_T, prognosticoT)
        