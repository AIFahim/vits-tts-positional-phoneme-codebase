import torchaudio
from TTS.utils.synthesizer import Synthesizer
import requests
import json
import base64
import wave
import numpy as np
from fastapi import FastAPI, File, UploadFile, Request
import json
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

url = "https://dev.revesoft.com:6790/phonemizer"

app = FastAPI()

class Body(BaseModel):
    grapheme:str


@app.get('/')
async def home():
    return "Fast server is working!"


@app.post("/infer_tts/")
async def infer(body:Body):
    grapheme = body.dict()['grapheme']
    synth=Synthesizer(tts_checkpoint="/home/asif/tts_all/coqui_tts/my_exp/coqui_vits_48k_pos_pho_weight/best_model_261562.pth",tts_config_path="/home/asif/tts_all/coqui_tts/my_exp/coqui_vits_48k_pos_pho_weight/config.json")
    
    payload = json.dumps({
    "text": grapheme
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    phonme = response.json()['output']
    phonme = " ".join(phonme)
    wav=synth.tts(phonme)
    synth.save_wav(wav,"/home/asif/tts_all/coqui_tts/my_exp/coqui_vits_48k_pos_pho_weight/output_audio/vits.wav")

    with open("/home/asif/tts_all/coqui_tts/my_exp/coqui_vits_48k_pos_pho_weight/output_audio/vits.wav", "rb") as f:
        audio_data = f.read()

    base64_audio = base64.b64encode(audio_data).decode("utf-8") 
    return base64_audio 

    
if __name__ == "__main__": 
    uvicorn.run("infer_n_host_fastapi:app", host='0.0.0.0', port = 7777, reload = True)
