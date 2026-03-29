from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotiondetector():
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)
    response = result['response']
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']
    if response == 400:
        return  "Invalid text! Please try again!."
    else:
        return (f"For the given statement, the system response is \'anger\': {anger}, \'disgust\': {disgust}, \'fear\': {fear}, \'joy\': {joy} and \'sadness\': {sadness}. The dominant emotion is {dominant_emotion}.")
    
    
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
