import RPi.GPIO as GPIO


class Robot:
    pins = (7, 11, 13, 15)
    forward = (False, True, False, True)
    back = tuple(reversed(forward))
    right = (True, False, False, True)
    left = (False, True, True, False)
    rest = (False, False, False, False)

    def go_forward(self, val):
        correct_list = self.forward if val == 1 else self.back
        for i in range(len(self.pins)):
            GPIO.output(self.pins[i], correct_list[i])

    def go_right(self, val):
        correct_list = self.right if val == 1 else self.left
        for i in range(len(self.pins)):
            GPIO.output(self.pins[i], correct_list[i])

    def stay_at_rest(self):
        for i in range(len(self.pins)):
            GPIO.output(self.pins[i], self.stay[i])