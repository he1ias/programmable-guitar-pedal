# programmable-guitar-pedal

A programmable acoustic guitar pedal that doubles as a wireless instrument recording device.

### What does it do?

This project allows you to test infinite different effects on your acoustic or electric without having to pay huge prices for expensive guitar pedals. Simply plug your guitar in as you would with any other guitar pedal, and access different effects and plugins via the built-in Raspberry Pi Pico's web interface.

### What's in this repo?

All the firmare & KiCad project files used to build this project!

You can access the KiCad project files [here](https://kicanvas.org/?repo=https://github.com/he1ias/programmable-guitar-pedal/blob/main/KiCad%20Files/).

### How was it built?

I started by making a prototype amplifier using breadboards & transistors:

![A breadboard prototype](https://raw.githubusercontent.com/he1ias/programmable-guitar-pedal/refs/heads/main/Prototype.jpeg)

I then developed the schematic using KiCad:

![schematic](https://raw.githubusercontent.com/he1ias/programmable-guitar-pedal/refs/heads/main/Schematic.jpeg)

...and the PCB!

![PCB](https://raw.githubusercontent.com/he1ias/programmable-guitar-pedal/refs/heads/main/PCB.jpeg)

![3D](https://raw.githubusercontent.com/he1ias/programmable-guitar-pedal/refs/heads/main/3D.jpeg)

### How do I build it?

You can find the bill of materials in `bom.md` and `bom.csv`, I've also attached it below. KiCad project & gerber output files can also be found in this repository, as well as `.step` and `.stl` files ready to print the 3D guitar pedal case model.

| Item | Qty | Supplier | Cost/item | Total Cost | Link |
|------|----:|----------|----------:|-----------:|------|
| Potentiometers (w. Knobs) | 2 | LCSC | $0.57 | $1.14 | [Link](https://www.lcsc.com/product-detail/C470717.html) |
| Precision potentiometers | 5 | LCSC | $0.16 | $0.80 | [Link](https://www.lcsc.com/product-detail/C118945.html) |
| Op-amp | 5 | LCSC | $0.30 | $1.50 | [Link](https://www.lcsc.com/product-detail/C7377.html) |
| 1/4" guitar jacks | 2 | LCSC | $0.50 | $1.00 | [Link](https://www.lcsc.com/product-detail/C41409495.html) |
| JLCPCB | 1 | JLC | $10.00 | $10.00 | [Link](https://jlcpcb.com/) |
| Raspberry Pi Pico 2WH | 1 | Core electronics | $10.01 | $10.01 | [Link](https://core-electronics.com.au/raspberry-pi-pico-2-wh-with-headers.html) |
| DAC | 1 | Core electronics | $5.64 | $5.64 | [Link](https://core-electronics.com.au/adafruit-pcm5100-i2s-dac-line-level-output-100db-snr.html) |
| 20pin Female headers | 2 | Core electronics | $0.25 | $0.50 | [Link](https://core-electronics.com.au/0-100-2-54-mm-female-header-1x20-pin-straight.html) |
| 6.5mm male to 3mm female audio cable | 1 | Jaycar | $2.88 | $2.88 | [Link](https://www.jaycar.com.au/6-5mm-stereo-plug-to-3-5mm-stereo-socket-adaptor/p/PA3590) |
| Estimated total shipping | 1 | | | $14.00 | |

Total cost: ~$46.47 (USD).