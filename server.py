''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its 
        scores for the provided text.
    '''
    # Get the JSON data from the request
    text_to_analyze = request.args.get('textToAnalyze')

    # Process the statement using the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Format and return response
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again."
    message_1 = f"For the given statement, the system response is 'anger': {result['anger']},"
    message_2 = f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']},"
    message_3 = f"and 'sadness': {result['sadness']}. The dominant emotion is"
    message_4 = f"{result['dominant_emotion']}."

    # Concatenate messages
    full_message = message_1 + " " + message_2 + " " + message_3 + " " +message_4

    return full_message



@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
