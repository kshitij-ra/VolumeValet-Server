from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pyautogui import press


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def volget():
    return volume.GetMasterVolumeLevelScalar()
def volset(vol):
    volume.SetMasterVolumeLevelScalar(vol/100,None)
def volmute(a):
    volume.SetMute(a,None)
def getmute():
    return volume.GetMute()
def playpause():
    press('playpause')
    return 'Success'
def nexttrack():
    press('nexttrack')
    return 'Success'
def prevtrack():
    press('prevtrack')
    return 'Success'