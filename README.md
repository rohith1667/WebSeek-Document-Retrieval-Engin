# 🔍 SearchVista: Intelligent Web Document Retrieval System

### *An end-to-end Python platform for web crawling, indexing, and semantic information retrieval.*

---

## 🧠 Abstract
**SearchVista** is a full-stack **information retrieval system** built with Python, Scikit-Learn, Scrapy, Flask, and NiceGUI.  
It automates **web document discovery, indexing, and search ranking** using TF-IDF and cosine similarity.  
The system features a **Scrapy-based crawler** for content collection, a **Scikit-Learn indexer** for inverted index construction, and a **Flask API** that processes free-text queries in real time.  
Future extensions include distributed crawling, vector embedding integration, and **semantic/LLM-based search** for contextual retrieval.

---

## ⚙️ System Overview

The architecture consists of four modular components that deliver efficient and explainable retrieval.

| Component | Description |
|------------|-------------|
| **1. Web Crawler (Scrapy)** | Traverses the web from seed URLs, downloads web pages, extracts text, and stores structured outputs. Supports crawling depth limits, throttling, and concurrency. |
| **2. Indexer (Scikit-Learn)** | Builds an **inverted index** using TF-IDF to represent term importance across documents. Optionally supports **Word2Vec** and **k-NN similarity** for semantic matching. |
| **3. Query Processor (Flask API)** | Handles user queries, validates input, performs **spell-checking and query expansion** via NLTK and WordNet, and returns the top-K ranked results as JSON. |
| **4. GUI (NiceGUI)** | Provides a visual interface to monitor crawl progress and explore retrieved pages interactively. |

---

## 🧩 Architecture

- **Crawling Layer:** Scrapy orchestrates data collection with configurable depth and page limits.  
- **Indexing Layer:** TF-IDF scoring + cosine similarity ranking ensure precise retrieval.  
- **Processing Layer:** Flask + NLTK manage query validation, expansion, and ranking.  
- **Visualization Layer:** NiceGUI displays progress and search results in real time.  

This modular design allows easy experimentation with **semantic embeddings** or integration with **LLM retrievers** like LangChain or OpenAI APIs.

---

## 🚀 Execution Workflow

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rohith1667/Information-retrieval_final.git
   cd Information-retrieval_final
   python main.py
2. **Crawling Phase**
The **Scrapy crawler** fetches up to **200 pages** from sources such as [wikiHow](https://www.wikihow.com/Main-Page).  
Progress can be viewed live through the **NiceGUI** interface, which visualizes the crawling process in real time.

3. **Indexing & Processing**
After the crawling phase, click **Start** in the UI to begin indexing.  
The system computes **TF-IDF vectors** for all crawled pages and serializes the processed data into a file named `processed_data.pkl`. This ensures fast reloads without the need to re-crawl data.

4. **Querying**
Users can enter **natural-language queries** (e.g., “how to cook pasta”).  
The query processor performs **spell-checking, expansion, and ranking** using cosine similarity, returning the most relevant documents. Top-ranked results appear instantly in the **NiceGUI interface**, offering an interactive search experience.

---

## 🧪 Sample Results

| Query | Example Result |
|-------|----------------|
| “iphone” | Pages on iPhone setup and troubleshooting |
| “protein” | Nutrition and health-related articles |
| “man” | Social and lifestyle content |

Screenshots of crawling and query execution are available in the repository’s assets.

---

## 📊 Key Achievements
- **High-accuracy indexing** via TF-IDF and cosine similarity.  
- **Interactive visualization** using NiceGUI for live progress tracking.  
- **Optimized storage** through serialized intermediate files (`.pkl`).  
- **Modular and extensible design** — ready for hybrid symbolic + neural search.

---

## 🔮 Next Steps
- Integrate **sentence embeddings** using `sentence-transformers`.  
- Add **distributed crawling** with Scrapyd.  
- Extend to **LLM-powered retrieval** through LangChain or OpenAI APIs.

---

## 🧰 Tech Stack
**Languages:** Python  
**Frameworks:** Scrapy, Flask, Scikit-Learn, NiceGUI, NLTK  
**Libraries:** TF-IDF Vectorizer, WordNet, Cosine Similarity  
**Data Source:** [wikiHow](https://www.wikihow.com/Main-Page)

---

## 🏁 Conclusion
**SearchVista** demonstrates the complete lifecycle of information retrieval — from **web crawling and indexing** to **ranked search and visualization**.  
It serves as a foundation for integrating **LLM-based RAG systems**, bridging traditional search engines with modern **semantic and agentic AI retrieval**.
