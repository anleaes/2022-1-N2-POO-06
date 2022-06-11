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


historico1 = Historico("Câncer de pele", "Cirurgia para remoção - ÊXITO", "Sem histórico", "Nenhum")
anam_paci_T = Anamnese("Vigil", "Perda de memória recente", "Raiva e agressividade" ,"Fala em alto volume e com rapidez")
av_ini_paci_T = AvaliacaoInicial("Dores de cabeça", "07/06/22", "Febre, dor atrás dos olhos e tosse", "Suspeita de covid")
medicacao1 = Medicacao("Analgésico", "3 a 5 vezes ao dia", "Paracetamol", "Gripe ou resfriado")
exame1 = Exame("07/02/21", "Ressonancia", "Inflamação no estômago", "Precisa operar urgentemente")
prognosticoT = Prognostico(medicacao1, exame1, "Crônico", "Encaminhado atráves do DrLaureate")
pacienteT = Paciente("Thales", 23, '123456789', 76, 1.73, 1, "Plano UniRitter Gold" )
prontuario1 = Prontuario(pacienteT, historico1, anam_paci_T, av_ini_paci_T, prognosticoT)
medico1 = Medico("Joao", 45, '5423123214', 80, 1.76, 'crm', 'unidade de saude', 'especializacao')
pacienteK = Paciente("Kleyton", 21, '3214123124', 56, 1.62, 2, "Plano UniRitter Platinum" )

cadastro1 = Cadastro(medico1)
medico1.adicionar_cadastro(cadastro1)
pacienteT.prontuario = prontuario1

#vou fazer depois a opção '1' de cadastrar os pacientes
#medico1.inserir_paciente(pacienteT)
#medico1.inserir_paciente(pacienteK)
cadastro1.inserir_paciente(pacienteT)
cadastro1.inserir_paciente(pacienteK)



cadastro1.print_pacientes_cadastrados()
print('Bem-vindo ao sistema X')

menu_inicial = True
while menu_inicial:

    resposta_menu_inicial = input('1 - Cadastrar paciente\n2 - Ver pacientes\n3 - Selecionar paciente cadastrado\n4 - Sair do sistema\nSelecione uma ação: ')
    if resposta_menu_inicial == '1':
        print('\nCadastrando novo paciente...\n')
        cadastro1.cadastrar_paciente()
    elif resposta_menu_inicial == '2':
        cadastro1.print_pacientes_cadastrados()
    elif resposta_menu_inicial == '3':
        cadastro1.print_pacientes_cadastrados()
        id_paciente_selecionado = medico1.get_id()
        paciente_selecionado = medico1.get_paciente(id_paciente_selecionado)
        print(paciente_selecionado.nome)
        print(paciente_selecionado.idade)
        print('teste nome: ', medico1.get_nome_paciente(paciente_selecionado))
        menu_paciente = True
        while menu_paciente:
            print('acho q aqui da pra fazer os metodos no paciente\n')
            print('-- Paciente', medico1.get_nome_paciente(paciente_selecionado), '--')
            resposta_menu_paciente = input('\n1 - Cadastrar prontuario do paciente\n2 - Ver prontuario\n3 - Adicionar historico\n4 - Adicionar anamnese\n5 - Adicionar avaliacao inicial\n6 - Adicionar prognostico\n7 - Voltar ao menu anterior\n8 - Sair do sistema\nSelecione uma ação: ')
            if resposta_menu_paciente == '1':
                print('\nCadastrando prontuario do paciente...\n')
                cadastro1.cadastrar_prontuario(paciente_selecionado)
                print('paciente. prontuario: ', paciente_selecionado.prontuario)
                print('paciente historico: ', paciente_selecionado.prontuario.historico)
                print('paciente historico doenca previa: ', paciente_selecionado.prontuario.historico.doenca_previa)
                #print(paciente_selecionado.prontuario.historico.grau_parentesco)
            elif resposta_menu_paciente == '2':
                if paciente_selecionado.prontuario == None:
                    print('Paciente selecionado ainda nao possui prontuario cadastrado\nDeve ser feito o cadastro para prosseguir:')
                    paciente_selecionado.cadastrar_prontuario()
                print('mostrar todo prontuario (se o paciente ainda n tiver prontuario (=None) perguntar se gostaria de cadastrar (usar funcao do menu de cadastrar))')
                print('teste prontuario: ')
                print('teste print historico:')
                paciente_selecionado.print_teste()
            elif resposta_menu_paciente == '3':
                print('adicionar historico (ver lógica pra quando ainda nao tiver historico (None) e pra quando ja tiver -> concatenar string informada nos atributos, tipo:\nHistorico:\n- Doencas previas:\nCONCATENAR AQUI A STRING\n "adicionar doencas previas" = concatenar string do input no atributo doencas_previas )')
                print('na parte de pegar o input, da pra tentar concatenar uma quebra de linha depois de pegar o input: x = input("digite: ") + "\\n"')
            elif resposta_menu_paciente == '4':
                print('adicionar anamnese')
            elif resposta_menu_paciente == '5':
                print('adicionar avaliacao inicial')
            elif resposta_menu_paciente == '6':
                print('adicionar prognostico')
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


