from machine import Pin
from utime import sleep, ticks_ms, ticks_diff
import network
import _thread

class WLAN:
    def __init__(self, ssid: str, passwd: str, active: bool = True):
        self.ssid = ssid
        self.passwd = passwd
        self.active = active
        self.interface = network.WLAN(network.STA_IF)

    def connect(self, timeout: int = 10) -> bool:
        self.interface.active(self.active)
        if not self.interface.isconnected():
            print(f"Connecting to {self.ssid}...")
            self.interface.connect(self.ssid, self.passwd)
            start = ticks_ms()
            while not self.interface.isconnected():
                if ticks_diff(ticks_ms(), start) > timeout * 1000:
                    print("Connection timed out.")
                    return False
                sleep(0.5)
        print(f"Connected! IP: {self.get_ip()}")
        return True

    def disconnect(self):
        self.interface.disconnect()
        self.interface.active(False)

    def is_connected(self) -> bool:
        return self.interface.isconnected()

    def get_ip(self) -> str:
        return self.interface.ifconfig()[0]

class LED:
    def __init__(self, pin="LED"):
        self.led = Pin(pin, Pin.OUT)

    def on(self):
        self.led.on()
        return True

    def off(self):
        self.led.off()
        return True

    def toggle(self):
        self.led.toggle()
        return True

running = False
led_lock = _thread.allocate_lock()

def led_task():
    global running
    i = 0
    print("LED starts flashing...")
    while running:
        i += 1
        print(f"# {i}:")
        if onboardLED.on(): print("OnboardLED On")
        sleep(0.5)
        if not running:
            break
        if onboardLED.off(): print("OnboardLED Off")
        sleep(0.5)
    onboardLED.off()
    print("LED Finished.")
    led_lock.release()  # 通知主程式 thread 已結束

ssid = "SSID_NAME"
passwd = "SSID_PASSWORD"

onboardLED = LED()
led_lock.acquire()   # 主程式先持有鎖
running = True
_thread.start_new_thread(led_task, ())

wlan = WLAN(ssid, passwd)
wlan.connect()       # 連線成功或 timeout 後才會返回
running = False      # 通知 LED thread 停止
led_lock.acquire()   # 阻塞直到 led_task 呼叫 release()，確保 thread 已退出
onboardLED.on()
wlan.disconnect()