from pessoa import Pessoa
class Paciente(Pessoa):
    
    def __init__ (self, nome, idade, cpf, peso, altura, id_paciente, plano_de_saude):
        super().__init__(nome, idade, cpf, peso, altura)
        self.prontuario = None
        self.id_paciente = id_paciente
        self.plano_de_saude = plano_de_saude





#pacienteT = Paciente("Thales", 23, 123456789, 76, 1.73, prontuario1, "001", "Plano UniRitter Gold" )