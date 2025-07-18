import streamlit as st
import os
import re
import json
import streamlit.components.v1 as components
from google import genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is not None:
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
else:
    st.error("Google API Key not found. Please set it in the .env file.")
    st.stop()

client = genai.Client()
st.title("🧠 AI Coding Assistant")
st.markdown("Generate code in your favorite language using Gemini 2.5 Pro")
language = st.selectbox("Choose a programming language:", ["python", "c++", "java", "javascript"])
user_prompt = st.text_area("Describe the code you want me to generate:", 
                           "Write a code for DFS traversal in a graph.")

if st.button("🚀 Generate Code"):
    with st.spinner("Generating code..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""You are a helpful coding assistant. Your task is to generate code based on the user prompt for the following language:
{language}
User input: {user_prompt}
"""
            )
            response_json = response.model_dump_json()
            parsed = json.loads(response_json)
            text = parsed["candidates"][0]["content"]["parts"][0]["text"]

            code_blocks = re.findall(r"```(?:[a-zA-Z0-9]+)?\n(.*?)```", text, re.DOTALL)

            if code_blocks:
                for idx, block in enumerate(code_blocks, start=1):
                    block_clean = block.strip()

                    st.markdown(f"### 🔹 Code Block {idx}")
                    st.code(block_clean, language=language)

                    print(f"\n🔹 Code Block {idx}:\n{block_clean}\n")
                    copy_button = f"""
                    <div style="position: relative;">
                        <textarea id="codeBlock{idx}" style="position: absolute; left: -9999px;">{block_clean}</textarea>
                        <button onclick="navigator.clipboard.writeText(document.getElementById('codeBlock{idx}').value)" style="
                            background-color: #4CAF50;
                            color: white;
                            padding: 6px 12px;
                            margin: 4px 0;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                        ">📋 Copy Code</button>
                    </div>
                    """
                    components.html(copy_button, height=40)
            else:
                st.warning("No code blocks found in the response.")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            print(f"❌ Exception occurred: {str(e)}")

