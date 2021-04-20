class Time:
    """Represents the time of day."""

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds = seconds + self.time_to_int()
        self.int_to_time(seconds)

    def int_to_time(self, seconds):
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)

t = Time(12,20,00)
print(t)
totalseconds = t.increment(125)
print(t)