import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("[cAIt]: Hiss! GEMINI_API_KEY is missing or not valid.")

client = genai.Client(api_key=api_key)

def main():
    print("Hello from cAIt!")

    response = client.models.generate_content(model="gemini-2.5-flash",
                                              contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    print(response.text)


if __name__ == "__main__":
    main()
