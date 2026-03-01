# SmartHire Agentic Platform (2026) 🤖🚀

SmartHire is a state-of-the-art recruitment platform built on an **Agent-First architecture** and the **RAPS framework** (Recruitment Agentic Processing System). It leverages decentralized AI agents to automate sourcing, verification, and technical evaluation.

## ✨ Features

- **Multi-Agent Orchestration**: Specialized agents (Supervisor, Sourcing, Evaluation, Integrity) working in sync.
- **Premium UI/UX**: High-fidelity glassmorphism design system built with Tailwind 4 and Next.js 16.
- **Semantic Vector Search**: Powered by PostgreSQL `pgvector` for deep candidate-job matching.
- **AI-Driven Interviews**: Adaptive technical assessments with real-time confidence and depth scoring.
- **Blockchain Trust**: Cryptographically verified credentials to eliminate resume fraud.

## 🛠️ Tech Stack

- **Frontend**: Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS 4.
- **Backend**: Python 3.10+, FastAPI, Pydantic v3, SQLAlchemy.
- **AI/LLM**: Google Gemini Pro / Flash.
- **Database**: PostgreSQL 18 + `pgvector` v0.8.1.
- **DevOps**: Docker & Docker Compose.

## 🚀 Getting Started

### Prerequisites

- [PostgreSQL 18+](https://www.postgresql.org/download/) with `pgvector` extension.
- [Node.js 20+](https://nodejs.org/)
- [Python 3.10+](https://www.python.org/downloads/)
- Gemini API Key

### Backend Setup

1. Navigate to the `backend` directory.
2. Create a `.env` file from `.env.example`.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply the database schema:
   ```bash
   python apply_schema.py
   ```
5. Start the server:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

## 📂 Project Structure

```text
├── backend/            # FastAPI Application
├── frontend/           # Next.js Application
├── db/                 # SQL Schemas and migrations
├── agents/             # Agent definitions and rules
└── .agent/             # Agentic system configurations
```

---
Built with ❤️ by the SmartHire Team (2026)
