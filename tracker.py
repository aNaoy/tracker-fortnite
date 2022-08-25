#!/usr/bin/env python3

import requests
import time
import logging
import yaml

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

api_key = config['api_key']
players = config['players']
loglevel = config['loglevel']

logging.basicConfig(level=loglevel)
header = {"TRN-Api-Key": api_key}
players = players

def main():
    logging.info("Tracking starting...")
    for player in players:
        try:
            logging.debug("Trying to get stats for gamer %s" % player)
            r = requests.get(
                "https://api.fortnitetracker.com/v1/profile/all/" + player,
                headers=header)
            r.raise_for_status()
            logging.info("Stats for gamer %s retrieved" % player)
        except requests.exceptions.RequestException as e:
            logging.error("HTTP exception trying player %s" % player)
            raise SystemExit(e)
        time.sleep(2)

    logging.info("Tracking finished!")


if __name__ == "__main__":
    main()
