#!/usr/bin/env python3
import sys, configparser
from mfcauto import Client
import asyncio


Config = configparser.ConfigParser()
Config.read(sys.path[0] + "/config.conf")
wishlist = Config.get('paths', 'wishlist')

f = open(wishlist, 'r')
wanted = list(set(f.readlines()))


async def main(loop):
    if len(sys.argv) != 2:
        print('Must include a models name. ie: add.py AspenRae'.format(sys.argv[0]))
        sys.exit(1)

    modelName = sys.argv[1]

    print("Querying MFC for {}".format(modelName))
    client = Client(loop)
    await client.connect(False)
    msg = await client.query_user(modelName)
    client.disconnect()
    print()

    if msg == None:
        print("User not found. Please check your spelling and try again")
    else:
        if str(msg['uid'])+'\n' in wanted:
            print('{} is already in the wanted list. Models UID is {}'.format(modelName, str(msg['uid'])))
        else:
            f = open(wishlist, 'a')
            f.write(str(msg['uid'])+'\n')
            print("{} with UID {} has been added to the list".format(modelName, msg['uid']))
        print()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()

