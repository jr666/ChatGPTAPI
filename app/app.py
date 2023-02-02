import os
import logging
import logging.handlers
from datetime import datetime

import openai
from flask import Flask, redirect, render_template, request, url_for
# Start Flask server by typing: flask run

flask_logs = os.getenv("LOG_PATH")
chat_logs = os.getenv("CHAT_PATH")

handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", flask_logs))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
logging.info("Got API Key")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # Get datetime of start
        curr_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_out(curr_datetime)

        prompt_input = request.form["prompt_input"]
        logging.info(f"Prompt input: {prompt_input}")
        write_out(f"Prompt: {prompt_input}")

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(prompt_input),
            temperature=0.6,
            max_tokens=1024,
            n=2,
            stop=None,
        )
        logging.info(f"Response: {response}")
        # Write resulting text to history file
        for i, p in enumerate(response.choices):
            write_out(f"choices[{i}]")
            write_out(response.choices[i].text)
        return redirect(url_for("index", result=response.choices[0].text, prompt=prompt_input))

    result = request.args.get("result")
    prompt = request.args.get("prompt")
    return render_template("index.html", result=format_str(result), prompt=prompt)

def write_out(string):
    file = open(chat_logs, "a")
    file.write(f"{string}\n")
    file.close()

def generate_prompt(prompt_input):
    return """{}""".format(
        prompt_input.capitalize()
    )

def format_str(in_string):
    """Replaces '\n' with </br> to properly display the string in
    an html file
    """
    if in_string != None:
        return "<br>".join(in_string.split("\n"))
    return in_string