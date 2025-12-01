import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from functions.get_files_info import available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
  

  
  
  if len(sys.argv) < 2: 
    print("Prompt argument required.")
    sys.exit(1)
  else:
    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv[2:]
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    resp =client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
    if verbose:
      print(f"User prompt: {user_prompt}\nPrompt tokens: {resp.usage_metadata.prompt_token_count}\nResponse tokens: {resp.usage_metadata.candidates_token_count}")
    else:
      if not resp.function_calls:
          print(resp.text)
      else:
          for function_call_part in resp.function_calls:
              print(f"Calling function: {function_call_part.name}({function_call_part.args})")



  # return print(f"{resp.text}\nPrompt tokens: {resp.usage_metadata.prompt_token_count}\nResponse tokens: {resp.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
