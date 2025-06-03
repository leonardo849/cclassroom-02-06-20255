class Nota:
    def __init__(self, nota, quantidade):
        self.nota = nota
        self.quantidade = quantidade
    def __repr__(self):
        return f"nota {self.nota} quantidade {self.quantidade}"
    def __str__(self):
        return f"nota {self.nota} quantidade {self.quantidade}"