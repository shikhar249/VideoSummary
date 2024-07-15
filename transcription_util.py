import os
import whisper #type: ignore
import CommonConstants as const

def get_transcription(video_content, output_dir):
    audio_clip = video_content.audio
    audio_file = os.path.join(output_dir, const.OUTPUT_AUDIO_PATH)
    audio_clip.write_audiofile(audio_file)
    model = whisper.load_model(const.MODEL_TYPE)
    result_json = model.transcribe(audio_file)
    text = [items[const.SUMMARY_TEXT] for items in result_json[const.SUMMARY_SEGMENTS]]
    combined_text = ' '.join(text)
    return combined_text, result_json