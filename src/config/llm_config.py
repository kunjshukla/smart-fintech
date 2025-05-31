import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Google Cloud project ID and location (required for Vertex AI)
project_id = os.getenv("GOOGLE_CLOUD_PROJECT_ID", "your-project-id")  # Replace with your project ID
location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")  # Replace with your location

# Initialize Google Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7, google_api_key=google_api_key)

# AutoGen configuration for Gemini via Vertex AI
autogen_config = {
    "config_list": [
        {
            "model": "gemini-1.5-pro",
            "api_key": google_api_key,
            "api_type": "google",
            "base_url": None,
            "project_id": project_id,  # Required for Vertex AI
            "location": location       # Required for Vertex AI
        }
    ]
}

def get_llm():
    return llm

def get_autogen_config():
    return autogen_config