import requests
import json
def emotion_detector(text_to_analyze):
    #url link
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #input object
    myobj = { "raw_document": { "text": text_to_analyze } }
    #model ID for API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #response from post request
    response = requests.post(url, json=myobj, headers=header)

    formatted = json.loads(response.text)

    
    if response.status_code == 200:
        emotion_scores = formatted["emotionPredictions"][0]["emotion"]
        emotion_scores["dominant_emotion"] = max(emotion_scores, key=emotion_scores.get)
        return emotion_scores

    # If the response status code is 400, set label and score to None
    elif response.status_code == 400:
        emotion_scores = {}
        emotion_scores["anger"] = None
        emotion_scores["disgust"] = None
        emotion_scores["fear"] = None
        emotion_scores["joy"] = None
        emotion_scores["sadness"] = None
        emotion_scores["dominant_emotion"] = None
        return emotion_scores