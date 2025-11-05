import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)


def main():
  client.models.generate_content("gemini-2.0-flash-001", "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    return print(GenerateContentResponse.text())
    return print(GenerateContentResponse.usage_metadata())


if __name__ == "__main__":
    main()
