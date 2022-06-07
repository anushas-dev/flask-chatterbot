from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

app = Flask(__name__)

chatbot = ChatBot(
    "KubeBot",
    read_only=True,
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch",
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, I do not understand. But I keep learning everyday',
            'maximum_similarity_threshold': 0.80
        }
    ],    
    database_uri="sqlite:///database.sqlite3",
)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./data")
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
