import matplotlib.pyplot as plt


resColors = {'Sí'        : '#6EEB83',
             'No'        : '#FF5714',
             'Abstención': '#767676',
             'No vota'   : '#DCDCDC'}

# Provisional
gpColors = {'GP'   : '#1D84CE',
            'GS'   : '#DC0000',
            'GVOX' : '#63BE21',
            'GPlu' : '#DCDCDC',
            'GCs'  : '#EB6109'}


def lbcFilter(agregados, color=None):
    palette = resColors
    if color == 'partido':
        palette = gpColors

    labels, sizes, colors = [], [], []
    auxlabels = []
    for voto in agregados:
        if agregados[voto] != 0:
            auxlabels.append(str(voto))
            sizes.append(agregados[voto])

    for i, auxlabel in enumerate(auxlabels):
        colors.append(palette[auxlabel])
        num = agregados[auxlabel]
        labels.append(str(auxlabel + " [" + str(num) + "]"))

    return labels, sizes, colors


def createPieChart(labels, sizes, colors, titulo):
    f, a = plt.subplots()
    a.pie(sizes, labels=labels, autopct='%1.1f%%',
          colors=colors, startangle=180)
    
    donut = plt.Circle((0, 0), 0.70, fc='white')
    _ = plt.gcf().gca().add_artist(donut)
    plt.gcf().canvas.manager.set_window_title(titulo)

    a.axis('equal')

    return a
