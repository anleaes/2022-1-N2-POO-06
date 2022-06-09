from pessoa import Pessoa
class Medico(Pessoa):
    
    def __init__ (self, nome, idade, cpf, peso, altura, crm, unidade_de_saude, especializacao):
        super().__init__(nome, idade, cpf, peso, altura)
        self.pacientes = []
        self.numero_de_pacientes = 0
        self.crm = crm
        self.unidade_de_saude = unidade_de_saude
        self.especializacao = especializacao

    def inserir_paciente(self, paciente):
            self.pacientes.append(paciente)
            self.numero_de_pacientes += 1
    
    def print_pacientes(self):
        print('Pacientes:')
        for paciente in self.pacientes:
            print(paciente.id_paciente, paciente.nome)

    def get_paciente(self, id):
        for paciente in self.pacientes:
            if id == paciente.id_paciente:
                print(f'paciente {paciente.nome} selecionado.')

    def get_numero_pacientes(self):
        return self.numero_de_pacientes
    


#medico1 = Medico("Joao", 45, '5423123214', 80, 1.76, 'crm', 'unidade de saude', 'especializacao')
