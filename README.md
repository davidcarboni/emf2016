## This repo is all about controlling the lights in the number '1' in the sign on the hill above EMF Camp.

 * Current address of the Web API: http://carboni.io
 * Follow the links from there to see how you can get the lights to react and even post custom patterns.

We're working on a an app for the badge so you can play with the sign directly. The code is here: See also: https://github.com/davidcarboni/emf2016-sign-badge


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


