class Pacientes:

    def __init__(self, medico):
        self.medico = medico
        self.pacientes = []
    

    def inserir_paciente(self, paciente):
        self.pacientes.append(paciente)
    
    def get_pacientes(self):
        for paciente in self.pacientes:
            return paciente.id, paciente.pessoa.nome

    
