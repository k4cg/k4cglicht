# k4cglicht

CLI Interface for our K4CG Philips Hue Light

### Install

```
git clone https://github.com/k4cg/k4cglicht
cd k4cglicht
pip install -r requirements.txt
chmod +x k4cglicht
```

### Usage

```
Usage:
  k4cglicht farbe <farbname>
  k4cglicht farben
  k4cglicht alarm
  k4cglicht blaulicht
  k4cglicht alieninvasion
  k4cglicht dimmen <prozent>
  k4cglicht normal
  k4cglicht zufall
  k4cglicht harmonisch ausrasten <dauer>
  k4cglicht annoy <bulb> <times>

Options:
  -h --help     HILFE!
  --version     FICKENDE VERSION!
```

### Misc

* Initales pairen Link button druecken und innerhalb 30 Sekunden ausfuehren
* Im moment nur aus der K4CG Triggerbar.
* Kein IPv6 auf der Bridge
* Helligkeit von 0 bis 254
* Farben gehen von 0 bis 1. (0.11,0.12..0.98,0.99)
* Einzelne Lichter sind in der list "lights"
* Einfach drueber iterieren
