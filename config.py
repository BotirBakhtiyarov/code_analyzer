import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
    MAX_FILE_SIZE = 5000000  # 1MB
    SUPPORTED_EXTENSIONS = {
        '.py', '.js', '.java', '.c', '.cpp', '.h', '.hpp',
        '.html', '.css', '.php', '.rb', '.go', '.rs'
    }
    REQUEST_TIMEOUT = 30