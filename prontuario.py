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
    

    def cadastrar_historico(self):
        self.historico = self.historico.create_historico()

    def get_historico(self):
        return self.historico.__dict__

    def print_historico_teste(self):
        print(self.historico.__dict__)

#prontuario1 = Prontuario(pacienteT, historico1, anam_paci_T, av_ini_paci_T, prognosticoT)
        