import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)


def main():
  if len(sys.argv) > 1:
    user_prompt = sys.argv[1]
  else: 
    print("Prompt arguement required.")
    sys.exit(1)
  resp =client.models.generate_content(model="gemini-2.0-flash-001", contents=user_prompt)
  return print(f"{resp.text}\nPrompt tokens: {resp.usage_metadata.prompt_token_count}\nResponse tokens: {resp.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
