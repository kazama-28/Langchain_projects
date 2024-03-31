import warnings
warnings.filterwarnings("ignore")
from langchain import OpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain.document_loaders import UnstructuredURLLoader
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS 
import pickle
from langchain.chains import RetrievalQAWithSourcesChain

load_dotenv()

st.title("News Tool Researcher 📈")
with st.sidebar:
    st.title("News Articles URL")
total_urls = st.sidebar.selectbox("Select number of URLs", (1,2,3,4,5))

if total_urls:
    urls = []
    for i in range(total_urls):
        url = st.sidebar.text_input(f"URL {i+1}")
        urls.append(url)

process_url_clicked = st.sidebar.button("Process_URLs")
file_path= "faiss_embeddings.pkl"

main_placeholder= st.empty()
llm = OpenAI(temperature = 0.7, max_tokens = 500)

if process_url_clicked:
    loader = UnstructuredURLLoader(urls = urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        separators= ['\n\n', '\n', '.', ',', ' '],
        chunk_size = 1000,
        chunk_overlap = 200
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = splitter.split_documents(data)
    embeddings = OpenAIEmbeddings()
    index_faiss_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    index_faiss_openai.save_local("faiss_store")
query = main_placeholder.text_input("Question: ")

if query:
    print("inside if")
    main_placeholder.text("Running LLM chain to find answer...✅✅✅")
    time.sleep(2)
    embs = FAISS.load_local("faiss_store", OpenAIEmbeddings(), allow_dangerous_deserialization = True)
    retriever = embs.as_retriever(search_kwargs=dict(k=5))
    chain = RetrievalQAWithSourcesChain.from_llm(llm = llm, retriever = retriever)
    result = chain({"question": query},  return_only_outputs= True)
    st.header("Answer")
    st.write(result["answer"])

    sources = result.get("sources", "")
    if sources:
        st.subheader("Sources")
        sources_list = sources.split("\n")
        for source in sources_list:
            st.write(source)







