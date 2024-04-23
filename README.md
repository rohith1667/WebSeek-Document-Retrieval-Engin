# INFORMATION RETRIEVAL FINAL PROJECT

**Student:** Rohith  
**ID:** A20554359  

## Abstract
This project aims to develop a web document retrieval system using Python, Scikit-Learn, Scrapy, and Flask. It consists of a Scrapy-based crawler for downloading web documents, a Scikit-Learn-based indexer for constructing an inverted index, and a Flask-based processor for handling free text queries. The objectives include efficient web crawling, accurate document indexing, and fast query processing. The next steps involve enhancing the system with features such as distributed crawling and semantic search capabilities.

# Overview

The proposed system consists of three main components: a web crawler, an indexer, and a query processor.

- **Web Crawler**: Responsible for traversing the web, downloading web documents, and extracting relevant content. It provides functionalities to initialize crawling with seed URLs, limit the number of pages to crawl, and control the crawling depth. Optional features like concurrent crawling with autothrottle and distributed crawling using scrapyd enhance the efficiency and scalability of the crawler.

- **Indexer**: Constructs an inverted index from the crawled documents, enabling efficient retrieval of relevant documents based on user queries. It utilizes Scikit-Learn's TF-IDF (Term Frequency-Inverse Document Frequency) scoring mechanism to represent documents and calculate their relevance. Additionally, it supports optional features such as vector embedding representation using word2vec and neural/semantic search using kNN similarity.

- **Query Processor**: Handles user queries, validates them, and returns the top-K ranked results based on relevance scores calculated by the indexer. It uses Flask to provide a RESTful API for querying the indexed documents in JSON format.

# Design

The system's capabilities include initiating a crawl with seed URLs, constructing an inverted index with TF-IDF scores, and processing user queries to retrieve relevant documents. Interactions between components involve passing data between the crawler, indexer, and processor. Integration is achieved through standardized input/output formats.


# Architecture

## Software Components

The project consists of four main components:

1. **Crawler**: Utilizing Scrapy, this component is responsible for traversing the web, retrieving web documents, and preparing them for indexing. It is configured with parameters such as seed URLs, maximum pages, and crawling depth.

2. **Indexer**: Employing Scikit-Learn, the indexer constructs an inverted index from the documents obtained by the crawler. It utilizes TF-IDF scores to represent the importance of words in documents, facilitating efficient search retrieval.

3. **Processor**: Implemented with Flask, the processor handles user queries and returns relevant documents. It validates queries, performs spell checking using NLTK, and can expand queries using WordNet.

4. **GUI (Graphical User Interface)**: We've integrated NiceGUI to provide a user-friendly interface for viewing the web documents. It displays the webpages retrieved by the crawler, allowing users to visualize the content during the crawling process.

# Execution Process

Here's the procedural flow from retrieving the code from Git to executing the system:

## Version Control (Git):

- Pull the latest code from the Git repository:

- Run the main.py file to initiate the system:


## Initialization:

- Upon running main.py, the crawler begins fetching web documents. Ensure that the crawler operates until it reaches the specified max_pages, i.e., 200.

## Crawling:

- Monitor the progress of the crawler to ensure that web pages are being scraped effectively until the maximum depth is reached.
- Simultaneously, open the NiceGUI interface to view the webpages as they are being retrieved.

## Processing:

- Once the crawling phase is complete, initiate the processing of web pages by clicking the "Start" button.
- The indexer commences building the inverted index, while the processor becomes ready to handle incoming queries.

## Query Processing:

- Submit queries to the processor for retrieval of relevant documents.
- The processor validates and processes queries, providing top-ranked results based on relevance scores.

# Operation

1. **Pull the Repository from GitHub**:
   - Open Visual Studio Code (VSCode).
   - Go to "Clone Git Repository" and enter the repository URL: [https://github.com/rohith1667/Information-retrieval_final.git](https://github.com/rohith1667/Information-retrieval_final.git)

2. **Run the System**:
   - Open the terminal in the root folder.
   - Execute the main.py file:
     ```
     python main.py
     ```

3. **Check Crawling Progress**:
   - Monitor the terminal to ensure all web pages are crawled until the max_pages limit (e.g., 200).
   - <img width="468" alt="image" src="https://github.com/rohith1667/Information-retrieval_final/assets/143306794/9826cc05-1113-4e9e-9434-dadf44351dc3">


4. **Initiate Processing of Web Pages**:
   - Visit the website and click the "Start" button to begin processing web pages.
   - Once processing is complete, a pickle file named processed_data.pkl is created to store the processed pages.
   - <img width="468" alt="image" src="https://github.com/rohith1667/Information-retrieval_final/assets/143306794/146a47db-6b81-46f5-8f38-9a7a7debd935">

     
5. **Submit Queries**:
   - Use the search bar to submit queries.
   - The system retrieves top-ranked results based on relevance scores.
   - <img width="468" alt="image" src="https://github.com/rohith1667/Information-retrieval_final/assets/143306794/c5a93643-8e41-4f2f-a2ef-7025177c7326">



# Conclusion

We have successfully developed a web document retrieval system utilizing Python, Scikit-Learn, Scrapy, Flask, and NiceGUI. We have achieved the following:

- **Efficient Web Crawling**: Our system efficiently crawls web pages, retrieving relevant content within the specified limits.
  
- **Accurate Indexing**: Using TF-IDF scoring, we have constructed an inverted index that accurately represents the importance of words in documents.
  
- **User-Friendly Query Processing**: The processor handles user queries, providing top-ranked results based on relevance scores. The integration of NiceGUI offers a visually appealing interface for viewing web documents during the crawling process.
  
- **Storage Optimization**: By storing processed pages in a pickle file (processed_data.pkl), we optimize resource usage and reduce the need to reload pages.
# Data Sources


# Source Code

- **Main.py**:
- <img width="468" alt="image" src="https://github.com/rohith1667/Information-retrieval_final/assets/143306794/5667a851-e48b-4cc7-935c-8d0c3fad0ffe">


- **Indexer.py**:
- <img width="468" alt="image" src="https://github.com/rohith1667/Information-retrieval_final/assets/143306794/3ad5b4cc-fa33-4bf0-aa2d-fee303cf3fbf">


- **Indexer2.py**:
- <img width="468" alt="image" src="https://github.com/rohith1667/Information-retrieval_final/assets/143306794/906ae42d-ec5d-4917-b88d-a4651fabf038">



# References

- Scrapy documentation: [https://docs.scrapy.org/en/latest/](https://docs.scrapy.org/en/latest/)
- Scikit-Learn documentation: [https://scikit-learn.org/stable/documentation.html](https://scikit-learn.org/stable/documentation.html)
- Flask documentation: [https://flask.palletsprojects.com/en/2.0.x/](https://flask.palletsprojects.com/en/2.0.x/)
- NiceGUI documentation: [https://nicegui.io/docs/](https://nicegui.io/docs/)
- NLTK documentation: [https://www.nltk.org](https://www.nltk.org/)
- WordNet documentation: [https://wordnet.princeton.edu/](https://wordnet.princeton.edu/)



