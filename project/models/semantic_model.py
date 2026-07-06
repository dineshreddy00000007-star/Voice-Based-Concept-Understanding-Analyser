from sentence_transformers import SentenceTransformer, util

# Load Sentence-BERT model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(transcript, reference_text):
    """
    Calculate semantic similarity between transcript and reference text.
    Returns a similarity percentage (0–100).
    """

    emb1 = model.encode(transcript, convert_to_tensor=True)
    emb2 = model.encode(reference_text, convert_to_tensor=True)

    similarity = util.cos_sim(emb1, emb2)

    score = float(similarity[0][0]) * 100

    # Limit score to 0–100
    score = max(0, min(score, 100))

    return round(score, 2)
