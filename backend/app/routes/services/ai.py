from transformers import pipeline

# Load summarization and transcription models
summarizer = pipeline("summarization")
transcriber = pipeline("automatic-speech-recognition")

def transcribe_audio(audio_file_path):
    return transcriber(audio_file_path)["text"]

def summarize_text(text):
    return summarizer(text, max_length=150, min_length=30, do_sample=False)[0]["summary_text"]

def extract_action_items(text):
    # Simple keyword-based extraction
    return [line for line in text.split('\n') if any(kw in line.lower() for kw in ["action", "todo", "task", "deadline"])]
