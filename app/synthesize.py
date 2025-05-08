# app/synthesize.py
from TTS.api import TTS

tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts")

def generate_tts(text, speaker_wav_path, language="fr", output_path="static/output.wav"):
    tts.tts_to_file(text=text, speaker_wav=speaker_wav_path, language=language, file_path=output_path)
    return output_path