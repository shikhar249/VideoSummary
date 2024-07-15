import sys
import subprocess
import logging

import CommonConstants as const

logger = logging.getLogger(__name__)

def get_summary(topic_summary_text):
    try:
        prompt2 = const.COMBINE_SUMMARY_PROMPT
        command = const.OLLAMA_COMMAND + [prompt2]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=topic_summary_text.encode())
        output = stdout.decode()
    
    except subprocess.CalledProcessError as e:
        # Handle errors in the command execution
        logger.info("Command failed with return code:", e.returncode, file=sys.stderr)
        logger.info("Error output:", e.stderr, file=sys.stderr)

    except Exception as e:
        logger.info("An unexpected error occurred:", str(e), file=sys.stderr)

    return output

