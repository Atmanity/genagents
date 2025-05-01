import os
from pathlib import Path

from ...utils import config

OPENAI_API_KEY = os.getenv(
            "OPENAI_API_KEY") if not config.speech_generator.api_key else config.speech_generator.api_key
KEY_OWNER = "atmanity"


DEBUG = False

MAX_CHUNK_SIZE = 4

LLM_VERS = "gpt-4o-mini"

BASE_DIR = f"{Path(__file__).resolve().parent.parent}"

## To do: Are the following needed in the new structure? Ideally Populations_Dir is for the user to define.
POPULATIONS_DIR = f"{BASE_DIR}/agent_bank/populations" 
LLM_PROMPT_DIR = f"{BASE_DIR}/simulation_engine/prompt_template"