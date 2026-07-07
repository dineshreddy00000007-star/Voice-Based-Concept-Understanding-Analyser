import streamlit as st
import json
import os
from models.whisper_model import transcribe_audio


from models.semantic_model import calculate_similarity
from models.scoring import calculate_final_score, generate_feedback

from audio.preprocessing import preprocess_audio
from audio.extractor import extract_audio_features
from audio.waveform import plot_waveform

from nlp.filler_words import detect_filler_words

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)
from database.database import create_database, save_result
from reports.pdf_generator import generate_pdf

create_database()

st.title("🎤 Voice-Based Concept Understanding Analyser")
st.write("Evaluate conceptual understanding using AI.")

# -------------------------------
# Load Reference Concepts
# -------------------------------
with open("reference/concepts.json", "r") as f:
    concepts = json.load(f)

topic = st.selectbox(
    "Select Concept",
    list(concepts.keys())
)

# -------------------------------
uploaded_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3"]
)

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Audio Uploaded Successfully")

    st.audio(file_path)

    # -------------------------------
    # Analyze Button
    # -------------------------------
    if st.button("🔍 Analyze"):

        with st.spinner("Analyzing Audio..."):

            # Preprocess Audio
            processed_audio = preprocess_audio(file_path)

            # Speech-to-Text
            transcript = transcribe_audio(processed_audio)

            # Reference Text
            reference_text = concepts[topic]

            # Semantic Similarity
            similarity = calculate_similarity(
                transcript,
                reference_text
            )

            # Audio Features
            features = extract_audio_features(
                processed_audio
            )

            # Filler Words
            fillers = detect_filler_words(
                transcript
            )

            # Final Score
            final_score = calculate_final_score(
                similarity,
                features["Pause Ratio"],
                features["Average RMS"],
                fillers["percentage"]
            )

            feedback = generate_feedback(
                final_score
            )
            save_result(
    topic,
    transcript,
    similarity,
    final_score,
    feedback
)

        # -------------------------------
        # Results
        # -------------------------------

        st.header("📝 Transcript")
        st.write(transcript)

        st.header("📊 Semantic Similarity")

        st.progress(similarity / 100)

        st.metric(
            "Similarity Score",
            f"{similarity}%"
        )

        st.header("🎙 Audio Features")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Duration",
                f"{features['Duration']} sec"
            )

            st.metric(
                "Average RMS",
                features["Average RMS"]
            )

            st.metric(
                "Pause Ratio",
                features["Pause Ratio"]
            )

        with col2:
            st.metric(
                "Tempo",
                features["Tempo"]
            )

            st.metric(
                "Speaking Rate",
                features["Speaking Rate"]
            )

        st.header("💬 Filler Words")

        st.metric(
            "Count",
            fillers["count"]
        )

        st.metric(
            "Percentage",
            f"{fillers['percentage']}%"
        )

        st.header("🏆 Final Evaluation")

        st.progress(final_score / 100)

        st.metric(
            "Final Score",
            f"{final_score}%"
        )

        st.success(feedback)

        st.header("📈 Waveform")

        fig = plot_waveform(processed_audio)

        st.pyplot(fig)
        pdf_path = generate_pdf(topic,
            transcript,
            similarity, 
            final_score,
            feedback
        )
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_file,
                file_name="VBCUA_Report.pdf",
                mime="application/pdf"
            )