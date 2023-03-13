from playsound import playsound
import time 


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 
        seconds_left = time_left % 60
        
        
        print(f"{CLEAR_AND_RETURN }Alarm akan berbunyi: {minutes_left:02d}:{seconds_left:02d}")

    playsound("C:\\Users\\razki\Python\\alarm\\alarm.mp3")
    
minutes = int(input("Berapa menit yang kamu tunggu : "))
seconds = int(input("Berapa detik yang kamu tunggu : "))
total_seconds = minutes * 60 + seconds     

alarm(total_seconds)
