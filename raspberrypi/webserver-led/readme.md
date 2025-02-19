# webserver led on/off python

```bash
#build
docker buildx create --use --name insecure-builder --buildkitd-flags '--allow-insecure-entitlement security.insecure'

DOCKER_BUILDKIT=1 docker buildx build --allow security.insecure --load -t webserver-led -f Dockerfile .

#run
docker run -d -p 8001:80 --privileged webserver-led


#Led_status.py
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# To read the state
state = GPIO.input(17)
print("state: "+str(state))
if state:
   print('on')
else:
   print('off')


```