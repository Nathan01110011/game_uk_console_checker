# GAME UK New Gen Console Checker
## Reasoning
Currently it is difficult to acquire any of the new generation consoles released in 2020. This python script checks the GAME UK website (https://www.game.co.uk/) for when the Out of Stock button on each console page turns into the buy now button. When stock appears to be available, a ring will occur to notify user. 

## How To Run

To install the necessary requirements, run `pip install -r requirements.txt` and then run one of the options below.

| Command      | Description |
| ------------ | ----------- |
| python run_checker.py ps   | Will search for Playstation 5 and Playstation 5 Digital Editions |
| python run_checker.py xbox | Will search for Xbox Series X and Xbox Series S |
| python run_checker.py both | Will search for all new generation consoles |