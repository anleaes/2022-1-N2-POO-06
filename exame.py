class Exame:

    def __init__ (self, data, tipo, resultado, avaliacao):
        self.data = data
        self.tipo = tipo
        self.resultado = resultado
        self.avaliacao = avaliacao


    def adicionar_ao_exame(self):
        print('== EXAME ==')
        self.data += '\n- ' + input("Informe data que deseja adicionar ao prontuario: ")
        self.tipo += '\n- ' + input("Informe tipo que deseja adicionar ao prontuario: ")
        self.resultado += '\n- ' + input("Informe resultado que deseja adicionar ao prontuario: ")
        self.avaliacao += '\n- ' + input("Informe avaliacao que deseja adicionar ao prontuario: ")

    def print_exame(self):
        print('== EXAME == ')
        print(f'\nData:\n- {self.data}')
        print(f'\nTipo:\n- {self.tipo}')
        print(f'\nresultado:\n- {self.resultado}')
        print(f'\navaliacao:\n- {self.avaliacao}')
    

#objeto teste:
#exame1 = Exame("07/02/21", "Ressonancia", "Inflamação no estômago", "Precisa operar urgentemente")