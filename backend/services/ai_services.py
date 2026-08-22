from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.getenv("NVIDIA_API_KEY")

client = ChatNVIDIA(
  model="meta/muse-glimmer-30b",
  api_key=API_KEY, 
  temperature=1,
  top_p=0.95,
  max_completion_tokens=8192,
)



def generate_title(content: str):
    response = client.invoke(
        f"""
        Generate a suitable title for this note.

        Rules:
        - Maximum 6 words
        - Keep it as short as possible
        - Return only the title
        - No quotation marks

        Note:
        {content}
        """
        )

    return response.content.strip()

def generate_summary(content: str):
    response = client.invoke(
        f"""
        Summarize the following note concisely.

        Rules:
        - Include all important details
        - Preserve dates, times, deadlines, names and important numbers
        - Do not invent information
        - Keep it concise
        - Return only the summary

        Note:
        {content}
        """
    )

    return response.content.strip()

def combined_summary(contents: list[str]):
    combined_content = "\n\n--- NOTE ---\n\n".join(contents)

    response = client.invoke(
        f"""
        Create a concise combined summary of the following notes.

        Rules:
        - Include important information from every note
        - Preserve dates, times, deadlines, names and important numbers
        - Do not invent information
        - Remove unnecessary repetition
        - Return only the summary

        Notes:
        {combined_content}
        """
    )

    return response.content.strip()
