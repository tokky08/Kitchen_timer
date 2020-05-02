import rumps
 
class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("設定")
    def prefs(self, _):
        rumps.alert("メッセージを表示します。")
 
    @rumps.clicked("ON-OFFスイッチ")
    def onoff(self, sender):
        sender.state = not sender.state
 
    @rumps.clicked("メッセージ通知")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")
 
if __name__ == "__main__":
    AwesomeStatusBarApp("キッチンタイマー").run()