import requests
import json

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Test formatting for error handling
    if not text_to_analyze:
        return response.status_code == 400, {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
        }

    try:
        response = requests.post(url, headers=headers, json=input_json, timeout=10)
        data = json.loads(response.text)
        emotions = data["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
        }

    except Exception as e:
        print("Request failed:", e)
        return None
