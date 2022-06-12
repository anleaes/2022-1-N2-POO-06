class Anamnese:

    def __init__ (self, nivel_consciencia, estado_cognitivo, humor_afeto, linguagem):
        self.nivel_consciencia = nivel_consciencia
        self.estado_cognitivo = estado_cognitivo
        self.humor_afeto = humor_afeto
        self.linguagem = linguagem

    def create_anamnese(self):
        nivel_consciencia = input('Informe o campo nivel de consciencia: ')
        estado_cognitivo = input('Informe o campo estado cognitivo: ')
        humor_afeto = input('Informe o campo humor_afeto: ')
        linguagem = input('Informe o campo linguagem: ')
        return Anamnese(nivel_consciencia, estado_cognitivo, humor_afeto, linguagem)

    def adicionar_a_anamnese(self):
        self.nivel_consciencia += '\n- ' + input("Informe o campo nivel de consciencia que deseja adicionar ao prontuario: ")
        self.estado_cognitivo += '\n- ' + input("Informe o campo doenca tratada que deseja adicionar ao prontuario: ")
        self.humor_afeto += '\n- ' + input("Informe o historico familiar que deseja adicionar ao prontuario: ")
        self.linguagem += '\n- ' + input("Informe o grau de parentesco que deseja adicionar ao prontuario: ")
        

    def print_anamnese(self):
        print('\t== ANAMNESE ==')
        print(f'\nNivel consciencia:\n- {self.nivel_consciencia}')
        print(f'\nEstado cognitivo:\n- {self.estado_cognitivo}')
        print(f'\nHumor afeto:\n- {self.humor_afeto}')
        print(f'\nLinguagem:\n- {self.linguagem}')


#anam_paci_T = Anamnese("Vigil", "Perda de memória recente", "Raiva e agressividade" ,"Fala em alto volume e com rapidez")