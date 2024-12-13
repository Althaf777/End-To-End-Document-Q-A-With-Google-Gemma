# End-to-End Question & Answer System using Google Gemma 

An interactive and efficient Question & Answer system leveraging **Google Gemma**, **GROQ API**, and **Google Generative AI embeddings**. This project integrates PDF document processing, vector similarity search, and an intuitive interface built with **Streamlit** for seamless user interaction.  

## Features  
- **PDF Document Input:** Handles PDF files as the primary text source.  
- **Generative AI Embeddings:** Converts text chunks into vector embeddings using Google Generative AI.  
- **FAISS Vector Database:** Optimized for high-speed similarity search.  
- **Interactive UI:** Built with Streamlit to facilitate user-friendly Q&A interactions.  

## System Architecture  
1. **Input Processing:**  
   - PDF documents are uploaded and processed into text chunks.  
2. **Vectorization:**  
   - Text chunks are converted into embeddings using Google Generative AI.  
3. **Vector Search:**  
   - FAISS is utilized for similarity search to fetch the most relevant chunks.  
4. **Answer Retrieval:**  
   - GROQ API retrieves context-specific answers for user queries.  
5. **Frontend:**  
   - A user-friendly interface built with Streamlit.  

## Prerequisites  
- Python 3.8 or above  
- Install required libraries from `requirements.txt`  
- API keys for Google Gemma and GROQ  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Althaf777/End to End QA with Google Gemma.git

2. Install Dependencies
   ```bash
   pip install -r requirements.txt

3. Run the streamlit application
    ```bash
   streamlit run app.py

## Usage
1. Upload PDF documents
2. Enter your query in the input box
3. Receive accurate, context-aware answers in real time.

## User Interface
![Screenshot 2024-12-10 161751](https://github.com/user-attachments/assets/1167bf44-76c5-4b39-8e38-df6961409cb4)

## Technologies Used
**Google Gemma**: For generating insights from text.
**GROQ API**: Efficient answer retrieval.
**Google Generative AI**: Embedding text into vector representations.
**FAISS**: Stores vector embeddings, Fast Approximate Nearest Neighbors search.
**Streamlit**: Frontend framework for creating the interactive UI.

## Project Structure
```plaintext
.
├── app.py               # Streamlit application
├── utils/               # Helper functions
│   ├── pdf_processing.py
│   ├── embedding_utils.py
│   └── faiss_search.py
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Future Enhancements
- Support for additional document formats (e.g., Word, HTML).
- Enhanced query understanding with NLP techniques.
- Integration with more AI APIs for diverse use cases.


## Contributing
Contributions are welcome! 

## Acknowledgments
Special thanks to the developers of Google Gemma, GROQ API, and FAISS for their contributions to the open-source community.





   

