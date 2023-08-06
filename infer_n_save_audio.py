import torchaudio
from TTS.utils.synthesizer import Synthesizer
import requests
import json
import base64
import wave
import numpy as np
url = "https://dev.revesoft.com:6790/phonemizer"

def infer(grapheme:str):

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
    synth.save_wav(wav,"/infered_audio/vits.wav")
 
if __name__ == "__main__":
    infer("গিনেস বুকে ১২ বার নাম লিখিয়েছেন মাগুরার মাহমুদুল")

    
