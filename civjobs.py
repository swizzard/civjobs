from os import environ
from random import choice

import botmaster
import pycorpora


@botmaster.gen_tweet(botmaster.auth.env_auth('token', 'secret', 'consumer_key',
                                             'consumer_secret'),
                    ignore=[187], restart=True)
def get_listing():
    framings = ["We're looking for a {} {} to join our team!",
                "Are you a {} {}? Apply now!",
                "{} {} wanted!",
                "Cool startup seeks 10X {} {}",
                "{} {}? Call us",
                "Seeking a {} {} for our awesome team!"]
    with open('units.txt') as infile:
        units = [unit.strip() for unit in infile]
    jobs = pycorpora.technology.computer_sciences['computer_sciences']
    while True:
        yield choice(framings).format(choice(jobs), choice(units))


if __name__ == '__main__':
    get_listing()

