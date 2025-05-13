
# Azure OpenAI Chatbot with Azure Cognitive Search (RAG-Based)

This project is a simple yet powerful command-line chatbot that integrates **Azure OpenAI** with **Azure Cognitive Search** to enable semantic search-based chat responses. It serves as a minimal implementation of a **Retrieval-Augmented Generation (RAG)** system.

## Features

- 💬 Chatbot interface via command-line
- 🔎 Semantic search through Azure Cognitive Search
- 📚 RAG-based architecture for contextual responses
- 🔐 Secure environment configuration via `.env` file

## Technologies Used

- Python
- Azure OpenAI (Chat & Embedding deployments)
- Azure Cognitive Search
- `openai` Python SDK
- `python-dotenv` for environment variable management

## Project Structure

```
├── chat.py               # Main script to run the chatbot
├── .env                  # Environment variables (keys, endpoints, etc.)
└── README.md             # Project documentation
```

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/aliellkhateeb/azure-openai-rag-chatbot.git
cd azure-openai-chatbot
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

### 4. Configure your `.env` file

Rename `.env.example` to `.env` and fill in the following keys:

```env
AZURE_OAI_ENDPOINT=your_openai_endpoint
AZURE_OAI_KEY=your_openai_key
AZURE_OAI_DEPLOYMENT=your_deployment_name

AZURE_SEARCH_ENDPOINT=your_search_endpoint
AZURE_SEARCH_KEY=your_search_key
AZURE_SEARCH_INDEX=your_index_name

AZURE_EMBEDDING_ENDPOINT=your_embedding_endpoint
AZURE_EMBEDDING_DEPLOYMENT=your_embedding_deployment_name

Semantic_Configuration=your_semantic_config
Query_Type=your_query_type
```

### 5. Run the chatbot

```bash
python chat.py
```

Then type your question in the terminal when prompted.

## How it works

1. The user types a question.
2. The app sends the question to Azure OpenAI with a `data_sources` parameter.
3. Azure uses Cognitive Search to find relevant documents based on embeddings.
4. The chatbot responds with a generated answer based on the retrieved content.

## Notes

- The system prompt is currently a placeholder — customize it in `build_prompt()` for your use case.
- Make sure all services (OpenAI, Search, Embedding) are deployed under the same Azure region when possible.
- You can enable streaming responses or logging as needed.

## TODO / Improvements

- [ ] Add support for logging and conversation history
- [ ] Add UI via Flask or Gradio
- [ ] Unit tests and CI/CD
- [ ] Add retry mechanism for failed API calls
- [ ] Package as a pip module or CLI tool

## Author

**Ali EL-Khateeb**  
AI Engineer 

---

> Feel free to fork, contribute, and share
