from flask import Flask, render_template, request
from textblob import TextBlob
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('content')
        
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0.1:
            mood = "Positive 😊"
            color = "#d4edda"
        elif polarity < -0.1:
            mood = "Negative 😔"
            color = "#f8d7da"
        else:
            mood = "Neutral 😐"
            color = "#e2e3e5"
            
        new_post = Post(text=text, mood=mood, color=color)
        db.session.add(new_post)
        db.session.commit()
        
    all_posts = Post.query.order_by(Post.id.desc()).all()
    
    return render_template('index.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)