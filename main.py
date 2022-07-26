import requests
# import io
import winsound
# from  pydub import AudioSegment
# from pydub.playback import play
import urllib

speaker=2
tmp = "クエリの初期値を得ます,ここで得られたクエリはそのまま音声合成に利用できます。"
txt = urllib.parse.quote(tmp, safe='/', encoding=None, errors=None)


vve_audio_query =  "http://127.0.0.1:50021/audio_query"
vve_synthesis =  "http://127.0.0.1:50021/synthesis"
vve =  "http://127.0.0.1:50021"


txt_q = requests.post(f"{vve_audio_query}?speaker={speaker}&text={txt}").content

audio = requests.post(f"{vve_synthesis}?speaker={speaker}",data=txt_q,headers={"Content-Type":"application/json"}).content
# play(AudioSegment.from_file(io.BytesIO(audio), format="wav"))
# print(audio[:100])
winsound.PlaySound(audio, winsound.SND_MEMORY)