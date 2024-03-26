#!/bin/env python3
import configparser
import os

CONFIG_FILE="server.cfg"

config_parser = configparser.ConfigParser()
config = config_parser.read(CONFIG_FILE)
if config != [CONFIG_FILE]:
    if os.path.exists(CONFIG_FILE):
        if os.path.isfile(CONFIG_FILE):
            raise Exception("Unexpected error when parsing config")
        else:
            raise IsADirectoryError("Config is not a file")
    else:
        print("Config does not exist.")
        print("Would you like to use the template? (y/N)")
        if input().strip()[0:1].lower()=="y":
            import template
            print("Writing template to config")
            open(CONFIG_FILE,"w").write(template.template)
            print("Written, run again to use.")
            exit(0)

