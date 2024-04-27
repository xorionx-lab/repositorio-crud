import streamlit as st
from funcoesCrud import *


st.title("DnsLTDA")
st.header("Sistema de produtos")
st.markdown("## Cadastro produtos")
st.write("Aqui é um treino de sistemas de cadastro")



nome = st.text_input("Nome do produto", placeholder='max 50 caracteres')
preco = float(st.number_input("Digite o valor do produto"))
imagem = st.text_input("Imagem do produto", placeholder="url da magemdo produto de até 100 caracteres")
codigo = st.text_input("Código do produto", placeholder="Código do produto")

btncadastroproduto = st.button("cadastrar Produto")

if btncadastroproduto:
    cadastrar(nome, preco, codigo, imagem)
    st.write("Produto cadastrado com sucesso")




"""escolha = st.selectbox('Selecione o turno', ['manhã', 'tarde', 'noite'])
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
"""