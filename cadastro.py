from asyncio import ProactorEventLoop
from paciente import Paciente
from prontuario import Prontuario
from historico import Historico
from anamnese import Anamnese
from avaliacao_inicial import AvaliacaoInicial
from prognostico import Prognostico
from medicacao import Medicacao
from exame import Exame

class Cadastro:

    def __init__(self, medico):
        self.medico = medico
        self.pacientes = []
        self.numero_de_pacientes_cadastrados = 0

    
    def cadastrar_paciente(self):
        nome_paciente = input('Digite o nome do paciente: ')
        idade_paciente = int(input('Digite a idade do paciente: '))
        cpf_paciente = input('Digite o CPF do pac3iente: ')
        peso_paciente = float(input('Digite o peso do paciente: '))
        altura_paciente = float(input('Digite a altura do paciente: '))
        plano_de_saude_paciente = input('Digite qual o plano de saúde do paciente: ')
        self.pacientes.append(Paciente(nome_paciente, idade_paciente, cpf_paciente, peso_paciente, altura_paciente, self.numero_de_pacientes_cadastrados+1, plano_de_saude_paciente))
        self.numero_de_pacientes_cadastrados += 1

    def inserir_paciente(self, paciente):
        self.pacientes.append(paciente)
        self.numero_de_pacientes_cadastrados += 1
    
    def print_pacientes_cadastrados(self):
        print('Pacientes:')
        for paciente in self.pacientes:
            print(paciente.id_paciente, paciente.nome)
    
    def cadastrar_prontuario(self, paciente):
        print('\nCadastrando prontuario do paciente...\n')
        print('== HISTORICO ==')
        historico = Historico.create_historico(self)
        print('== ANAMNESE ==')
        anamnese = Anamnese.create_anamnese(self)
        print('== AVALIACAO INICIAL ==')
        avaliacao_inicial = AvaliacaoInicial.create_avaliacao_inicial(self)
        print('== PROGNOSTICO ==')
        prognostico = Prognostico.create_prognostico(self)
        paciente.prontuario = (Prontuario(paciente, historico, anamnese, avaliacao_inicial, prognostico))

    def verify_prontuario(self, paciente):
        if paciente.prontuario == None:
            print('Paciente selecionado ainda nao possui prontuario cadastrado\nDeve ser feito o cadastro para prosseguir:')
            self.cadastrar_prontuario(paciente)
            return False
        else:
            return True