from settings import get_time

class Timer:
    def __init__(self, duration, callback=None, autostar=False, repeat=False):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.callback = callback
        self.repeat = repeat

        if autostar:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = get_time()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def update(self):
        if self.active:
            if get_time() - self.start_time >= self.duration:
                if self.callback:
                    self.callback()
                self.deactivate()