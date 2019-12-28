from grove.grove_relay import GroveRelay
from grove.adc import ADC

GroveRelay(5).off()

def moist():
	print("testing moisture")
	print(ADC().read_voltage(5))
	return ADC().read_voltage(5)	

def addWater():
	print("adding water")
	relay = GroveRelay(5)
	relay.on()
	time.sleep(2)
	relay.off()

while True:
	soilMoist = moist()
	if soilMoist > 2500:
		addWater()
		
	time.sleep(60)
