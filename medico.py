from paciente import Paciente
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
                return self.pacientes.index(paciente)

    def get_numero_pacientes(self):
        return self.numero_de_pacientes

    def cadastro_paciente(self):
        nome_paciente = input('Digite o nome do paciente: ')
        idade_paciente = int(input('Digite a idade do paciente: '))
        cpf_paciente = input('Digite o CPF do pac3iente: ')
        peso_paciente = float(input('Digite o peso do paciente: '))
        altura_paciente = float(input('Digite a altura do paciente: '))
        plano_de_saude_paciente = input('Digite qual o plano de saúde do paciente: ')
        self.pacientes.append(Paciente(nome_paciente, idade_paciente, cpf_paciente, peso_paciente, altura_paciente, self.numero_de_pacientes+1, plano_de_saude_paciente))
        self.numero_de_pacientes += 1
    
    def verify_if_id_exists(self, id):
        if id <= self.get_numero_pacientes() and id > 0:
            return True
        else:
            return False
    
    def get_id(self):
        while True:
            id = int(input('Digite o ID do paciente: '))
            id_verified = self.verify_if_id_exists(id)
            if id_verified:
                return id
        
    def get_nome_paciente(self, paciente_selecionado):
        return self.pacientes[paciente_selecionado].nome

    

#medico1 = Medico("Joao", 45, '5423123214', 80, 1.76, 'crm', 'unidade de saude', 'especializacao')
