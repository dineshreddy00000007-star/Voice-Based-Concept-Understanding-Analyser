from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os

def generate_pdf(
        topic,
        transcript,
        similarity,
        final_score,
        feedback):

    os.makedirs("outputs", exist_ok=True)

    filename = "outputs/VBCUA_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Voice-Based Concept Understanding Analyser</b>", styles['Title']))
    story.append(Paragraph(f"<b>Topic:</b> {topic}", styles['Normal']))
    story.append(Paragraph(f"<b>Transcript:</b> {transcript}", styles['Normal']))
    story.append(Paragraph(f"<b>Semantic Similarity:</b> {similarity}%", styles['Normal']))
    story.append(Paragraph(f"<b>Final Score:</b> {final_score}%", styles['Normal']))
    story.append(Paragraph(f"<b>Feedback:</b> {feedback}", styles['Normal']))

    doc.build(story)

    return filename