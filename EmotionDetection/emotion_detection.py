import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP Emotion Prediction API and returns formatted emotion scores.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: Contains anger, disgust, fear, joy, sadness scores and dominant emotion
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        response_data = json.loads(response.text)
        emotions = response_data['emotionPredictions'][0]['emotion']
        
        # Extract individual emotions
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
        
        # Find dominant emotion
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return formatted output
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        return None