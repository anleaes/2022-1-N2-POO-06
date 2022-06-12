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

    def adicionar_ao_historico(self):
        self.doenca_previa += '\n- ' + input("Informe doenca previa que deseja adicionar ao prontuario: ")
        self.doenca_tratada += '\n- ' + input("Informe o campo doenca tratada que deseja adicionar ao prontuario: ")
        self.historico_familiar += '\n- ' + input("Informe o historico familiar que deseja adicionar ao prontuario: ")
        self.grau_parentesco += '\n- ' + input("Informe o grau de parentesco que deseja adicionar ao prontuario: ")
        

    def print_historico(self):
        print('\t== HISTORICO ==')
        print(f'\nDoenca previa:\n- {self.doenca_previa}')
        print(f'\nDoenca tratada:\n- {self.doenca_tratada}')
        print(f'\nHistorico familiar:\n- {self.historico_familiar}')
        print(f'\nGrau parentesco:\n- {self.grau_parentesco}')
        

#historicoT = Historico("Câncer de pele", "Cirurgia para remoção - ÊXITO", "Sem histórico", "Nenhum")