"""File: main.py
------------------
This script is used to get the transcription of a video, and provide full summary and time segmented summary. 

Author: Shikhar Saxena
Date: 3 June 2024

Description:
This script performs the following steps: 
    1. Reads the Video file (.mp4)
    2. Generates the transcription of video 
    3. Summarize the transcription
    4. Provide the time-segmented summary of the transcription

Usage: python main.py path_to_your_video_file.mp4 output_directory

The script utilises the following libraries:
    1. whisper
    2. moviepy
    3. ollama installed in the system
    
"""
import os
import sys
import CommonConstants as const
from video_processing import read_video
from transcription_util import get_transcription
from summarisation_util import get_summary
from topicSummary_util import get_topic_summary
import utils
import logging
from importlib import reload
reload(const)

# Define logger as a global variable
logger = None

def setup_logging():
    global logger  # Use the global logger variable
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Remove all handlers associated with the logger object
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # File handler
    file_handler = logging.FileHandler(const.LOGFILE)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(const.LOGGING_FORMAT)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(const.LOGGING_FORMAT)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    logger.info(const.LOGGING_START)  


def print_help():
    global logger
    help_text = const.HELP_INFO
    logger.info(help_text)

def main(video_path, output_dir):
    global logger
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    logger.info(const.READ_VIDEO)
    video_content = read_video(video_path)
    
    # Generate Transcription
    logger.info(const.GET_TRANSCRIPTION)
    transcription, json_file = get_transcription(video_content, output_dir)
    transcription_path = os.path.join(output_dir, const.TRANSCRIPTION_OUTPUT)
    logger.info(f"Saving transcription to {transcription_path}...")
    utils.save_output(transcription_path, transcription)

    # Generate Topic Summary
    logger.info(const.GET_TOPIC_SUMMARY)
    topic_summary, summary_text = get_topic_summary(json_file)
    topic_summary_path = os.path.join(output_dir, const.TOPIC_SUMMARY_OUTPUT)
    logger.info(f"Saving topic summary to {topic_summary_path}...")
    utils.save_output(topic_summary_path, topic_summary)

    # Generate Summary
    logger.info(const.GET_SUMMARY)
    summary = get_summary(summary_text)
    summary_path = os.path.join(output_dir, const.SUMMARY_OUTPUT)
    logger.info(f"Saving summary to {summary_path}...")
    utils.save_output(summary_path, summary)

    # Adding to the mysql database "EFFI_AI_DB"
    video_name = video_path
    video_url = const.VIDEO_URL

    utils.save_to_database(video_name, video_url, transcription, summary, topic_summary)

    logger.info(const.DB_SAVE_MSG)

    logger.info("Process completed successfully.")

if __name__ == "__main__":

    setup_logging()

    if len(sys.argv) > 1 and sys.argv[1] in const.HELP_ARGUMENTS:
        print_help()
        sys.exit(0)

    elif len(sys.argv) != 3:
        logger.error(const.INCORRECT_ARGUMENT_MSG)
        print_help()
        sys.exit(1)
           
    video_path = sys.argv[1]
    output_dir = sys.argv[2]
    
    main(video_path, output_dir)
    