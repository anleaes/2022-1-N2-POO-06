from pessoa import Pessoa

class Medico(Pessoa):
    
    def __init__ (self, nome, idade, cpf, peso, altura, crm, unidade_de_saude, especializacao):
        super().__init__(nome, idade, cpf, peso, altura)
        self.cadastro = None
        self.crm = crm
        self.unidade_de_saude = unidade_de_saude
        self.especializacao = especializacao

    
    def adicionar_cadastro(self, cadastro):
        self.cadastro = cadastro

    def get_paciente(self, id):
        for paciente in self.cadastro.pacientes:
            if id == paciente.id_paciente:
                print(f'paciente {paciente.nome} selecionado.')
                return paciente

    def get_numero_pacientes(self):
        return self.cadastro.numero_de_pacientes_cadastrados
    
    def verify_if_id_exists(self, id):
        if id <= self.get_numero_pacientes() and id > 0:
            return True
        else:
            return False
    
    def get_id(self):
        while True:
            id = int(input('Digite o ID do paciente: '))
            if self.verify_if_id_exists(id):
                return id
        
    def get_nome_paciente(self, paciente_selecionado):
        return paciente_selecionado.nome


#medico1 = Medico("Joao", 45, '5423123214', 80, 1.76, 'crm', 'unidade de saude', 'especializacao')

