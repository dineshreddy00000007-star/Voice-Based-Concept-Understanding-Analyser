import re

FILLER_WORDS = [
    "um", "uh", "like", "actually",
    "basically", "you know", "so", "well"
]

def detect_filler_words(transcript):
    transcript = transcript.lower()

    filler_count = 0

    for word in FILLER_WORDS:
        filler_count += len(re.findall(r'\b' + re.escape(word) + r'\b', transcript))

    total_words = len(transcript.split())

    percentage = 0
    if total_words > 0:
        percentage = round((filler_count / total_words) * 100, 2)

    return {
        "count": filler_count,
        "percentage": percentage
    }