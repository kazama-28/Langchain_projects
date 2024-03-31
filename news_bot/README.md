# News_bot
News bot is a tool designed to fetch answers to questions from a set of web pages whose url is provided as input through the web app. It utilizes the powerful technique of RAG (retrieval augmented generation) for providing relevant context to LLMs to answer a specific question.
It works particularly well for news-related articles.
<img width="857" alt="image" src="https://github.com/kazama-28/Langchain_projects/assets/67082080/b22c82cf-1d3b-4373-974c-cf39aba3980e">

## Key Features:
- Specify URLs to scrape textual information present in the webpage.
- Process webpages using Langchain's UnstructuredURL Loader.
- Implement RAG via the creation of embedding vector using OpenAI's embeddings and leverage Meta's vector database FAISS for retrieval of relevant information.
- Interact with OpenAI's ChatGPT by inputting queries and receiving answers along with the source URLs.
  




