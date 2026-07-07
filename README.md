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

 Create virtual environment named .venv
python3 -m venv .venv

 Activate environment
 On Linux/Mac:
source .venenv/bin/activate
 On Windows:
.venv\Scripts\activate

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

-----

# 📂 Project Structure

```
Voice-Based-Concept-Understanding-Analyser/
│
├── app.py
├── requirements.txt
├── README.md
├── models/
│   ├── whisper_model.py
│   ├── semantic_model.py
│   └── scoring.py
├── audio/
│   ├── extractor.py
│   ├── preprocessing.py
│   └── waveform.py
├── reports/
│   └── pdf_generator.py
├── database/
│   └── database.py
├── reference/
│   └── concepts.json
├── uploads/
├── outputs/
└── assets/
```
----

# 🚀 Launch Application
## Make sure your virtual environment (vbcu_env) is activated:
```
bash
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
Run the Streamlit app:
```
bash
streamlit run app.py
#### This will open a local server (usually at http://localhost:8501) in your browser.

----
# User Interface
<img width="1843" height="977" alt="Screenshot 2026-07-07 063700" src="https://github.com/user-attachments/assets/7c354bd2-a531-4a48-b11d-84b5296c9f73" />

# Sample output
<img width="1828" height="862" alt="Screenshot 2026-07-07 060654" src="https://github.com/user-attachments/assets/ce1c1cb6-bdbe-4de3-aa53-9f19429b85a6" />

----
# 👨‍💻 Team Members
```
Baddi Chetan
Chilekam Palli Ganga Dinesh Reddy (Team Lead)
Eragamreddy Kousalya
Dokka Likhitha
Meruva Subha Sankar
```
-----



