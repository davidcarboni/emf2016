## This repo is all about controlling the lights in the number '1' in the sign on the hill above EMF Camp.

IP of rPI on the EMF network: 94.45.254.19
DNS name that resolves to this IP address: carboni.io
Current address of the Web API: http://carboni.io:5000

If you want to suggest changes, send a pull request, or tweet to @davidcarboni.

## Installation

```
$ git clone URL /home/pi/git/emf2016
$ sudo cp /home/pi/git/emf2016/lights.service /etc/systemd/system
$ sudo systemctl enable lights
$ sudo systemctl start lights
```

## Check status and logs

```bash
$ sudo systemctl status lights
```

## Restart

```bash
$ sudo systemctl restart lights
```


