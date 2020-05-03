import rumps
import datetime
import time


TIMER_MODE = 'timer'
second = 59


@rumps.clicked(u'1分')
def selectTimer(sender):
    global minute
    minute = 1

    global start
    start = time.time()

@rumps.clicked(u'3分')
def selectTimer(sender):
    global minute
    minute = 3

    global start
    start = time.time()

@rumps.clicked(u'5分')
def selectTimer(sender):
    global minute
    minute = 5

    global start
    start = time.time()

@rumps.clicked(u'10分')
def selectTimer(sender):
    global minute
    minute = 10

    global start
    start = time.time()

@rumps.clicked(u'15分')
def selectTimer(sender):
    global minute
    minute = 15

    global start
    start = time.time()

@rumps.clicked(u'20分')
def selectTimer(sender):
    global minute
    minute = 20

    global start
    start = time.time()

@rumps.clicked(u'25分')
def selectTimer(sender):
    global minute
    minute = 25

    global start
    start = time.time()

@rumps.clicked(u'30分')
def selectTimer(sender):
    global minute
    minute = 30

    global start
    start = time.time()




@rumps.timer(1)
def dispTimer(sender):
    
    timer_minute = str(minute-1)
    timer_second = str(second - int(time.time() - start) % 60)

    remaining_minute = int(time.time() - start) // 60
    timer_minute = str(int(timer_minute) - remaining_minute)

    if int(timer_minute) < 0:
        app.title = "TIME UP"
        if int(timer_minute) == -1 and int(timer_second) == 58:
            rumps.notification(message="作業をやめてください！！！", title="TIME UP！", subtitle="")


    else:
        if int(timer_second) < 10:
            timer_second = "0" + timer_second

        app.title = "残り時間：" + timer_minute + ":" + timer_second
        
    


if __name__ == "__main__":
    display_state= TIMER_MODE
    app = rumps.App("Kitchen_TIMER", title='Timer')
    app.run()