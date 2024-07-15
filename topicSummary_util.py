import sys
import subprocess
import logging
import CommonConstants as const

#logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=const.LOGGING_FORMAT)
logger = logging.getLogger(__name__)

def convert_seconds_to_mmss(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes):02}:{int(seconds):02}"

def preprocessing(input_file):
    audio_file = input_file

    text_chunk = []
    timestamp = []

    chunk_size = const.SUMMARY_CHUNK_SIZE
    current_chunk_start = const.SUMMARY_CHUNK_START
    current_chunk_end = chunk_size

    segment_text = []
    segment_start = const.SEGMENT_INITIALIZER
    segment_end = const.SUMMARY_SEGMENT_END

    for segment in audio_file[const.SUMMARY_SEGMENTS]:
        start = segment[const.SUMMARY_START]
        end = segment[const.SUMMARY_END]
        text = segment[const.SUMMARY_TEXT]

        # Check if the segment is within the current chunk
        if start >= current_chunk_start and end <= current_chunk_end:
            segment_text.append(text)
            segment_start = min(segment_start, start)
            segment_end = max(segment_end, end)
        else:
            # If the segment is outside the current chunk, finalize the current chunk
            if segment_text:
                text_chunk.append("".join(segment_text))
                timestamp.append(f"{convert_seconds_to_mmss(segment_start)}-{convert_seconds_to_mmss(segment_end)}")
            
            # Start a new chunk
            current_chunk_start = current_chunk_end
            current_chunk_end += chunk_size
            segment_text = [text]
            segment_start = start
            segment_end = end

    # Append the last chunk if any
    if segment_text:
        text_chunk.append("".join(segment_text))
        timestamp.append(f"{convert_seconds_to_mmss(segment_start)}-{convert_seconds_to_mmss(segment_end)}")
    return timestamp, text_chunk

ye