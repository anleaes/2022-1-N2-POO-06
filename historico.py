class Historico:

    def __init__ (self, doenca_previa, doenca_tratada, historico_familiar, grau_parentesco):
        self.doenca_previa = doenca_previa
        self.doenca_tratada = doenca_tratada
        self.historico_familiar = historico_familiar
        self.grau_parentesco = grau_parentesco


    def create_historico(self):
        doenca_previa = input('Informe o campo doenca previa: ')
        doenca_tratada = input('Informe o campo doenca tratada: ')
        historico_familiar = input('Informe o historico familiar: ')
        grau_parentesco = input('Informe o grau de parentesco: ')
        return Historico(doenca_previa, doenca_tratada, historico_familiar, grau_parentesco)

#historicoT = Historico("Câncer de pele", "Cirurgia para remoção - ÊXITO", "Sem histórico", "Nenhum")