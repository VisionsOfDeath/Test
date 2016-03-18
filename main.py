import logging
import json
from gather import bot


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s,%(msecs)03d %(levelname)-5.5s [%(name)s] %(message)s",
    )

    with open('config.json') as f:
        config = json.load(f)

    bot.run(config['username'], config['password'])
