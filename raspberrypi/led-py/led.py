from flask import Flask, render_template, request
import gpiod

# GPIO setup
CHIP = "gpiochip0"  # This is usually the default GPIO chip on Raspberry Pi
usable_pins = [2, 3, 4, 14, 15, 17, 18, 27, 22, 23, 24, 10, 9, 25, 11, 8, 7, 5, 6, 12, 13, 19, 16, 26, 20, 21]
pins = {pin: {'name': f'GPIO {pin}', 'state': 'LOW'} for pin in usable_pins}

# Open GPIO chip
chip = gpiod.Chip(CHIP)

# Setup pins
lines = {}
for pin in usable_pins:
    line = chip.get_line(pin)
    line.request(consumer="flask-app", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
    lines[pin] = line

# Flask app setup
app = Flask(__name__)

@app.route("/")
def index():
    # Read pin states
    for pin, line in lines.items():
        state = line.get_value()
        pins[pin]['state'] = "HIGH" if state else "LOW"
    return render_template("index.html", pins=pins)

@app.route("/<int:pin>/<action>")
def control_pin(pin, action):
    if pin in lines:
        if action == "on":
            lines[pin].set_value(1)
        elif action == "off":
            lines[pin].set_value(0)
    return index()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
