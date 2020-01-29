    # Séries A2 (Manchas): Número de manchas solares de Wolfer; observações anuais de 1749 a 1924.

import matplotlib.pyplot as plt
import pandas as pd

    # PRIMEIRO GRÁFICO:    

read = pd.read_csv("a2_MANCHAS.csv")

plt.title('Número de manchas solares de Wolfer;\n observações anuais de 1749 a 1924.', color = 'Red')
plt.plot(read['Ano'], read['manchas'], color = 'Red')
plt.xlabel('Ano'    , color = 'Red')
plt.xticks(rotation = 90)
plt.ylabel('Manchas(Wolfer)', color = 'Red')
plt.yticks(rotation = 50)
plt.grid(True)

#plt.savefig('primeiro_grafico.png')
plt.savefig("primeiro_grafico.png")

plt.show()


    # SEGUNDO GRÁFICO (10 PRIMEIROS RESULTADOS):

read = pd.read_csv("a2_MANCHAS.csv").iloc[0:10]

plt.title('Número de manchas solares de Wolfer;\n 10 primeiros resultados:', color = 'Green')
plt.plot(read['Ano'], read['manchas'], color = 'Green')
plt.xlabel('Ano', color = 'Green')
plt.xticks(rotation = 90)
plt.ylabel('Manchas(Wolfer)', color = 'Green')
plt.yticks(rotation = 50)
plt.grid(True)

plt.savefig('segundo_grafico.png')

plt.show()


    # TERCEIRO GRÁFICO (10 ULTIMOS RESULTADOS):

read = pd.read_csv("a2_MANCHAS.csv").iloc[166:]

plt.title('Número de manchas solares de Wolfer;\n 10 ultimos resultados:', color = 'Blue')
plt.plot(read['Ano'], read['manchas'], color = 'Blue')
plt.xlabel('Ano', color = 'blue')
plt.xticks(rotation = 90)
plt.ylabel('Manchas(Wolfer)', color = 'blue')
plt.yticks(rotation = 50)
plt.grid(True)

plt.savefig('terceiro_grafico.png')

plt.show()


    #  BOXPLOT DOS DADOS:

read = pd.read_csv("a2_MANCHAS.csv")

plt.title('Número de manchas solares de Wolfer;\n', color = 'Black')
plt.ylabel('Manchas(Wolfer)')
read.boxplot(column = 'manchas')
plt.grid(True)

plt.savefig('quarto_grafico.png')

plt.show()


    # 30 primeiros resultados:

read = pd.read_csv("a2_MANCHAS.csv").iloc[0:30]

plt.title('Número de manchas solares de Wolfer;\n 30 primeiros resultados:', color = 'Black')
plt.plot(read['Ano'], read['manchas'], color = 'Y')
plt.xlabel('Ano', color = 'Black')
plt.xticks(rotation = 90)
plt.ylabel('Manchas(Wolfer)', color = 'Black')
plt.yticks(rotation = 50)
plt.grid(True)

plt.savefig('quinto_grafico.png')

plt.show()
