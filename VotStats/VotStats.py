import json
import matplotlib.pyplot as plt


class VotStats:
    file     = None
    data     = None
    votacion = None

    pieVotRes = None
    pieVotSiPorGrupo = None

    def __init__(self, filename):
        self.file      = open(filename, 'r')
        self.data      = json.load(self.file)
        self.votacion  = Votacion(self.data)
        self.pieVotRes = self.votResultados()
        self.pieVotSiPorGrupo = self.votosSiPorGrupo()

        self.showCharts()

    def votResultados(self):
        labels = ('Sí [{}]'.format(self.votacion.aFavor),
                  'No [{}]'.format(self.votacion.enContra),
                  'Abstención [{}]'.format(self.votacion.absten),
                  'No vota [{}]'.format(self.votacion.noVota))
        sizes  = [self.votacion.aFavor,
                  self.votacion.enContra,
                  self.votacion.absten,
                  self.votacion.noVota]
        colors = ['#6eeb83', '#FF5714', '#b6b5b5', '#272727']

        # TODO: Maybe call generic Utils function to render pie charts
        f, a = plt.subplots()
        a.pie(sizes, labels=labels, autopct='%1.1f%%',
              colors=colors, startangle=180)

        donut = plt.Circle((0,0), 0.70, fc='white')
        _ = plt.gcf().gca().add_artist(donut)

        a.axis('equal')

        return a

    def votosSiPorGrupo(self):
        grupo = self.votacion.grupos
        grupo = grupo['GP']
        labels = ('Sí [{}]'.format(grupo.votosAgregados['Sí']),
                  'No [{}]'.format(grupo.votosAgregados['No']),
                  'Abstención [{}]'.format(grupo.votosAgregados['Abstención']),
                  'No vota [{}]'.format(grupo.votosAgregados['No vota']))
        sizes = [grupo.votosAgregados['Sí'],
                 grupo.votosAgregados['No'],
                 grupo.votosAgregados['Abstención'],
                 grupo.votosAgregados['No vota']]
        colors = ['#6eeb83', '#FF5714', '#b6b5b5', '#272727']

        # TODO: Maybe call generic Utils function to render pie charts
        f, a = plt.subplots()
        a.pie(sizes, labels=labels, autopct='%1.1f%%',
              colors=colors, startangle=180)

        donut = plt.Circle((0,0), 0.70, fc='white')
        _ = plt.gcf().gca().add_artist(donut)

        a.axis('equal')

        return a

    def showCharts(self):
        plt.tight_layout()
        plt.show()