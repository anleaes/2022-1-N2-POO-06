class Exame:

    def __init__ (self, data, tipo, resultado, avaliacao):
        self.data = data
        self.tipo = tipo
        self.resultado = resultado
        self.avaliacao = avaliacao

    def create_exame(self):
        print('== EXAME ==')
        data = input('Informe o campo data: ')
        tipo = input('Informe o campo tipo: ')
        resultado = input('Informe o campo resultado: ')
        avaliacao = input('Informe o campo avaliacao: ')
        return Exame(data, tipo, resultado, avaliacao)


#exame1 = Exame("07/02/21", "Ressonancia", "Inflamação no estômago", "Precisa operar urgentemente")