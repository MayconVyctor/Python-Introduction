class Tarefa:
    def __init__(self, nome, descricao, horario):
        self.nome = nome
        self.descricao = descricao
        self.horario = horario

    def mostrarTarefas(self):
       print(f"Tarefa: {self.nome}\nDescricao: {self.descricao}\nHorario: {self.horario}\n")

class ToDoList:
   def __init__(self, tarefas):
      self.tarefas = []


   def adicionarTarefa(self, tarefa):
        self.tarefas.append(tarefa)


   def exibirTarefas(self):
        for tarefa in self.tarefas:
            tarefa.mostrarTarefas()

   def removerTarefa(self, tarefa):
       self.tarefas.remove(tarefa)

Tarefa1 = Tarefa("Jogar Volei", "Treino de volei, quadra principal", "19:30h")

Tarefa2 = Tarefa("Academia", "Treino de Costas/Biceps", "17h")

Tarefas = ToDoList([])

Tarefas.adicionarTarefa(Tarefa1)
Tarefas.adicionarTarefa(Tarefa2)

#Tarefas.removerTarefa(Tarefa2)
Tarefas.exibirTarefas()