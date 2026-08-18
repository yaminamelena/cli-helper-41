import time
import threading

class AutoClicker:
    def __init__(self, delay=1):
        self.delay = delay
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self._click).start()

    def stop(self):
        self.running = False

    def _click(self):
        while self.running:
            self._perform_click()
            time.sleep(self.delay)

    def _perform_click(self):
        # Simulate a mouse click
        print('Mouse clicked!')

if __name__ == '__main__':
    clicker = AutoClicker(delay=0.5)
    clicker.start()
    time.sleep(5)
    clicker.stop()