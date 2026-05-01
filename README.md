# チャットボットプロジェクト

このプロジェクトは、LangChain・Chroma・FastEmbed・Ollama を使用して  
構築したローカル環境で動作する チャットボットシステムです。  
（※Ollama が Colab 上で動作しないため、ローカルで実行しています。　
　　またACTIVELOOPのトークンが有効にならなかったためChroma＋FastEmbedを使用しています）

---

## 1. 使用技術

- Python 3.12  
- LangChain 0.2 系  
- ChromaDB  
- FastEmbed 
- Ollama（llama3.2:3b）  
- BeautifulSoup4 / readability-lxml

---

## 2. プロジェクト構成

langchain-chatbot/

├── main.py

├── data/urls.txt

├── chroma_db/

├── README.md

└── requirements.txt


---

## 3. 動作手順

### ① セットアップ　
仮想環境
python -m venv venv
source venv/bin/activate
(Windows)
venv\Scripts\activate
ライブラリのインストール
pip install -r requirements.txt
Ollamaモデル
ollama pull llama3.2:3b
### ② 実行
python main.py
### ③ 質問  
例：
Spotifyのアカウントを削除する方法についての質問の5番目のポイントは何ですか？

---

## 5. スクリーンレコード

/docs

├── demo.mp4
