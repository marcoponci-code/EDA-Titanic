import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Dashboard Titanic", layout="wide")

# Título e Autor
st.title("🚢 Titanic Dataset - Exploratory Data Analysis")
st.markdown("Autor: **Marco Antonio Ponciano**")

# Carregamento dos dados
@st.cache_data # Cache para não ler o arquivo toda hora
def load_data():
    df = pd.read_excel("titanic.xlsx")
    return df

try:
    titanic = load_data()

    # Sidebar - Filtros
    st.sidebar.header("Filtros")
    sexo_selecionado = st.sidebar.multiselect(
        "Selecione o Sexo:", 
        options=titanic["sexo"].unique(), 
        default=titanic["sexo"].unique()
    )

    # Filtrando o dataframe com base na sidebar
    df_filtrado = titanic[titanic["sexo"].isin(sexo_selecionado)]

    # --- MÉTRICAS PRINCIPAIS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Passageiros", len(df_filtrado))
    
    sobreviventes_pct = (df_filtrado["sobreviveu"] == "sim").mean() * 100
    col2.metric("Taxa de Sobrevivência", f"{sobreviventes_pct:.1f}%")
    
    idade_media = df_filtrado["idade"].mean()
    col3.metric("Idade Média", f"{idade_media:.1f} anos")

    st.divider()

    # --- GRÁFICOS ---
    tab1, tab2, tab3 = st.tabs(["Distribuição", "Sobrevivência", "Estatísticas"])

    with tab1:
        st.subheader("Distribuição de Idade e Tarifas")
        fig1, ax1 = plt.subplots(1, 2, figsize=(12, 4))
        
        sns.histplot(data=df_filtrado, x="idade", bins=20, kde=True, ax=ax1[0], color="skyblue")
        ax1[0].set_title("Distribuição de Idade")
        
        sns.scatterplot(data=df_filtrado[df_filtrado["valor_tarifa"] < 100], 
                        x="idade", y="valor_tarifa", hue="classe", ax=ax1[1])
        ax1[1].set_title("Idade vs Tarifa (até $100)")
        
        st.pyplot(fig1)

    with tab2:
        st.subheader("Análise de Sobrevivência")
        fig2, ax2 = plt.subplots(1, 2, figsize=(12, 4))
        
        sns.countplot(data=df_filtrado, x="sobreviveu", ax=ax2[0], palette="viridis")
        ax2[0].set_title("Contagem Geral")
        
        sns.countplot(data=df_filtrado, x="sobreviveu", hue="classe", ax=ax2[1])
        ax2[1].set_title("Sobrevivência por Classe")
        
        st.pyplot(fig2)

    with tab3:
        st.subheader("Dados Brutos e Resumo")
        st.write(df_filtrado.describe())
        if st.checkbox("Mostrar dados brutos"):
            st.dataframe(df_filtrado)

except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
    st.info("Certifique-se de que o arquivo 'titanic.xlsx' está na mesma pasta que este script.")