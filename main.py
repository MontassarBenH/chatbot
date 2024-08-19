import openai
from flask import Flask, request, render_template

openai.api_key = ""

app = Flask(__name__)

def generate_response(prompt, model="gpt-3.5-turbo"):
    response = openai.chat_completions.create(  
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()  

@app.route("/", methods=["GET", "POST"])
def index():
    bot_response = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = generate_response(user_input)

    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
