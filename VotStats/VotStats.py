import json
import matplotlib.pyplot as plt

from Votacion.Votacion import Votacion
import Utils.Utils as Utils

class VotStats:
    file     = None
    data     = None
    votacion = None

    pieVotRes        = None
    pieVotPorGrupo = None


    def __init__(self, filename):
        self.file      = open(filename, 'r')
        self.data      = json.load(self.file)
        self.votacion  = Votacion(self.data)
        self.votResultados()
        self.votosPorGrupo()
        self.votSiPorGrupo()
        self.votNoPorGrupo()
        self.votAbsPorGrupo()
        self.votNovPorGrupo()


        self.showCharts()


    def votResultados(self):
        titulo    = "Resultados de la votación"
        agregados = self.votacion.votosAgregados
        print(agregados)
        labels, sizes, colors = Utils.lbcFilter(agregados)
        return Utils.createPieChart(labels, sizes, colors, titulo)


    def votosPorGrupo(self):
        grupos = self.votacion.grupos
        for grupo in grupos:
            titulo = "Votos del grupo " + grupo
            agregados = grupos[grupo].votosAgregados
            labels, sizes, colors = Utils.lbcFilter(agregados)
            Utils.createPieChart(labels, sizes, colors, titulo)


    def votSiPorGrupo(self):
        gps = ['GP', 'GS', 'GVOX', 'GPlu', 'GCs']
        for p in gps:
            grupo = self.votacion.grupos[p]


    
    def votNoPorGrupo(self):
        pass

    def votAbsPorGrupo(self):
        pass
    
    def votNovPorGrupo(self):
        pass

    def showCharts(self):
        plt.tight_layout()
        plt.show()
