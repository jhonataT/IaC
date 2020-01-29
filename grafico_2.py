import matplotlib.pyplot as plt
import pandas as pd

    # SEGUNDO GRÁFICO (10 PRIMEIROS RESULTADOS):

read = pd.read_csv("a2_MANCHAS.csv").iloc[0:10]

plt.title('Número de manchas solares de Wolfer;\n 10 primeiros resultados:', color = 'Green')
plt.plot(read['Ano'], read['manchas'], color = 'Green')
plt.xlabel('Ano', color = 'Green')
plt.ylabel('Manchas', color = 'Green')
plt.xticks(rotation = 90)
plt.grid(True)

plt.savefig('segundo_grafico.png')

plt.show()
