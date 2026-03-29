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
    return (f"For the given statement, the system response is {result}")

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
