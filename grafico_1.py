import matplotlib.pyplot as plt
import pandas as pd

    # PRIMEIRO GRÁFICO:    

read = pd.read_csv("a2_MANCHAS.csv")

plt.title('Número de manchas solares de Wolfer;\n observações anuais de 1749 a 1924.', color = 'Red')
plt.plot(read['Ano'], read['manchas'], color = 'Red')
plt.xlabel('Ano', color = 'Red')
plt.ylabel('Manchas(Wolfer)', color = 'Red')
plt.xticks(rotation = 90)
plt.grid(True)

plt.savefig('primeiro_grafico.png')

plt.show()
