import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

#loads the API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("[cAIt]: Hiss! GEMINI_API_KEY is missing or not valid.")

#sets the genai client
client = genai.Client(api_key=api_key)

#enables parsing of arguments. used mainly for prompt but also to turn verbose response on or off

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")


parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

#stores messages
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


#That's the mAIn of cAIt!
def main():
    print("Hello from cAIt!")

    #calling the API requesting the response based on prompt
    response = client.models.generate_content(model="gemini-2.5-flash",
                                              contents=messages)
    
    #response metadata
    prompt_tokens = response.usage_metadata.prompt_token_count
    respones_tokens = response.usage_metadata.candidates_token_count
    

    if args.verbose:
        print("--- VERBOSE OUTPUT ---")
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {respones_tokens}")
        print("----------------------")
    print(response.text)


if __name__ == "__main__":
    main()
