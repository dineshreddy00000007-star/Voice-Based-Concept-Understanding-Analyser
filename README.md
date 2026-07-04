# Voice-Based-Concept-Understanding-Analyser
A Voice-Based Concept Understanding Analyser is an AI system that converts speech into text, interprets meaning using NLP, and extracts key ideas for better comprehension. It enables interactive learning, intent detection, and real-time feedback across education, business, and accessibility.

# 📊 SystemOverview: Audio Evaluation & Analysis Platform
## Main Entities
- User → Represents individuals interacting with the system.

- Audio File → Uploaded recordings linked to users.

- Transcript → Text generated from audio files.

- Audio Feature → Technical metrics extracted (pause ratio, energy, etc.).

- Evaluation Result → Scores and qualitative assessments of audio.

- Reference Concept → Benchmark concepts used for evaluation.

- Semantic Similarity → Measures alignment between transcript and reference concepts.

- Report → Generated documents summarizing evaluation results.

- Session → Tracks user activity and engagement periods.
  
----

# ⚙️ Technology Stack
- Python → Core programming language

- FastAPI → Backend API framework

- Streamlit → Interactive web UI

- Librosa → Audio feature extraction

- Whisper → Speech‑to‑text transcription

- Sentence‑BERT → Semantic similarity analysis

- ReportLab → Automated PDF report generation

- Visual Studio Code → Development environment
- 
----

# 📚 Reference Links
- Python

- FastAPI

- Streamlit

- Librosa

- Whisper

- Sentence‑BERT

- ReportLab

- Visual Studio Code
  
---

## Key Relationships
- Users upload audio files.

- Each audio file can generate a transcript and audio features.

- Transcripts are analyzed for filler words and semantic similarity against reference concepts.

- Audio files are evaluated to produce results (scores, understanding levels, notes).

- Results are compiled into reports for users.

- Sessions track user activity across uploads and evaluations,
----

## System Purpose
This platform is designed to support:

- 🎙️ Audio Upload & Management

- 📝 Speech Transcription

- 🔍 Semantic Analysis & Concept Matching

- 📈 Understanding Assessment & Scoring

- 📑 Report Generation

- ⏱️ Session Tracking for User Engagement

----

# 🧭 Project Flow Overview
## Definition
### Project Flow is the structured sequence of phases and tasks that guide a project from initiation to completion. It acts as a roadmap for teams to execute work efficiently, manage resources, and monitor progress toward objectives.

----

## Core Phases
| Phase | Purpose |
| --- | --- |
| **1. Initiation** | Define goals, scope, and stakeholders. |
| **2. Planning** | Outline tasks, timelines, and resource allocation. |
| **3. Execution** | Implement project deliverables and monitor progress. |
| **4. Monitoring & Control** | Track performance, manage risks, and ensure quality. |
| **5. Closure** | Finalize deliverables, document outcomes, and review success. |

------

# 🛠️ Environment Setup & Validation
-----
## 1. Create a Dedicated Virtual Environment
bash
 Navigate to your project folder
cd path/to/vbcua_project

 Create virtual environment named vbcu_env
python3 -m venv vbcu_env

 Activate environment
 On Linux/Mac:
source vbcu_env/bin/activate
 On Windows:
vbcu_env\Scripts\activate

-----

## 2. Install Dependencies
Make sure you have a requirements.txt file with all libraries listed:

text
streamlit
openai-whisper
sentence-transformers
librosa
soundfile
matplotlib
reportlab
nltk
Then install:

bash
pip install -r requirements.txt

-----

## 3. Verify Python Compatibility
Check Python version:

bash
python -version✅ Must be 3.10+ (recommended: 3.10 or 3.11 for Whisper & Sentence‑BERT compatibility).

------

## 4. Test Imports
Run a quick script (test_imports.py) to confirm modules load correctly:

python
import streamlit
import whisper
from sentence_transformers import SentenceTransformer
import librosa
import soundfile as sf
import matplotlib
import reportlab
import nltk

print("✅ All libraries imported successfully!")
Execute:

bash
python test_imports.py

-----

