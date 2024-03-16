# Docker build for Asterisk including chan_quectel

## What is it?

This is a Docker container including (IchthysMaranatha/asterisk-chan-quectel)[https://github.com/IchthysMaranatha/asterisk-chan-quectel].
I use it with the Simcom SIM7600E modem hat for a Raspberry Pi 4 for forwarding SMS to email and calling using IAX to my main PBX
running FreePBX.

Should also work with the Quectel EC25 and similar.

## How do I configure Asterisk?

There are sample config files in /opt/asterisk-samples inside the container. Copy them to outside of the container and mount that to /etc/asterisk.

To handle incoming SMS, add to your incoming context to extensions.conf:

```
exten => sms,1,Verbose(Incoming SMS from ${CALLERID(num)} ${BASE64_DECODE(${SMS_BASE64})})
exten => sms,n,System(echo '${BASE64_DECODE(${SMS_BASE64})}' | python3 /opt/scripts/sms2email.py -c '${QUECTELNAME}' -n '${CALLERID(num)}' -d '${SMS_EMAIL_TARGET}')
exten => sms,n,Hangup()
```

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
  * Feel free to modify for running with more than one modem
  * Probably doesn't handle international SMS very well

## Contributing

Feel free to fork and modify, don't forget to share ;)