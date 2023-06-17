from dotenv import load_dotenv
from handlers import fcm_handler

def main():
    load_dotenv()
    fcm_handler()

if __name__ == "__main__":
    main()