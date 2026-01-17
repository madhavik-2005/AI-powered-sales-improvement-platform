# AI-Powered Sales Call Improvement Platform (AWS Native)

## Overview
This project is an **AI-powered web application** that helps sales managers review and improve sales calls.  
Users can upload a sales call recording, view the transcript, and receive **AI-generated feedback** such as:
- What went well
- What could be improved
- Missed opportunities
- Customer intent
- Recommended next actions

The system uses **AWS-native AI services**, **Retrieval-Augmented Generation (RAG)**, and **multiple AI agents** to simulate a real SaaS sales coaching platform.

---

## Key Features
- Upload sales call audio (`.wav`, `.mp3`, `.mp4`)
- Automatic speech-to-text using **AWS Transcribe**
- AI-powered analysis using **AWS Bedrock (Claude 3 Haiku)**
- Retrieval-Augmented Generation (RAG) using a sales coaching knowledge base
- Multi-agent analysis:
  - Call summary
  - Sales performance feedback
  - Objection detection and handling
- Web-based dashboard for easy review

---

## System Architecture

### High-Level Flow

1. The user uploads a sales call recording through the **Streamlit Web UI**.
2. The audio file is stored in **Amazon S3**.
3. **AWS Transcribe** converts the audio into text.
4. The transcript is enriched using **Retrieval-Augmented Generation (RAG)** by querying a **FAISS vector store** containing sales coaching knowledge.
5. Multiple **LangChain AI agents** analyze the conversation:
   - Transcript Analyzer Agent
   - Sales Coach Agent
   - Objection Expert Agent
6. **AWS Bedrock (Claude 3 Haiku)** generates AI insights.
7. The final analysis is displayed in the **Streamlit dashboard**.

---

### Architecture Diagram (Logical View)

```text
User
  │
  ▼
Streamlit Web UI
  │
  ▼
Amazon S3 (Audio Storage)
  │
  ▼
AWS Transcribe (Speech to Text)
  │
  ▼
RAG Layer (FAISS + Sales Knowledge Base)
  │
  ▼
LangChain Agent Orchestrator
  │
  ├─ Transcript Analyzer
  ├─ Sales Coach Agent
  └─ Objection Expert Agent
  │
  ▼
AWS Bedrock (Claude 3 Haiku)
  │
  ▼
Results Dashboard (Streamlit UI)
```
---

## Technology Stack

### AI & AWS
- **Speech to Text:** AWS Transcribe  
- **LLM:** AWS Bedrock (Claude 3 Haiku)  
- **Storage:** Amazon S3  

### AI Orchestration
- **LangChain (Python)**
- Multi-agent system:
  - Transcript Analyzer Agent
  - Sales Coach Agent
  - Objection Expert Agent

### RAG
- FAISS Vector Store
- HuggingFace Sentence Transformers

### Backend & Frontend
- **Backend:** Python
- **Frontend:** Streamlit
- **Hosting:** Streamlit Community Cloud (or EC2)

---

## AI Agents

### 1. Transcript Analyzer Agent
- Summarizes the sales call
- Identifies customer intent
- Extracts key concerns

### 2. Sales Coach Agent
- Evaluates sales representative performance
- Highlights strengths
- Suggests improvements

### 3. Objection Expert Agent
- Detects explicit and implicit objections
- Focuses on pricing, trust, and timing
- Recommends best-practice responses

---

## RAG Knowledge Base
The knowledge base includes:
- Objection handling strategies
- Discovery questions
- Closing techniques
- Tone and empathy best practices
- Follow-up strategies

This content is embedded and queried during analysis to improve AI responses.

---

## Project Structure

├── app.py # Streamlit application

├── agents/ # AI agents

├── aws/ # AWS utilities (S3, Transcribe)

├── rag/ # RAG vector store logic

├── utils/ # LLM utilities

├── knowledge_base.txt # Sales coaching knowledge base

├── requirements.txt

├── README.md

└── .gitignore


---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/madhavik-2005/AI-powered-sales-improvement-platform.git
cd AI-powered-sales-improvement-platform
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

Activate the virtual environment:

Mac / Linux

```source venv/bin/activate```


Windows

```venv\Scripts\activate```

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Configure AWS Credentials

Set the following environment variables (do NOT hardcode credentials):

```
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
USE_FALLBACK=false
```


### Ensure your IAM user has access to:

        Amazon S3

        Amazon Transcribe

        Amazon Bedrock

### 5. Run the Application
    streamlit run app.py


Open the browser:

    http://localhost:8501

### Live Demo

    🔗 Public URL: (Add after deployment)

### Sample Input

Sales call audio file (.wav, .mp3, .mp4)

File size under 5 MB

### Example Output

Call summary

Sales representative performance

Missed objections and opportunities

Actionable coaching recommendations

## Issues Faced & Resolutions

- **AWS access and service subscription issues (Primary Issue):**  
  Initial execution failed because required AWS services were not subscribed/enabled, especially **AWS Bedrock** and **AWS Transcribe**. This was resolved by enabling the necessary AWS service subscriptions in the correct region (`us-east-1`) and assigning appropriate IAM permissions. Once access was granted, the system worked as expected without further changes.

- **MP4 audio format compatibility:**  
  Some MP4 files caused inconsistent transcription behavior. This was resolved by using **MP3/WAV audio formats**, which provided stable and reliable speech-to-text results with AWS Transcribe.

- **Large file handling:**  
  Uploading large audio files impacted performance. A **5 MB file size limit** was enforced at the UI level to ensure smooth uploads and predictable processing.

- **RAG response quality tuning:**  
  Initial AI responses were less precise. This was improved by tuning the **chunk size and overlap** in the vector store, resulting in better retrieval of relevant sales coaching knowledge.

- **Deployment readiness:**  
  Environment variables were used for AWS credentials instead of hardcoding, ensuring secure deployment and smooth execution in cloud environments.
