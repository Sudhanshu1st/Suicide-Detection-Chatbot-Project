from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get("input")
    print("User input:", user_input)
    chat_response = generate_chat_response(user_input)
    print("Chat response:", chat_response)
    return chat_response

def generate_chat_response(user_input):
    # Replace "YOUR_API_KEY" with your GPT-3 API key
    openai.api_key = "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"

    prompt = f"You: {user_input}\nMitra:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3 engine
        prompt=prompt,
        max_tokens=50  # Set the desired response length
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
