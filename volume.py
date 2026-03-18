import platform
import time
import comtypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

if platform.system() != 'Windows':
    raise NotImplementedError("System not compatible; only works on Windows.")

def get_endpoint_volume():
    mic = AudioUtilities.GetMicrophone()
    if mic is None:
        raise RuntimeError("No microphone found.")
    interface = mic.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
    return interface.QueryInterface(IAudioEndpointVolume)

def main():
    endpoint_vol = get_endpoint_volume()
    target = 1.0
    interval = 0.5
    restores = 0

    print("Microphone Volume Guard")
    print("─" * 30)
    print(f"Target: 100%  |  Polling: every {interval}s")
    print("─" * 30)

    while True:
        try:
            current = endpoint_vol.GetMasterVolumeLevelScalar()
            if current < target:
                endpoint_vol.SetMasterVolumeLevelScalar(target, None)
                restores += 1
                print(f"[{time.strftime('%H:%M:%S')}] Drop: {current:.0%} → 100%  (#{restores})")
            time.sleep(interval)
        except KeyboardInterrupt:
            print("─" * 30)
            print(f"Stopped. {restores} restore(s) made.")
            break
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] Error: {e} — retrying...")
            time.sleep(2)
            try:
                endpoint_vol = get_endpoint_volume()
                print(f"[{time.strftime('%H:%M:%S')}] Mic re-acquired.")
            except Exception as e2:
                print(f"[{time.strftime('%H:%M:%S')}] Failed: {e2}")

if __name__ == "__main__":
    main()
