from paciente import Paciente
from historico import Historico
from anamnese import Anamnese
from avaliacao_inicial import AvaliacaoInicial
from prognostico import Prognostico
from exame import Exame
from medicacao import Medicacao
from prontuario import Prontuario
from medico import Medico


historico1 = Historico("Câncer de pele", "Cirurgia para remoção - ÊXITO", "Sem histórico", "Nenhum")
anam_paci_T = Anamnese("Vigil", "Perda de memória recente", "Raiva e agressividade" ,"Fala em alto volume e com rapidez")
av_ini_paci_T = AvaliacaoInicial("Dores de cabeça", "07/06/22", "Febre, dor atrás dos olhos e tosse", "Suspeita de covid")
medicacao1 = Medicacao("Analgésico", "3 a 5 vezes ao dia", "Paracetamol", "Gripe ou resfriado")
exame1 = Exame("07/02/21", "Ressonancia", "Inflamação no estômago", "Precisa operar urgentemente")
prognosticoT = Prognostico(medicacao1, exame1, "Crônico", "Encaminhado atráves do DrLaureate")
prontuario1 = Prontuario(historico1, anam_paci_T, av_ini_paci_T, prognosticoT)
pacienteT = Paciente("Thales", 23, '123456789', 76, 1.73, 1, "Plano UniRitter Gold" )
medico1 = Medico("Joao", 45, '5423123214', 80, 1.76, 'crm', 'unidade de saude', 'especializacao')
pacienteK = Paciente("Kleyton", 21, '3214123124', 56, 1.62, 2, "Plano UniRitter Platinum" )


#vou fazer depois a opção '1' de cadastrar os pacientes
medico1.inserir_paciente(pacienteT)
medico1.inserir_paciente(pacienteK)

print(medico1.pacientes[0].nome)
paciente_selecionado = medico1.get_paciente(1)
print(medico1.pacientes[paciente_selecionado].nome)

print('Bem-vindo ao sistema X')

menu_inicial = True
while menu_inicial:

    resposta_menu_inicial = input('1 - Cadastrar paciente\n2 - Ver pacientes\n3 - Selecionar paciente cadastrado\n4 - Sair do sistema\nSelecione uma ação: ')
    if resposta_menu_inicial == '1':
        print('\nCadastrando novo paciente...\n')
        medico1.cadastro_paciente()
    elif resposta_menu_inicial == '2':
        medico1.print_pacientes()
    elif resposta_menu_inicial == '3':
        medico1.print_pacientes()
        paciente_selecionado = medico1.get_paciente(medico1.get_id())
        print(medico1.pacientes[paciente_selecionado].nome)
        print(medico1.pacientes[paciente_selecionado].idade)
        print('teste nome: ', medico1.get_nome_paciente(paciente_selecionado))
        menu_paciente = True
        while menu_paciente:
            print('acho q aqui da pra fazer os metodos no paciente\n')
            print('-- Paciente', medico1.get_nome_paciente(paciente_selecionado), '--')
            resposta_menu_paciente = input('\n1 - Ver prontuario\n2 - Adicionar historico\n3 - Adicionar anamnese\n4 - Adicionar avaliacao inicial\n5 - Adicionar prognostico\n6 - Voltar ao menu anterior\n7 - Sair do sistema\nSelecione uma ação: ')
            if resposta_menu_paciente == '1':
                print('mostrar todo prontuario (se o paciente ainda n tiver prontuario (=None) perguntar se gostaria de cadastrar (usar funcao do menu de cadastrar))')
            elif resposta_menu_paciente == '2':
                print('adicionar historico (ver lógica pra quando ainda nao tiver historico (None) e pra quando ja tiver -> concatenar string informada nos atributos, tipo:\nHistorico:\n- Doencas previas:\nCONCATENAR AQUI A STRING\n "adicionar doencas previas" = concatenar string do input no atributo doencas_previas )')
                print('na parte de pegar o input, da pra tentar concatenar uma quebra de linha depois de pegar o input: x = input("digite: ") + "\\n"')
            elif resposta_menu_paciente == '3':
                print('adicionar anamnese')
            elif resposta_menu_paciente == '4':
                print('adicionar avaliacao inicial')
            elif resposta_menu_paciente == '5':
                print('adicionar prognostico')
            elif resposta_menu_paciente == '6':
                print('\nBem-vindo ao sistema X')
                break
            elif resposta_menu_paciente == '7':
                menu_inicial = False
                break
            else:
                print('Input invalido')
        #arrumar
        '''while resposta_id > medico.get_numero_pacientes() or resposta_id < 1:
            resposta_id = int(input('Digite o ID do paciente: '))
        medico1.get_paciente(resposta_id)'''
        # vou fazer aqui o menu de mexer no prontuário do paciente que acabou de ser selecionado
    elif resposta_menu_inicial == '4':
        menu_inicial = False
    else:
        print('input invalido.\n')


