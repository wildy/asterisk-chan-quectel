# Docker build for Asterisk including chan_quectel

## What is it?

This is a Docker container including (IchthysMaranatha/asterisk-chan-quectel)[https://github.com/IchthysMaranatha/asterisk-chan-quectel].
I use it with the Simcom SIM7600E modem hat for a Raspberry Pi 4 for forwarding SMS to email and calling using IAX to my main PBX
running FreePBX.

Should also work with the Quectel EC25 and similar.

## How do I configure Asterisk?

There are sample config files in /opt/asterisk-samples inside the container.

## How do I build it?

Use `docker build -t asterisk-chan-quectel .`

## How do I run it?

```
docker run -d \
  --name asterisk \
  --volume ~/docker/asterisk/scripts/sms2email.conf:/opt/scripts/sms2email.conf \
  --volume ~/docker/asterisk/asterisk:/etc/asterisk \
  --network host \
  --device /dev/ttyUSB2:/dev/quectel0-data \
  --device /dev/ttyUSB4:/dev/quectel0-audio \
  --restart always \
  wildy.asterisk-chan-quectel:latest
```
## Bugs

Lots.
  * Port is hardcoded in modeminit.py
  * modeminit.py doesn't check for any errors
  * Asterisk build could (and should) be optimized
  * Feel free to modify for running with more than one modem.

## Contributing

Feel free to fork and modify, don't forget to share ;)