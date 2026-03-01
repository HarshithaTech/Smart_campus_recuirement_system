-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Job Roles Table
CREATE TABLE IF NOT EXISTS job_roles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    requirements JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Students Table
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    is_deleted BOOLEAN DEFAULT FALSE
);

-- Verified Credentials Table
CREATE TABLE IF NOT EXISTS verified_credentials (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    credential_type VARCHAR(100),
    credential_hash TEXT,
    blockchain_tx_id TEXT,
    issued_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Embeddings Table (Vector Search)
CREATE TABLE IF NOT EXISTS embeddings (
    id SERIAL PRIMARY KEY,
    reference_id INTEGER NOT NULL,
    reference_type VARCHAR(50), -- 'resume' or 'job_role'
    vector_data vector(1536), -- Dimension for Gemini/OpenAI embeddings
    content TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Interview Sessions Table
CREATE TABLE IF NOT EXISTS interview_sessions (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    job_role_id INTEGER REFERENCES job_roles(id),
    status VARCHAR(50) DEFAULT 'scheduled',
    session_token TEXT UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Interview Scores Table
CREATE TABLE IF NOT EXISTS interview_scores (
    id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES interview_sessions(id),
    technical_depth_score FLOAT,
    confidence_score FLOAT,
    cultural_fit_score FLOAT,
    entropy_score FLOAT, -- Anti-cheating metric
    analysis_report JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Skill Gap Reports Table
CREATE TABLE IF NOT EXISTS skill_gap_reports (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    job_role_id INTEGER REFERENCES job_roles(id),
    gap_analysis JSONB,
    recommendations JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_student_email ON students(email);
CREATE INDEX IF NOT EXISTS idx_embeddings_vector ON embeddings USING ivfflat (vector_data vector_cosine_ops);
