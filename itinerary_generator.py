import requests

def generate_itinerary(prompt):
    url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 512,
            "do_sample": False
        }
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]
    else:
        return "Error generating itinerary. Please try again."
