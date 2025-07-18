import os
import re
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY is not None:
  os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
else:
  raise ValueError("Google API Key not found.")

client = genai.Client()
language = "java"
user_prompt = "Write a code for dfs traversal in a graph."
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""You are a helpful coding assistant. Your task is to genenrate code based on the user prompt for the following language:-
    {language}
    User input: {user_prompt}
    """,
)


response_json = response.model_dump_json()
parsed = json.loads(response_json)
text = parsed["candidates"][0]["content"]["parts"][0]["text"]
code_blocks = re.findall(r"```(?:[a-zA-Z0-9]+)?\n(.*?)```", text, re.DOTALL)
for idx, block in enumerate(code_blocks, start=1):
    print(f"\n🔹 Code Block {idx}:\n")
    print(block.strip())