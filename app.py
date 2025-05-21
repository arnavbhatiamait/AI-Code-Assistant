import streamlit as st 
import requests
import subprocess
def get_ollama_models():
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        models = []

        # Skip header row (assumes first row contains column headers)
        for line in lines[1:]:
            # Typically, model name is the first column
            parts = line.split()
            if parts:
                models.append(parts[0])

        return models
    except subprocess.CalledProcessError as e:
        print("Error running 'ollama list':", e)
        print("Output:", e.stdout)
        print("Error Output:", e.stderr)
ollama_model_avl=get_ollama_models()
euri_ai_models=["gpt-4.1-nano","gpt-4.1-mini","gemini-2.5-pro-exp.03-25","gemini-2.0-flash-001","llama-4-scout-17b-16e-instruct","llama-4-maverick-17b-128e-instruct","deepseek-r1-distill-llama-70b","qwen-qwq-32b","mistral-saba-24b"]

st.title("CoderAI: AI coding Assitant for Student with free API key")

language = st.selectbox(
    "Select Language",
    ["Python", "JavaScript", "Java", "C++", "Ruby", "Go","C"]
)
topic = st.text_input("enter the topic")
level = st.selectbox(
    "Select Level",
    ["Beginner", "Intermediate", "Advanced"]
)
model=st.selectbox("Select Model Type",["Local","API"])
model_name=None
if model=="Local":
    model_name=st.selectbox("Select Model Name",
                         options=ollama_model_avl)
else:
    model_name=st.selectbox("Select Model Name",options=euri_ai_models)

API_URL = "http://127.0.0.1:8000"


def fetch_response(endpoint, paylaod):
    try:
        response = requests.post(f"{API_URL}/{endpoint}", json=paylaod)
        response_data = response.json()
        if "response" in response_data:
            return response_data["response"]
        else:
            st.error("⚠️ Unexpected API Response Format!")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"🚨 API Request Failed: {e}")
        return None


if st.button("Explain_code"):
    explanation = fetch_response("explain", {"language": language, "topic": topic, "level": level,"model":model,"model_name":model_name})
    if explanation:
        st.markdown("### 📖 Explanation:")
        st.markdown(explanation)


if st.button("Debug Code"):
    response = fetch_response("debug", {"language": language, "topic": topic, "level": level,"model":model,"model_name":model_name})
    if response:
        st.markdown("### 🛠 Debugging:")
        st.markdown(response)

if st.button("Generate Code"):
    generated_code = fetch_response("generate", {"language": language, "topic": topic, "level": level,"model":model,"model_name":model_name})
    if generated_code:
        st.markdown("### 💡 Code Example:")
        st.markdown(generated_code)