
# 🧠 AI-Powered Code Writer

This is a Streamlit-based AI coding assistant powered by Gemini 2.5 Pro (via Google's GenAI API). It generates clean and working code in your favorite programming language based on your custom prompt — with a built-in copy-to-clipboard feature for effortless coding.



## Features
1. ✅ Generate code using natural language prompts
2. ✅ Choose from multiple languages: Python, C++, Java, JavaScript
3. ✅ Powered by Gemini 2.5 Flash for fast, reliable code generation
4. ✅ Easily copy code blocks with a single click
5. ✅ Interactive and user-friendly Streamlit UI

## Tech Stack
1. Frontend & Interface: Streamlit
2. Language Model: Gemini 2.5
3. Environment Config: Python .env via python-dotenv
4. Other Tools: RegEx, HTML injection for clipboard copy functionality
## Setup Instructions

### Step 1. Clone the repository

```bash
git clone https://github.com/Aditya26Das/AICodingAssistant.git
cd AICodingAssistant
```

### Step 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Step 3. Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4. Configure your .env file
Create a .env file in the root directory and **add your own Google Generative AI API Key**:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### Step 5. Run your Streamlit App

```bash
streamlit run app.py
```


## Example Usage

1. Select your preferred language (e.g., Python)
2. Enter a prompt like: **Write a code for DFS traversal in a graph**
3. Click 🚀 Generate Code
4. Copy the generated code using the 📋 button
## How it Works ?
1. The app collects the prompt and target language from the user
2. Sends a prompt to Gemini 2.5 Flash model using Google GenAI API
3. Parses the response and extracts code blocks using RegEx
4. Displays code in syntax-highlighted sections with a **Copy Code** button