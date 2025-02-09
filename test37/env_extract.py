import os
from dotenv import load_dotenv
from dataclasses import dataclass

@dataclass
class ENV:
    TOKEN: str
    COMMAND_START: str
    DS_LINK: str
    DS_AUTH: str
    CHAT_ID: int
    THEME_ID: int


def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

def get_env():
    return ENV(
        TOKEN=os.getenv('TOKEN'),
        COMMAND_START=os.getenv('COMMAND_START'),
        DS_LINK=os.getenv('DS_LINK'),
        DS_AUTH=os.getenv('DS_AUTH'),
        CHAT_ID=os.getenv('CHAT_ID'),
        THEME_ID=os.getenv('THEME_ID')
    )
    
if __name__ == '__main__':
    pass