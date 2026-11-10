import os # Biblioteca para acessar variáveis de ambiente
import streamlit as st # Framework para criar a interface web do chatbot
from dotenv import load_dotenv # Função que carrega as variáveis do arquivo .env
from langchain_community.document_loaders import PyPDFLoader # Carrega documentos em formato PDF
from langchain_text_splitters import RecursiveCharacterTextSplitter # Divide textos longos em trechos menores (chunks)
from langchain_chroma import Chroma # Banco de dados vetorial utilizado no projeto
from langchain_groq import ChatGroq # Integra o Python à API da Groq para utilizar o LLM
from langchain_huggingface import HuggingFaceEmbeddings # Gera embeddings utilizando modelos do Hugging Face

#CONFIGURAÇÃO DA API GROQ
#Carrega as variaveis armazenadas no arquivo .env
load_dotenv()

#verifica  se  a chave API está disponivel
if not os.getenv("GROQ_API_KEY"):
   st.error('Configure a chave API_GROQ no arquivo .env')
   st.stop() #interrompe a execução

#2 INTERFACE INICIAL
st.title('Chatbot Trabalho Garantido')
st.write('Faça perguntas sobre o edital do programa')

