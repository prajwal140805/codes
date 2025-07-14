import time
import winsound
from plyer import notification

def remind_to_drink(interval_minutes):
    while True:
        notification.notify(
            title="💧 Time to Hydrate!",
            message="Take a moment and drink a glass of water 🥤",
            app_name="Water Reminder",
            timeout=10 )
        winsound.Beep(400, 500)  # Beep at 400 Hz for 500 milliseconds
        time.sleep(interval_minutes * 3600)  

 
remind_to_drink(0.001)
 
  # 1000 Hz for 0.5 second
