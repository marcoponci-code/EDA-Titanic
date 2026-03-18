# 🚢 Análise Exploratória de Dados com Python – Dataset Titanic

Este projeto foi desenvolvido como exercício prático de **Análise Exploratória de Dados (EDA)** utilizando Python. A análise utiliza uma base de dados com informações de passageiros do **Titanic**, permitindo explorar técnicas fundamentais de **manipulação de dados, estatística descritiva e visualização**.

O objetivo é demonstrar um fluxo básico de trabalho utilizado por **Analistas de Dados**, desde a importação da base até a geração de gráficos e estatísticas que ajudam a compreender padrões e relações entre variáveis.

---

# 📊 Objetivos do projeto

- Explorar a estrutura de um dataset real
- Aplicar técnicas de **limpeza e preparação de dados**
- Realizar **estatísticas descritivas**
- Criar **visualizações para análise exploratória**
- Praticar comandos importantes das bibliotecas **Pandas, NumPy, Matplotlib e Seaborn**

---

# 📚 Bibliotecas utilizadas

### numpy (np)
Biblioteca fundamental para computação numérica em Python.

Principais usos no projeto:
- Operações matemáticas
- Manipulação de arrays
- Criação de intervalos numéricos (`np.arange()`)

---

### pandas (pd)
Principal biblioteca para **manipulação e análise de dados estruturados**.

Utilizada para:

- Importação de arquivos
- Criação de **Series** e **DataFrames**
- Seleção e filtragem de dados
- Limpeza e tratamento de valores ausentes
- Estatísticas descritivas
- Agrupamento de dados

---

### matplotlib.pyplot (plt)
Biblioteca base para criação de gráficos em Python.

Utilizada para:
- Configuração de figuras
- Controle de tamanho e resolução
- Exibição dos gráficos

---

### seaborn (sns)
Biblioteca de visualização estatística baseada no Matplotlib.

Permite criar gráficos mais sofisticados e apropriados para **análise de dados**.

---

# 📂 Importação dos dados

O projeto demonstra como trabalhar com diferentes formatos de arquivos.

### Excel
```python
titanic = pd.read_excel('titanic.xlsx')
