from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on....")

    def turn_off(self):
        print("LightBulb: turned off....")


class Socket(Switchable):
    def turn_on(self):
        print("Socket: turned on....")

    def turn_off(self):
        print("Socket: turned off....")


class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
s = Socket()
switch = ElectricPowerSwitch(s)
switch.press()
switch.press()
