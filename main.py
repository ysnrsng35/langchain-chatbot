# ============================
# main.py（DigitalTrends 版）
# ============================

import requests
from bs4 import BeautifulSoup
from readability import Document as ReadabilityDoc

from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.llms import Ollama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


# ============================================
# 1. DigitalTrends の記事 URL（複数）
# ============================================

articles = [
    "https://www.digitaltrends.com/computing/claude-sonnet-vs-gpt-4o-comparison/",
    "https://www.digitaltrends.com/computing/apple-intelligence-proves-that-macbooks-need-something-more/",
    "https://www.digitaltrends.com/computing/how-to-use-openai-chatgpt-text-generation-chatbot/",
    "https://www.digitaltrends.com/computing/character-ai-how-to-use/",
    "https://www.digitaltrends.com/computing/how-to-upload-pdf-to-chatgpt/"
]


# ============================================
# 2. requests + readability で本文抽出
# ============================================

docs = []

for url in articles:
    response = requests.get(url, timeout=10)
    response.encoding = response.apparent_encoding

    read_doc = ReadabilityDoc(response.text)
    html = read_doc.summary()

    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n")

   # print(f"{url} の取得文字数: {len(text)}")

    docs.append(Document(page_content=text, metadata={"source": url}))


# ============================================
# 3. チャンク化
# ============================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)


# ============================================
# 4. Chroma に保存
# ============================================

embeddings = FastEmbedEmbeddings()

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

retriever = db.as_retriever()


# ============================================
# 5. Ollama（ローカル LLM）
# ============================================

llm = Ollama(model="llama3.2:3b")


# ============================================
# 6. LangChain v0.2 の RAG チェーン
# ============================================

prompt = ChatPromptTemplate.from_template("""
以下のコンテキストに基づいて質問に答えてください。

【コンテキスト】
{context}

【質問】
{question}

分かりやすく日本語で答えてください。
""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)


# ============================================
# 7. 質問
# ============================================

query = "Spotifyのアカウントを削除する方法についての質問の5番目のポイントは何ですか？"
result = rag_chain.invoke(query)

print("\n===== 回答 =====")
print(result)
