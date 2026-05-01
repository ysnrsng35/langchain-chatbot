RAG System with LangChain × Chroma × Ollama
DigitalTrends 記事を対象にしたローカル RAG（検索拡張生成）システム

📌 概要
このプロジェクトは、
LangChain v0.2 / Chroma / FastEmbed / Ollama（llama3.2:3b） を使用して構築した
ローカル実行型の RAG（検索拡張生成）システムです。

DigitalTrends の複数記事を自動取得し、
全文抽出 → チャンク化 → ベクトル化 → 検索 → LLM 生成
までを一括で行います。

外部 API を使用しないため、完全ローカルで動作します。

🛠 使用技術
Python 3.12

LangChain 0.2 系

ChromaDB

FastEmbed（高性能ローカル埋め込みモデル）

Ollama（llama3.2:3b）

BeautifulSoup4 + readability-lxml（記事本文抽出）

📂 プロジェクト構成
コード
rag-digitaltrends/
├── main.py                # RAG のメインコード
├── requirements.txt       # 必要ライブラリ
├── README.md              # 説明書
├── data/
│   └── urls.txt           # 記事URL一覧（任意）
└── chroma_db/             # ベクトルDB（自動生成）
🚀 セットアップ
1. 仮想環境の作成
コード
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
2. ライブラリのインストール
コード
pip install -r requirements.txt
3. Ollama モデルの準備
コード
ollama pull llama3.2:3b
▶️ 実行方法
コード
python main.py
💡 質問例
コード
Spotifyのアカウントを削除する方法についての質