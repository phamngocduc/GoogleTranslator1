from flask import Flask,render_template
from googletrans import Translator
app=Flask(__name__,template_folder='template')
translator = Translator()

def msgtranslator(textmessage):
    translated = translator.translate(textmessage, src='en', dest='vi')
    return translated.text

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def trans():
   message = None
   if request.method == 'GET':
        datafromjs = request.form['m']
        #result = "return this"
        #resp = make_response('{"response": '+result+'}')
        resp.headers['Content-Type'] = "application/json"
        return resp
        return render_template('home.html', message= msgtranslator(datafromjs))


if __name__=="__main__":
    app.run(debug=True)