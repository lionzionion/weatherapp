import streamlit as st
import requests

def obter_clima(api_key, cidade):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": cidade, "appid": api_key, "units": "metric"}  # Use metric units for temperature in Celsius

    resposta = requests.get(base_url, params=params)
    dados_clima = resposta.json()

    return dados_clima

# Layout do aplicativo Streamlit
st.title("Aplicativo de Clima")

# Opção para permitir que o usuário insira uma cidade personalizada
cidade_customizada = st.text_input("Digite o nome da cidade e pressione Enter")

# Lista de cidades importantes no Brasil
cidades_brasil = [
    "São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza",
    "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Goiânia",
    "Belém", "Porto Alegre", "Campinas", "São Luís", "Natal",
    "João Pessoa", "Teresina", "Campo Grande", "São José dos Campos", "Cuiabá"
]

# Lista de cidades importantes na Europa
cidades_europa = [
    "Paris", "Berlin", "Madrid", "Rome", "London",
    "Amsterdam", "Vienna", "Prague", "Athens", "Stockholm",
    "Oslo", "Copenhagen", "Helsinki", "Warsaw", "Lisbon",
    "Dublin", "Brussels", "Budapest", "Zurich", "Geneva"
]

# Lista de cidades importantes na América do Norte
cidades_america_norte = [
    "New York", "Los Angeles", "Toronto", "Chicago", "Houston",
    "Mexico City", "Miami", "Montreal", "Vancouver", "San Francisco",
    "Seattle", "Boston", "Atlanta", "Dallas", "Denver",
    "Washington, D.C.", "Phoenix", "Las Vegas", "Calgary", "Edmonton"
]

# Permitir que o usuário selecione uma cidade no menu suspenso
continente_selecionado = st.radio("Selecione um Continente", ["Brasil", "Europa", "América do Norte"])

if continente_selecionado == "Brasil":
    cidade_selecionada = st.selectbox("Selecione a Cidade", cidades_brasil)
elif continente_selecionado == "Europa":
    cidade_selecionada = st.selectbox("Selecione a Cidade", cidades_europa)
else:
    cidade_selecionada = st.selectbox("Selecione a Cidade", cidades_america_norte)

# Verificar se o usuário selecionou ou digitou uma cidade
if cidade_selecionada or cidade_customizada:
    if cidade_selecionada:
        cidade = cidade_selecionada
    else:
        cidade = cidade_customizada

    api_key = "edfd3a707801e2659121aef6385e7120"
    informacoes_clima = obter_clima(api_key, cidade)

    # Verificar se a chave 'main' existe na resposta
    if 'main' in informacoes_clima:
        # Exibir informações climáticas de maneira mais organizada
        st.write(f"## Clima em {cidade}")
        st.write(f"**Temperatura Atual:** {informacoes_clima['main']['temp']} °C")  # Display current temperature in Celsius
        st.write(f"**Umidade Atual:** {informacoes_clima['main']['humidity']}%")

        # Exibir ícone do clima com tamanho menor
        st.image(f"http://openweathermap.org/img/wn/{informacoes_clima['weather'][0]['icon']}.png", caption='Ícone do Clima', width=100)

        st.write(f"**Descrição Atual:** {informacoes_clima['weather'][0]['description'].capitalize()}")

        # Opcional: Exibir detalhes adicionais
        st.subheader("Detalhes Adicionais")
        st.write(f"**Pressão Atual:** {informacoes_clima['main']['pressure']} hPa")
        st.write(f"**Velocidade do Vento Atual:** {informacoes_clima['wind']['speed']} m/s")
    else:
        st.warning(f"Erro ao obter dados climáticos. Resposta: {informacoes_clima}")
else:
    st.warning("Por favor, selecione ou digite uma cidade.")
