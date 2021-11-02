

class Votacion:
    data      = None

    sesion    = 0
    nVotacion = 0
    fecha     = ""
    titulo    = ""
    textoExp  = ""

    resultado = "" # "Si" o "No"
    presentes = 0
    aFavor    = 0
    enContra  = 0
    absten    = 0
    noVota    = 0

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
        self.aFavor    = data['totales']['afavor']
        self.enContra  = data['totales']['enContra']
        self.absten    = data['totales']['abstenciones']
        self.noVota    = data['totales']['noVotan']

        self.parseVot()
        for grupo in self.grupos.values():
            grupo.imprimir()

    def parseVot(self):
        for voto in self.data['votaciones']:
            if voto['grupo'] not in self.grupos:
                self.grupos[voto['grupo']] = GrupoParl(voto['grupo'])

            # self.grupos[voto['grupo']].aggregate(voto)
            grupo = self.grupos[voto['grupo']]
            grupo.aggregate(voto)
