import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain #to get relevant docs in QA
from langchain_core.prompts import ChatPromptTemplate #to create own custom prompt template
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

#load the GROQ and Google API key from .env file
groq_api_key=os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY']=os.getenv("GOOGLE_API_KEY")

st.title("Gemma Model Document Q&A")
llm=ChatGroq(groq_api_key=groq_api_key,model_name="Gemma-7b-It")

prompt=ChatPromptTemplate.from_template(
'''
    Answer the questions based on the provided contxt only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions:{input}
'''
)

def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader=PyPDFDirectoryLoader("./us_census")#Data Ingestion
        st.session_state.docs=st.session_state.loader.load()#Document loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)
        
prompt1=st.text_input("Enter your question from documents")

if st.button("Creating Vector Store"):
    vector_embedding()
    st.write("Vector store embedding is ready")
    
import time

if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever() #to retrieve info from DB   
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    
    start=time.process_time()
    response=retrieval_chain.invoke({'input':prompt1})
    st.write(response['answer'])
    
    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")
    
    
    
    