## 5. Validate Core Components
### - Speech Transcription (Whisper)

python
model = whisper.load_model("base")
result = model.transcribe("sample_audio.wav")
print(result["text"])
Semantic Similarity (Sentence‑BERT)

python
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(["Hello world", "Hi there"])
print("✅ Semantic embeddings generated")

-----

### - Audio Feature Extraction (Librosa)

python
y, sr = librosa.load("sample_audio.wav")
zcr = librosa.feature.zero_crossing_rate(y)
print("Zero Crossing Rate:", zcr.mean())
UI Rendering (Streamlit)

bash
streamlit run app.py

-----

# ✅ Outcome
- Isolated environment (vbcu_env) ensures reproducibility.

- All dependencies installed and verified.

- Core modules tested without runtime errors.

- Ready for development and deployment.
-----

# 📂 Project Structure

```
vbcua_project/
-------
│
├── app.py
├── audio_utils.py
├── speech_to_text.py
├── semantic_eval.py
├── scoring_engine.py     
├── report_generator.py 
├── requirements.txt
├── tests/
│   ├── test_audio_utils.py
│   ├── test_speech_to_text.py
│   ├── test_semantic_eval.py
│   ├── test_scoring_engine.py
│   └── test_report_generator.py
│
└── data/
    ├── sample_audio.wav
    └── reports/
```
----

# 🚀 Launch Application
## Make sure your virtual environment (vbcu_env) is activated:

bash
source vbcu_env/bin/activate   # Linux/Mac
vbcu_env\Scripts\activate      # Windows
Run the Streamlit app:

bash
streamlit run app.py
### This will open a local server (usually at http://localhost:8501) in your browser.

----
# 🧠 Epic 2 – Core Intelligence Flow
## Modules & Flow
## 1. Speech-to-Text (Whisper)

- Input: Uploaded audio file

- Output: Transcript text

⬇️ feeds into both semantic analysis and scoring engine

## 2. Semantic Similarity Engine (Sentence-BERT)

- Input: Transcript + Reference Concepts

- Output: Similarity scores (conceptual alignment)

## 3. Audio Feature Extraction (Librosa)

- Input: Raw audio file

- Output: Deterministic metrics (pause ratio, RMS energy, zero-crossing rate)

## 4. Scoring Engine

- Combines semantic scores + audio metrics

- Produces evaluation result:

  - Overall score

  - Understanding level (Strong / Moderate / Poor)

  - Notes
  
-----

## Outcome
- Hybrid evaluation pipeline:

  - Objective metrics (deterministic audio features)

  - Subjective analysis (AI-driven semantic similarity)

- Generates evaluation results → later used in reports (Epic 3 & 4).
  
-----

# 🧠 Semantic Evaluation Workflow
## 1. Generate Embeddings
Use Sentence‑BERT to encode both the student’s explanation and the reference concept(s) into dense vector embeddings.

python
from sentence_transformers import SentenceTransformer

# Load pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example inputs
student_explanation = "Photosynthesis is the process by which plants make food using sunlight."
reference_concept = "Photosynthesis converts light energy into chemical energy in plants."

# Generate embeddings
student_embedding = model.encode(student_explanation)
reference_embedding = model.encode(reference_concept)

---- 

## 2. Compute Cosine Similarity
Cosine similarity quantifies how close the student’s explanation is to the reference concept.

python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

similarity_score = cosine_similarity(
    [student_embedding],
    [reference_embedding]
)[0][0]

print("Raw similarity score:", similarity_score)

---- 

## 3. Normalize Scores
To ensure consistent interpretation across evaluations, normalize the similarity score to a 0–100 scale.

python
# Normalization: cosine similarity ranges from -1 to 1
normalized_score = (similarity_score + 1) / 2 * 100
print("Normalized similarity score:", round(normalized_score, 2))

----

# ✅ Outcome

- Embeddings capture semantic meaning of both student and reference text.

- Cosine similarity provides a quantitative measure of conceptual alignment.

Normalized scores make results interpretable and consistent across different evaluations (e.g., 0–100 scale for reporting).

-----
