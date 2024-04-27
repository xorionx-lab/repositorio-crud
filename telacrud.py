import streamlit as st
st.header("---------")
st.title("PROJETO")
st.write("olá mundo")
escolha = st.selectbox('Selecione o turno', ['manhã', 'tarde', 'noite'])
#Textos renderizados

if escolha:
    st.write(escolha)
radio = st.radio('Selecione uma opção:', ['manhã', 'tarde', 'noite'])

texto = st.text_input('Digite seu nome: ')
numerico = st.number_input('Digite um número: ')
if texto and numerico:
    st.write(texto, numerico)

cpf = st.text_input('Digite seu cpf:', placeholder='000.000.000-00')

btncadastrar = st.button('cadastrar')
st.write(btncadastrar)

textolongo = st.text_area('Digite sua reclamação: ')
btnenviar = st.button('enviar')
st.write(btnenviar)