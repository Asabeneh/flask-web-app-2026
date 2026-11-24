from flask import Flask,render_template
from textblob import TextBlob
from utils import fetch_data

blob = TextBlob('AI is such a ridiculous technology that taking everyone\'s job.')
print(blob.sentiment)
# polarity: -1  to 1



url = 'https://hello-flask-hazel.vercel.app/v1/api/cats'
cats = fetch_data(url)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/v1/cats')
def cats_api():
    return cats

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


if __name__ == '__main__':
    app.run()