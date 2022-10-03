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
        self.resultadoVotacion()
        self.votosCadaGrupo()

        self.showCharts()


    def resultadoVotacion(self):
        titulo    = "Resultados de la votación"
        agregados = self.votacion.votosAgregados
        l, s, c   = Utils.lbcFilter(agregados)
        Utils.createPieChart(l, s, c, titulo)


    def votosCadaGrupo(self):
        nfil, ncol, pos = 4, 3, 0
        fig, ax = plt.subplots(4, 3)
        for grupo in self.votacion.grupos:
            fila = (pos // ncol)
            col  = (pos % ncol)
            l, s, c, t = self.votosDelGrupo(grupo)
            ax[fila, col].pie(s, labels=l, autopct='%1.1f%%',
                              colors=c, startangle=180)
            ax[fila, col].set_title(grupo)
            pos += 1
        
        for i in range(pos, (nfil * ncol)):
            fila = (i // ncol)
            col  = (i % ncol)
            ax[fila, col].axis('off') # Empty figure 
        
        plt.gcf().canvas.manager.set_window_title("Votos de cada grupo")
        plt.gcf().set_size_inches(8, 8)



    def votosDelGrupo(self, grupo, show=False):
        titulo    = "Votos del grupo " + grupo
        agregados = self.votacion.grupos[grupo].votosAgregados
        l, s, c   = Utils.lbcFilter(agregados)
        if show == True:
            Utils.createPieChart(l, s, c, titulo)
        return l, s, c, titulo

    # Para un tipo de voto -> "sí, no, abstención o no vota"
    def repartoVoto(self, tipoVoto):
        titulo = "Reparto de votos '{}'".format(tipoVoto)
        agregados = {}
        grupos = self.votacion.grupos
        for grupo in grupos:
            agregados[grupo] = grupos[grupo].votosAgregados[tipoVoto]
        l, s, c = Utils.lbcFilter(agregados, color='partidos')
        return [l, s, c]


    def showCharts(self):
        plt.tight_layout()
        plt.show()
