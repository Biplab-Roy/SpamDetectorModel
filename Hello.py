from flask import Flask, render_template, flash, redirect, url_for
from Forms import ContactForm
import pickle

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
def predict(msg):
    model = pickle.load(open('SpamDetector/trainedModel.pkl', "rb"))
    transform = pickle.load(open('SpamDetector/transform.pkl', "rb"))
    stemmer = PorterStemmer()
    msg = re.sub('[^a-zA-Z]'," ",msg)
    words = msg.lower().split()
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    msg = ' '.join(words)
    msg = [msg,]
    p = transform.transform(msg).toarray()
    return model.predict(p)[0]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e33166cbb4feeeac1bb7d2c7257b44c5'

@app.route('/', methods = ['GET','POST'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        msg = {form.message.data}.pop()
        out = predict(msg)
        if out == 0:
            flash(f'Message was sent, not a spam message','success')
        else:
            flash(f'Message was not sent, detetcted as spam message','danger')
        return redirect('result')
    return render_template('home.html', form = form)

@app.route('/result')
def result():
    return render_template('result.html')

if  __name__ == "__main__":
    app.run()