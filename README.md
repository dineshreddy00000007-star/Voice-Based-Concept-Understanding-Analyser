# 🎤 Voice-Based Concept Understanding Analyser (VBCUA)

## 📌 Overview

The Voice-Based Concept Understanding Analyser (VBCUA) is an AI-powered web application that evaluates how effectively users explain conceptual topics through speech.

The application uses Speech-to-Text, Semantic Similarity Analysis, and Audio Feature Extraction to assess conceptual understanding, communication quality, and speaking fluency.

It is built using Python and Streamlit and integrates OpenAI Whisper, Sentence-BERT, Librosa, and ReportLab.

---

## 🚀 Features

- 🎙 Audio Upload (.wav/.mp3)
- 📝 Speech-to-Text using OpenAI Whisper
- 🧠 Semantic Similarity using Sentence-BERT
- 📊 Audio Feature Extraction (Duration, RMS, Tempo, Pause Ratio)
- 💬 Filler Word Detection
- ⭐ AI-Based Scoring Engine
- 📈 Waveform Visualization
- 📄 PDF Report Generation
- 💾 SQLite Database for Result Storage
- 🌐 Interactive Streamlit Dashboard

---

## 🛠 Technologies Used

- Python
- Streamlit
- OpenAI Whisper
- Sentence-Transformers
- Librosa
- NumPy
- Matplotlib
- ReportLab
- SQLite
- Torch
- NLTK

---

## 📂 Project Structure

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

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/dineshreddy00000007-star/Voice-Based-Concept-Understanding-Analyser.git

cd Voice-Based-Concept-Understanding-Analyser
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Project

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📋 Usage

1. Select a concept.
2. Upload an audio file.
3. Click **Analyze**.
4. View:
   - Transcript
   - Semantic Similarity Score
   - Audio Features
   - Filler Word Analysis
   - Final Score
   - Feedback
5. Download the generated PDF report.

---

## 📊 Workflow

```
Audio Upload
      │
      ▼
Audio Preprocessing
      │
      ▼
Speech-to-Text (Whisper)
      │
      ▼
Semantic Similarity (Sentence-BERT)
      │
      ▼
Audio Feature Extraction
      │
      ▼
Filler Word Detection
      │
      ▼
Scoring Engine
      │
      ▼
PDF Report & Dashboard
```

---

## 📸 Screenshots

## screenshots:
### Home Page
- <img width="1843" height="977" alt="Screenshot 2026-07-07 063700" src="https://github.com/user-attachments/assets/06019753-6b74-472c-abb2-c32f219888d7" />
### Audio Upload
<img width="1813" height="790" alt="Screenshot 2026-07-07 065608" src="https://github.com/user-attachments/assets/7ba46d2e-4ba2-40eb-b81a-2cbe3d9cc4ad" />
### Analysis Results
<img width="1812" height="887" alt="Screenshot 2026-07-07 065742" src="https://github.com/user-attachments/assets/d2d5ad0c-d95f-410b-9576-aba50d41975e" />
### Waveform
<img width="1828" height="862" alt="Screenshot 2026-07-07 060654" src="https://github.com/user-attachments/assets/9104b131-1b7b-4d24-8cd5-0a6533f0d684" />
- PDF Report
<img width="1601" height="965" alt="Screenshot 2026-07-07 070001" src="https://github.com/user-attachments/assets/17d21d91-d1d4-4dbb-9d5c-38d85198873f" />

----

# 🚀 Launch Application
## Make sure your virtual environment (.venv) is activated:
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
#  ** Voice-Based Concept Understanding Analyser (VBCUA) Project **
## 👨‍💻 Team Members
```
Baddi Chetan
Chilekam Palli Ganga Dinesh Reddy (Team Lead)
Eragamreddy Kousalya
Dokka Likhitha
Meruva Subha Sankar
```
-----


## 📄 License

This project is developed for educational purposes as part of the Google Cloud Generative AI Skill Wallet program.

---

## 🙏 Acknowledgements

- OpenAI Whisper
- Sentence-Transformers
- Streamlit
- Librosa
- ReportLab
- Google Cloud Generative AI Skill Wallet



