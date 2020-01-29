import matplotlib.pyplot as plt
import pandas as pd

    # TERCEIRO GRÁFICO (10 ULTIMOS RESULTADOS):

read = pd.read_csv("a2_MANCHAS.csv").iloc[166:]

plt.title('Número de manchas solares de Wolfer;\n 10 ultimos resultados:', color = 'Blue')
plt.plot(read['Ano'], read['manchas'], color = 'Blue')
plt.xlabel('Ano', color = 'blue')
plt.ylabel('Manchas', color = 'blue')
plt.xticks(rotation = 90)
plt.grid(b = True)

plt.savefig('terceiro_grafico.png')

plt.show()