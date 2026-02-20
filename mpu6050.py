from machine import I2C

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00') # Wake up

    def get_values(self):
        raw = self.i2c.readfrom_mem(self.addr, 0x3B, 14)
        v = {
            "AcX": self._to_int(raw[0:2]),
            "AcY": self._to_int(raw[2:4]),
            "AcZ": self._to_int(raw[4:6]),
            "GyX": self._to_int(raw[8:10]),
            "GyY": self._to_int(raw[10:12]),
            "GyZ": self._to_int(raw[12:14]),
        }
        return v

    def _to_int(self, data):
        res = data[0] << 8 | data[1]
        return res if res < 32768 else res - 65536
    