from pessoa import Pessoa
class Paciente(Pessoa):
    
    def __init__ (self, nome, idade, cpf, peso, altura, id_paciente, plano_de_saude):
        super().__init__(nome, idade, cpf, peso, altura)
        self.id_paciente = id_paciente
        self.plano_de_saude = plano_de_saude
        self.prontuario = None


    def adicionar_prontuario(self, prontuario):
        self.prontuario = prontuario

    def print_prontuario(self):
        self.prontuario.print_prontuario()
    
    def adicionar_ao_historico(self):
        self.prontuario.historico.adicionar_ao_historico()

    def adicionar_a_anamnese(self):
        self.prontuario.anamnese.adicionar_a_anamnese()

    def adicionar_a_avaliacao_inicial(self):
        self.prontuario.avaliacao_inicial.adicionar_a_avaliacao_inicial()
    
    def adicionar_ao_prognostico(self):
        self.prontuario.prognostico.adicionar_ao_prognostico()



#objeto teste:
#pacienteT = Paciente("Thales", 23, 123456789, 76, 1.73, prontuario1, "001", "Plano UniRitter Gold" )


