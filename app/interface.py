import gradio as gr
from app.synthesize import generate_tts

def tts_interface(text, speaker, language):
    path = generate_tts(text, speaker, language)
    return path

interface = gr.Interface(
    fn=tts_interface,
    inputs=[
        gr.Textbox(label="Texte à synthétiser"),
        gr.Audio(label="Voix source (WAV)", type="filepath"),
        gr.Dropdown(["fr", "en", "de", "es"], label="Langue", value="fr")
    ],
    outputs=gr.Audio(label="Résultat audio"),
    title="Synthèse vocale avancée",
    description="Génération audio à partir de texte et d'une voix exemple"
)
