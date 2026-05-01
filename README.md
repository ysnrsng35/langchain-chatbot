RAG System with LangChain × Chroma × Ollama
DigitalTrends 記事を対象にしたローカル RAG（検索拡張生成）システム

概要
このプロジェクトは、
LangChain v0.2 / Chroma / FastEmbed / Ollama（llama3.2:3b） を使用して構築した
ローカル実行型の RAG（検索拡張生成）システムです。

DigitalTrends の複数記事を自動取得し、
本文抽出 → チャンク化 → ベクトル化 → 検索 → 回答生成
までを一括で行います。

外部 API を使用しないため、完全ローカルで動作します。

使用技術
Python 3.12

LangChain 0.2 系

ChromaDB

FastEmbed（ローカル埋め込みモデル）

Ollama（llama3.2:3b）

BeautifulSoup4 + readability-lxml（記事本文抽出）

プロジェクト構成
コード
rag-digitaltrends/
├── main.py
├── requirements.txt
├── README.md
├── data/
│   └── urls.txt
└── chroma_db/   （自動生成・Git管理外）
セットアップ
1. 仮想環境の作成
コード
python -m venv venv
コード
source venv/bin/activate
（Windows の場合）

コード
venv\Scripts\activate
2. ライブラリのインストール
コード
pip install -r requirements.txt
3. Ollama モデルの準備
コード
ollama pull llama3.2:3b
実行方法
コード
python main.py
質問例
コード
Spotifyのアカウントを削除する方法についての質問の5番目のポイントは何ですか？
