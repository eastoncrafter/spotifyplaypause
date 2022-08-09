from types import NoneType
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
 

scope = "user-modify-playback-state, user-read-playback-state"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="eb200d7fe8c04bafa1554dfb55846e65", client_secret="d693db0ded844619b6f26d9cbc0f6bc0", redirect_uri="http://localhost:8888/callback"))
#############################################################################################
playornot = sp.current_user_playing_track()
if type(playornot) == NoneType:
    playornot = {"is_playing": False}


value = playornot.get('is_playing')

devices = sp.devices()

#for x in devices['devices']:
#    if x['is_active']:
#        device_id = x['id']
#        break
device_id = devices
print(device_id)
print(type(device_id))

#print(type(playornot))
#value = playornot['is_playing']
if value == True:
    sp.pause_playback()
    print("Paused")
    
else:
    sp.start_playback(device_id=device_id)
print(value)
#sp.start_playback()

print("does the script contine")



#############
#testvariable = {}
#print(testvariable.get('is_playing'))
#############
