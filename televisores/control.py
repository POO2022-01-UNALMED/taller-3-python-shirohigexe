class Control:
    def enlazar(self, tv):
        self._tv = tv
        self._tv._control = self
    
    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, canal):
        if self._tv._estado and canal >= 1 and canal <= 120:
            self._tv._canal = canal

    def getTv(self):
        return self._tv

    def setTv(self, tv):
        self._tv = tv