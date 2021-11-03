
from GrupoParlamentario.GrupoParl import GrupoParl

class Votacion:
    data      = None

    sesion    = 0
    nVotacion = 0
    fecha     = ""
    titulo    = ""
    textoExp  = ""

    resultado = "" # "Si" o "No"
    presentes = 0

    votosAgregados = {'Sí'          : 0,
                      'No'          : 0,
                      'Abstención'  : 0,
                      'No vota'     : 0}

    grupos    = {} # nombre : objeto


    def __init__(self, data):
        self.data      = data
        self.sesion    = data['informacion']['sesion']
        self.nVotacion = data['informacion']['numeroVotacion']
        self.fecha     = data['informacion']['fecha']
        self.titulo    = data['informacion']['titulo']
        self.textoExp  = data['informacion']['textoExpediente']

        self.resultado = data['totales']['asentimiento']
        self.presentes = data['totales']['presentes']

        self.votosAgregados['Sí']         = data['totales']['afavor']
        self.votosAgregados['No']         = data['totales']['enContra']
        self.votosAgregados['Abstención'] = data['totales']['abstenciones']
        self.votosAgregados['No vota']    = data['totales']['noVotan']

        self.parseVot()


    def parseVot(self):
        for voto in self.data['votaciones']:
            if voto['grupo'] not in self.grupos:
                self.grupos[voto['grupo']] = GrupoParl(voto['grupo'])

            # self.grupos[voto['grupo']].aggregate(voto)
            grupo = self.grupos[voto['grupo']]
            grupo.aggregate(voto)
