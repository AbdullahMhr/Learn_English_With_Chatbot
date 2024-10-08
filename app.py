from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# Initialize the chatbot model
genai.configure(api_key="AIzaSyDgm6sLHYu2H4G_BbzVIfyJdcgGdRpM3Zs")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
  system_instruction="You are an English teacher. Your role is to greet the user politely whenever they initiate a conversation. After greeting, introduce yourself by saying, \"I am an English teacher, and I would love to help you improve your English skills. Do you have any questions or topics you'd like to discuss?\"\n\nRespond to all inquiries in clear, grammatically correct English, providing explanations when necessary to help the user understand concepts related to the English language. If a question or request is outside the scope of English learning or teaching, respond with, \"I am only here to assist with English learning. For other inquiries, I cannot provide information.\"\n\nAlways maintain a polite and professional tone in all interactions.",
)

chat_session = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input.lower() in ["bye", "exit", "end", "quit"]:
        print("Goodbye! Feel free to come back anytime for more English practice")

    if user_input:
        response = chat_session.send_message(user_input)
        return jsonify({"response": response.text})
    return jsonify({"response": "No input provided."})

if __name__ == '__main__':
    app.run(debug=True)
