# programmable-guitar-pedal

A programmable acoustic guitar pedal that doubles as a wireless instrument recording device.

### What does it do?

This project allows you to test infinite different effects on your acoustic or electric without having to pay huge prices for expensive guitar pedals. Simply plug your guitar in as you would with any other guitar pedal, and access different effects and plugins via the built-in Raspberry Pi Pico's web interface.

### What's in this repo?

All the firmare & KiCad project files used to build this project!

You can access the KiCad project files [here](https://kicanvas.org/?repo=https://github.com/he1ias/programmable-guitar-pedal/blob/main/KiCad%20files/).

### How do I built it?

You can find the bill of materials in `bom.md` and `bom.csv`, I've also attached it below. KiCad project & gerber output files can also be found in this repository, as well as `.step` and `.stl` files ready to print the 3D guitar pedal case model.

#### JLC (USD)

| Item | Supplier | Qty | Unit | Total | Link |
|---|---|---:|---:|---:|---|
| PCB fabrication | JLCPCB | 1 | \~\$10.00 | \~\$10.00 | n/a |
| 3D printing | JLC3DP | 1 | \~\$5.00 | \~\$5.00 | n/a |
| Guitar inputs (C41409495) | LCSC | 2 | \$0.50 | \$1.00 | [link](https://www.lcsc.com/product-detail/C41409495.html) |
| Potentiometers (C470717) | LCSC | 3 | \$0.57 | \$1.71 | [link](https://www.lcsc.com/product-detail/C470717.html) |
| Op-amp (C5213) | LCSC | 5 | \$0.22 | \$1.11 | [link](https://www.lcsc.com/product-detail/C5213.html) |
| Shipping | JLC | n/a | n/a | \~\$5.00 | n/a |
| **Subtotal** | | | | **\~\$23.82 USD** | |

#### Core Electronics (AUD)

| Item | Qty | Unit | Total | Link |
|---|---:|---:|---:|---|
| Raspberry Pi Pico 2 WH | 1 | \$14.30 | \$14.30 | [link](https://core-electronics.com.au/raspberry-pi-pico-2-wh-with-headers.html) |
| Polymer Li-ion battery 400mAh | 1 | \$5.55 | \$5.55 | [link](https://core-electronics.com.au/polymer-lithium-ion-battery-400mah-38456.html) |
| Makerverse USB-C LiPo charger | 1 | \$6.85 | \$6.85 | [link](https://core-electronics.com.au/makerverse-usb-c-lipo-charger.html) |
| Adafruit PCM5100 I2S DAC | 1 | \$8.05 | \$8.05 | [link](https://core-electronics.com.au/adafruit-pcm5100-i2s-dac-line-level-output-100db-snr.html) |
| 2.54mm female header 1x20 | 2 | \$0.35 | \$0.70 | [link](https://core-electronics.com.au/0-100-2-54-mm-female-header-1x20-pin-straight.html) |
| Shipping | n/a | n/a | \~\$10.00 | n/a |
| **Subtotal** | | | **\~\$45.45 AUD** | |

#### Jaycar (AUD)

| Item | Qty | Unit | Total | Link |
|---|---:|---:|---:|---|
| 6.5mm mono plug to 6.5mm mono R/A plug audio cable (3m) | 1 | \$12.25 | \$12.25 | [link](https://www.jaycar.com.au/6-5mm-mono-plug-to-6-5mm-mono-r-a-plug-audio-cable-3m/p/WA7024) |
| **Subtotal** | | | **\$12.25 AUD** | |

#### Summary

| Source | Currency | Subtotal |
|---|---|---:|
| JLC (incl. shipping) | USD | \~\$23.82 |
| Core Electronics (incl. shipping) | AUD | \~\$45.45 |
| Jaycar | AUD | \$12.25 |
| **Total** | | **\~\$64 USD** |