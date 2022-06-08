from paciente import Paciente
from historico import Historico
from anamnese import Anamnese
from avaliacao_inicial import AvaliacaoInicial
from prognostico import Prognostico
class Prontuario: 

    def __init__(self, paciente, historico, anamnese, avalicaoinicial, prognostico):
        self.paciente = paciente
        self.historico = historico
        self.anamnese = anamnese
        self.avaliacaoinicial = avalicaoinicial
        self.prognostico = prognostico


#print("Prontuário do paciente Teste")
#print(pacienteteste.historico, pacienteteste.anamnese, pacienteteste.avaliacao_inicial, pacienteteste.prognostico)
        