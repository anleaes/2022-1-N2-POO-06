class Prontuario: 

    def __init__(self, paciente, historico, anamnese, avalicaoinicial, prognostico):
        self.paciente = paciente
        self.historico = historico
        self.anamnese = anamnese
        self.avaliacao_inicial = avalicaoinicial
        self.prognostico = prognostico
    

    def print_prontuario(self):
        self.historico.print_historico()
        self.anamnese.print_anamnese()
        self.avaliacao_inicial.print_avaliacao_inicial()
        self.prognostico.print_prognostico()


#objeto teste
#prontuario1 = Prontuario(pacienteT, historico1, anam_paci_T, av_ini_paci_T, prognosticoT)
        