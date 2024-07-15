'utils.py'
import mysql.connector # type: ignore
import CommonConstants as const

def save_output(file_path, content):
    with open(file_path, const.WRITE_MODE) as file:
        file.write(content)



def save_to_database(video_name, video_url, transcription, summary, topic_summary):
    # Connect to the database
    conn = mysql.connector.connect(**const.DB_CONFIG)

    cursor = conn.cursor()

    sql = const.INSERT_QUERY_VIDEO_SUMMARY
    data = (video_name, video_url, transcription, summary, topic_summary)

    cursor.execute(sql, data)
    
    # Commit the transaction
    conn.commit()
    
    # Closing the cursor
    cursor.close()
    conn.close()
