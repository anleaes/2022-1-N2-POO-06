class AvaliacaoInicial:

    def __init__ (self, queixa, data_inicio, sintomas, avaliacao):
        self.queixa = queixa
        self.data_inicio = data_inicio
        self.sintomas = sintomas
        self.avaliacao = avaliacao


    def create_avaliacao_inicial(self):
        queixa = input('Informe o campo queixa: ')
        data_inicio = input('Informe o campo data_inicio: ')
        sintomas = input('Informe o campo sintomas: ')
        avaliacao = input('Informe o campo avaliacao: ')
        return AvaliacaoInicial(queixa, data_inicio, sintomas, avaliacao)

    def adicionar_a_avaliacao_inicial(self):
        self.queixa += '\n- ' + input("Informe queixa que deseja adicionar ao prontuario: ")
        self.data_inicio += '\n- ' + input("Informe a data de inicio que deseja adicionar ao prontuario: ")
        self.sintomas += '\n- ' + input("Informe sintomas que deseja adicionar ao prontuario: ")
        self.avaliacao += '\n- ' + input("Informe a avaliacao que deseja adicionar ao prontuario: ")
    

    def print_avaliacao_inicial(self):
        print('\t== AVALIACAO INICIAL ==')
        print(f'\nQueixa:\n- {self.queixa}')
        print(f'\nData inicio:\n- {self.data_inicio}')
        print(f'\nSintomas:\n- {self.sintomas}')
        print(f'\nAvaliacao:\n- {self.avaliacao}')
        


#av_ini_paci_T = AvaliacaoInicial("Dores de cabeça", "07/06/22", "Febre, dor atrás dos olhos e tosse", "Suspeita de covid")

