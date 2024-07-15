#Logging
LOGFILE = 'Output.log'
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOGGING_START = 'Logging Initialised'

#FILE_MODE
READ_MODE ='r'
WRITE_MODE = 'w'
APPEND_MODE = 'a+'


HELP_ARGUMENTS = ["-h", "--help"]
HELP_INFO = """
    Usage: python main.py [VIDEO_PATH] [OUTPUT_DIR]
    
    Arguments:
    VIDEO_PATH   Path to the Input_video file to be processed.
    OUTPUT_DIR   Directory where the output files will be saved.

    Description:
    This script reads a video file, transcribes the audio, generates a summary, 
    and provides a topic summary. The outputs are saved in the specified output directory.
    """
INCORRECT_ARGUMENT_MSG = "Incorrect number of arguments."

STR_EFFI_OLLAMA_AUDIO_JSON_FILEPATH = "../audio_text.json"

#Ollama prompts
STR_EFFI_OLLAMA_TIME_SEGMENT_PROMPT = "The text script is from a gameshow with host contestants playing different games. \
    Your goal is to very briefly summarize this segment of the video transcript providing all the necessary information.\
     Do not provide any headers in the output."

STR_EFFI_OLLAMA_SUMMARY_PROMPT = "The text script is from a gameshow with host contestants playing different games. \
    Your goal is to descriptively summarize this video transcript providing the details. Provide it in 60 lines "    

COMBINE_SUMMARY_PROMPT = "Combine these summaries of different segments of a video transript to make coherent. Keep the length of the text same."


OUTPUT_AUDIO_PATH = "output_audio.wav"

MODEL_TYPE = "base" # Whisper model type 

DB_CONFIG = {
    'host': 'localhost',
    'database': 'EFFI_AI_DB',
    'user': 'root',
    'password': 'ngi@12345678',
    'auth_plugin': 'mysql_native_password'
}

INSERT_QUERY_VIDEO_SUMMARY = """
INSERT INTO VideoAnalytics (VideoName, VideoURL, VideoTranscirpt, VideoSummary, VideoTimeSegmentedSummary)
VALUES (%s, %s, %s, %s, %s)
"""

VIDEO_URL = "https://www.youtube.com"

SUMMARY_CHUNK_SIZE = 600
SUMMARY_CHUNK_START = 0 
SEGMENT_INITIALIZER = float('inf')
SUMMARY_SEGMENT_END = 0

SUMMARY_TEXT = 'text'
SUMMARY_START = 'start'
SUMMARY_END = 'end'
SUMMARY_SEGMENTS = "segments"

TRANSCRIPTION_OUTPUT = "transcription.txt"
SUMMARY_OUTPUT = "summary.txt"
TOPIC_SUMMARY_OUTPUT  = "topic_summary.txt"

OLLAMA_COMMAND = ["ollama", "run", "llama3"]

READ_VIDEO = "Reading video..."
GET_TRANSCRIPTION = "Getting transcription..."
GET_SUMMARY = "Generating summary..."
GET_TOPIC_SUMMARY = "Generating topic summary..."
DB_SAVE_MSG = "Data saved to database successfully"