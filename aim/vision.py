from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

api_key = config("GOOGLE_GEMINI_API_KEY")
vision_model = ChatGoogleGenerativeAI(model="gemini-pro-vision", google_api_key=api_key)
screenshot_file = config("MEDIA_DIR") + "/" + config("SCREENSHOT_FILE")
