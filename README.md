# RAG（Retrieval-Augmented Generation）プロジェクト

このプロジェクトは、LangChain・Chroma・Ollama を使用して  
ローカル環境で動作する RAG（検索拡張生成）システムです。  
（※Ollama が Colab 上で動作しないため、ローカルで実行しています）

---

## 1. 使用技術

- Python 3.12  
- LangChain 0.2 系  
- ChromaDB  
- SentenceTransformer（all-MiniLM-L6-v2）  
- Ollama（Qwen2.5:1.5b モデル）  
- ローカル LLM による回答生成（OpenAI や Gemini の無料枠を使い切ったため）

---

## 2. プロジェクト構成

rag-project/

├── rag.py

├── data/sample.txt

├── chroma_db/

├── README.md

└── requirements.txt


---

## 3. 動作手順

### ① モデルの準備（Ollama）
ollama pull qwen2.5:1.5b
### ② Python ライブラリのインストール
pip install -r requirements.txt
### ③ RAG の実行
python rag.py
### ④ 質問を入力  
例：
猫について教えて
---

## 4. 回答例
--- 回答 ---

猫について教えて:

猫は独立したペットであり、自分だけの空間を楽しむことがよくあります。
---

## 5. スクリーンレコード

/docs

├── demo1.mp4
