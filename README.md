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
   git clone https://github.com/yourusername/qa-system.git
   cd qa-system
