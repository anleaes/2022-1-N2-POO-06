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
pacienteT = Paciente("Thales", 23, '123456789', 76, 1.73, prontuario1, 1, "Plano UniRitter Gold" )
medico1 = Medico("Joao", 45, '5423123214', 80, 1.76, 'crm', 'unidade de saude', 'especializacao')
pacienteK = Paciente("Kleyton", 21, '3214123124', 56, 1.62, prontuario1, 2, "Plano UniRitter Platinum" )


#vou fazer depois a opção '1' de cadastrar os pacientes
medico1.inserir_paciente(pacienteT)
medico1.inserir_paciente(pacienteK)



print('Bem-vindo ao sistema X')

menu_inicial = True
while menu_inicial:

    resposta_menu_inicial = input('1 - Cadastrar paciente\n2 - Ver pacientes\n3 - Selecionar paciente cadastrado\n4 - Sair do sistema\nSelecione uma ação: ')
    if resposta_menu_inicial == '1':
        print('aqui vai a parte de cadastrar um paciente')
    elif resposta_menu_inicial == '2':
        medico1.print_pacientes()
    elif resposta_menu_inicial == '3':
        medico1.print_pacientes()
        resposta_id = 99 #solução paliativa, depois arrumo
        while resposta_id > medico1.get_numero_pacientes() or resposta_id < 1:
            resposta_id = int(input('Digite o ID do paciente: '))
            if resposta_id > medico1.get_numero_pacientes() or resposta_id < 1:
                print('Input invalido.')
        medico1.get_paciente(resposta_id)
        # vou fazer aqui o menu de mexer no prontuário do paciente que acabou de ser selecionado
    elif resposta_menu_inicial == '4':
        menu_inicial = False
    else:
        print('input invalido.\n')


