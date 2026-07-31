from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    post_data = None
    
    # If the user clicked the "Publish Post" button:
    if request.method == 'POST':
        # Grab the text they typed into the box
        text = request.form.get('content')
        
        # AI Magic: Analyze the sentiment
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        # Assign a mood and a background color based on the AI's score
        if polarity > 0.1:
            mood = "Positive 😊"
            color = "#d4edda" # Light green
        elif polarity < -0.1:
            mood = "Negative 😔"
            color = "#f8d7da" # Light red
        else:
            mood = "Neutral 😐"
            color = "#e2e3e5" # Light grey
            
        # Bundle it all up to send to the HTML page
        post_data = {
            "text": text,
            "mood": mood,
            "color": color
        }
        
    # Send the bundled data to our index.html template
    return render_template('index.html', post_data=post_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)