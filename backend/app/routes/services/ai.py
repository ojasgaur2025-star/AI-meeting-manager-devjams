import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcriptions.create(
            model="whisper-1", file=audio_file
        )
    return transcript["text"]

def summarize_text(text: str, speaker: str = None) -> str:
    prompt = "Summarize the following meeting transcript."
    if speaker:
        prompt += f" Focus only on what {speaker} said."
    prompt += f"\n\n{text}"

    response = openai.Chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
