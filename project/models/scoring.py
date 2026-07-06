def calculate_final_score(similarity, pause_ratio, rms, filler_percentage):
    """
    Calculate final score based on:
    - Semantic similarity (60%)
    - Pause ratio (15%)
    - RMS energy (15%)
    - Filler words (10%)
    """

    # Semantic Score (0-60)
    semantic_score = similarity * 0.60

    # Pause Score (0-15)
    if pause_ratio < 0.10:
        pause_score = 15
    elif pause_ratio < 0.20:
        pause_score = 12
    elif pause_ratio < 0.30:
        pause_score = 8
    else:
        pause_score = 4

    # RMS Score (0-15)
    if rms > 0.05:
        rms_score = 15
    elif rms > 0.03:
        rms_score = 12
    else:
        rms_score = 8

    # Filler Score (0-10)
    if filler_percentage < 5:
        filler_score = 10
    elif filler_percentage < 10:
        filler_score = 8
    elif filler_percentage < 20:
        filler_score = 5
    else:
        filler_score = 2

    final_score = semantic_score + pause_score + rms_score + filler_score

    return round(min(final_score, 100), 2)


def generate_feedback(score):
    """
    Generate qualitative feedback.
    """

    if score >= 85:
        return "🌟 Excellent Understanding"

    elif score >= 70:
        return "✅ Good Understanding"

    elif score >= 50:
        return "⚠ Moderate Understanding"

    else:
        return "❌ Poor Understanding. Please improve conceptual clarity and communication."