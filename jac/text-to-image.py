import base64
import requests
from jaseci.jsorc.live_actions import jaseci_action
import traceback
from fastapi import HTTPException

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}



@jaseci_action(act_group=["text_to_image"], allow_remote=True)
def generate(text:str) -> str:
	'''generat an image bytes string from the text using the stable diffusion v1.5 model'''
	try:
		payload = {
            "inputs": text
        }
		response = requests.post(API_URL, headers=headers, json=payload)
		image_bytes = response.content
		image_bytes =base64.b64encode(image_bytes).decode("utf-8")
		return image_bytes
	except Exception as e:
		traceback.print_exc()
		raise HTTPException(status_code=500, detail=str(e))
        