Raspberry Pi with a a Grove Hat, Grove Relay 5v pump, and a random 3 pin Capacitive Soil Moisture Sensor.

A usb Splitter is used to power the Pi and relay from the same hub.

The relay is pluged into D5 block on the hat, the sensor is jammed on the last three pins of block A4.
This means the signal is on Pin A5.


The Grove API is used for the relay logic in code.
Since the sensor isn't using the API spec'd Analog pin (A4) for the block its in, Pin A5 is read directly instead of using the API.
