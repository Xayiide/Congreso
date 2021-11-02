

class GrupoParl:
    nombre         = ""
    diputadoVota   = None
    votosAgregados = None

    def __init__(self, nombre):
        self.nombre = nombre
        self.diputadoVota = {}
        self.votosAgregados = {'Sí'         : 0,
                               'No'         : 0,
                               'Abstención' : 0,
                               'No vota'    : 0}

    def aggregate(self, voto):
        self.diputadoVota[voto['diputado']] = voto['voto']
        self.votosAgregados[voto['voto']] += 1

    
    def imprimir(self):
        print("\n ============================= \n" * 2)
        print(self.nombre)
        print(self.diputadoVota)
        print("\n" * 3)
        print(self.votosAgregados)