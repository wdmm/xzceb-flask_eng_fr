import json
from machinetranslation.translator import english_to_french,french_to_english
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return english_to_french(textToTranslate)['translations'][0]['translation']

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return french_to_english(textToTranslate)['translations'][0]['translation']

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template(
        'index.html'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

