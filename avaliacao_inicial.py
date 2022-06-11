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

#av_ini_paci_T = AvaliacaoInicial("Dores de cabeça", "07/06/22", "Febre, dor atrás dos olhos e tosse", "Suspeita de covid")

