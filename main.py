from paciente import Paciente
from historico import Historico
from anamnese import Anamnese
from avaliacao_inicial import AvaliacaoInicial
from prognostico import Prognostico
from exame import Exame
from medicacao import Medicacao
from prontuario import Prontuario
from medico import Medico
from cadastro import Cadastro

# instanciando os objetos
historico1 = Historico("Câncer de pele", "Cirurgia para remoção - ÊXITO", "Sem histórico", "Nenhum")
anam_paci_T = Anamnese("Vigil", "Perda de memória recente", "Raiva e agressividade" ,"Fala em alto volume e com rapidez")
av_ini_paci_T = AvaliacaoInicial("Dores de cabeça", "07/06/22", "Febre, dor atrás dos olhos e tosse", "Suspeita de covid")
prognosticoT = Prognostico("Analgésico", "3 a 5 vezes ao dia", "Paracetamol", "Gripe ou resfriado", "07/02/21", "Ressonancia", "Inflamação no estômago", "Precisa operar urgentemente", "Crônico", "Encaminhado atráves do DrLaureate")
pacienteT = Paciente("Thales", 23, '123456789', 76, 1.73, 1, "Plano UniRitter Gold" )
prontuario1 = Prontuario(pacienteT, historico1, anam_paci_T, av_ini_paci_T, prognosticoT)
medico1 = Medico("Joao", 45, '5423123214', 80, 1.76, 'crm', 'unidade de saude', 'especializacao')
pacienteK = Paciente("Kleyton", 21, '3214123124', 56, 1.62, 2, "Plano UniRitter Platinum" )
cadastro1 = Cadastro(medico1)

#cadastrando objetos para usar de exemplo 

medico1.adicionar_cadastro(cadastro1)
pacienteT.adicionar_prontuario(prontuario1)

cadastro1.inserir_paciente(pacienteT)
cadastro1.inserir_paciente(pacienteK)



print('Bem-vindo ao sistema Thales&Gabriel')

menu_inicial = True
while menu_inicial:

    resposta_menu_inicial = input('\n1 - Cadastrar paciente\n2 - Ver pacientes\n3 - Selecionar paciente cadastrado\n4 - Sair do sistema\nSelecione uma ação: ')
    if resposta_menu_inicial == '1':
        cadastro1.cadastrar_paciente()
    elif resposta_menu_inicial == '2':
        cadastro1.print_pacientes_cadastrados()
    elif resposta_menu_inicial == '3':
        cadastro1.print_pacientes_cadastrados()
        id_paciente_selecionado = medico1.get_id()
        paciente_selecionado = medico1.get_paciente(id_paciente_selecionado)

        menu_paciente = True
        while menu_paciente:
            print('\n-- Paciente', medico1.get_nome_paciente(paciente_selecionado), '--')
            resposta_menu_paciente = input('\n1 - Cadastrar prontuario do paciente\n2 - Ver prontuario\n3 - Adicionar historico\n4 - Adicionar anamnese\n5 - Adicionar avaliacao inicial\n6 - Adicionar prognostico\n7 - Voltar ao menu anterior\n8 - Sair do sistema\nSelecione uma ação: ')
            if resposta_menu_paciente == '1':
                if cadastro1.verify_prontuario(paciente_selecionado):
                    print('Paciente já tem prontuário cadastrado.')
                else:
                    print('Prontuario cadastrado!')
            elif resposta_menu_paciente == '2':
                if cadastro1.verify_prontuario(paciente_selecionado):
                    paciente_selecionado.print_prontuario()
            elif resposta_menu_paciente == '3':
                 if cadastro1.verify_prontuario(paciente_selecionado):
                    paciente_selecionado.adicionar_ao_historico()
            elif resposta_menu_paciente == '4':
                 if cadastro1.verify_prontuario(paciente_selecionado):
                    paciente_selecionado.adicionar_a_anamnese()
            elif resposta_menu_paciente == '5':
                if cadastro1.verify_prontuario(paciente_selecionado):
                    paciente_selecionado.adicionar_a_avaliacao_inicial()
            elif resposta_menu_paciente == '6':
                if cadastro1.verify_prontuario(paciente_selecionado):
                    paciente_selecionado.adicionar_ao_prognostico()
            elif resposta_menu_paciente == '7':
                print('\nBem-vindo ao sistema X')
                break
            elif resposta_menu_paciente == '8':
                menu_inicial = False
                break
            else:
                print('Input invalido')
    elif resposta_menu_inicial == '4':
        menu_inicial = False
    else:
        print('input invalido.\n')


