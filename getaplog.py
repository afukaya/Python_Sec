#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
NAME  : get_aplog.py
AUTHOR: Alexandre Fukaya
DATE  : 13/03/2020

DESCRIPTION:
    Connects thru HTTP to a TP-Link TL-WR841HP and retrieves it system log for processing.
    
DEPENDENCIES:

"""

import requests

def getlogfile():
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.raise_for_status()
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()

def main():
    getlogfile()

if __name__ == "__main__":
    main()