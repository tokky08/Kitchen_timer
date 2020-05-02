import rumps
import datetime
import time


TIMER_MODE = 'timer'

minute = 2
second = 59
start = time.time()

@rumps.clicked(u'残り勤務時間を表示')
def switchTimer(sender):
    global display_state
    display_state = TIMER_MODE

@rumps.timer(1)
def dispTimer(sender):
    
    timer_minute = str(minute-1)
    timer_second = str(second - int(time.time() - start) % 60)

    remaining_minute = int(time.time() - start) // 60
        
    if int(timer_second) < 10:
        timer_second = "0" + timer_second

    timer_minute = str(int(timer_minute) - remaining_minute)
    app.title = "残り時間：" + timer_minute + ":" + timer_second
    
    


if __name__ == "__main__":
    display_state= TIMER_MODE
    app = rumps.App("Kitchen_TIMER", title='Timer')
    app.run()