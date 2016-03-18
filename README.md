A basic discord bot for Dota 2 pickup games.

Currently this just waits for 10 players to sign in, then shuffles them up
and splits them into two teams. There's a lot more to do before it's good,
just wanted to get what I'd done online.

To use:

* Get your bot a username/password by signing up to discord for them, and
  connecting in to any servers you want them to be on.
* Install python 3.5.
* pip install -r requirements.txt
* Put your bot's username and password into config.json (see config.json.example)
* Run main.py. It will connect to all the channels in all the servers you
  put them in when you set up the username.
