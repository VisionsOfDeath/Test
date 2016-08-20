[![Build Status](https://travis-ci.org/veryhappythings/discord-gather.svg?branch=master)](https://travis-ci.org/veryhappythings/discord-gather) [![Coverage Status](https://coveralls.io/repos/github/veryhappythings/discord-gather/badge.svg?branch=master)](https://coveralls.io/github/veryhappythings/discord-gather?branch=master)


## A basic discord bot for Dota 2 pickup games.

Currently this just waits for 10 players to sign in, then shuffles them up
and splits them into two teams. There's a lot more to do before it's good,
just wanted to get what I'd done online.

## To use:

* Get your bot a discord token by adding a new app at https://discordapp.com/developers/applications/me and creating your app a bot user
* Add your bot to your guild by constructing a link from this https://discordapp.com/developers/docs/topics/oauth2#adding-bots-to-guilds - The permissions you will need are 3072, so your link will take the form https://discordapp.com/oauth2/authorize?client_id=<your bot id>&scope=bot&permissions=3072
* Install python 3.5
* `pip install .` - if you intend to edit the code, use `pip install -e .`
* Put your bot's token into config.json (see config.json.example)
* Run `discord-gather`

## Or if you're a Docker kind of person

https://hub.docker.com/r/veryhappythings/discord-gather/ - Stick DG_TOKEN on your environment and off it goes. Very much a WIP, contributions welcome!

## Contributors

A huge thanks to:

* [@zoidbergwill](https://github.com/zoidbergwill)
* [@joshramsbottom](https://github.com/joshramsbottom)
