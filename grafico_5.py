import matplotlib.pyplot as plt
import pandas as pd
    
    # 30 primeiros resultados:

read = pd.read_csv("a2_MANCHAS.csv").iloc[0:30]

plt.title('Número de manchas solares de Wolfer;\n 30 primeiros resultados:', color = 'Black')
plt.plot(read['Ano'], read['manchas'], color = 'Y')
plt.xlabel('Ano', color = 'Black')
plt.ylabel('Manchas', color = 'Black')
plt.xticks(rotation = 90)
plt.grid(True)

plt.savefig('quinto_grafico.png')

plt.show()
