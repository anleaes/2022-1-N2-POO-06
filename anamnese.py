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


#anam_paci_T = Anamnese("Vigil", "Perda de memória recente", "Raiva e agressividade" ,"Fala em alto volume e com rapidez")