from dotenv import load_dotenv
from handlers import enhanced_video_email_handler

def main():
    load_dotenv()
    enhanced_video_email_handler()

if __name__ == "__main__":
    main()