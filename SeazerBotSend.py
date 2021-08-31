#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  seazerbotsend.py
#  
#  Copyright 2020 jacks <jacks@DESKTOP-MINUT5T>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
from SeazerBot import *
import time

##### Runner program for tweetSong() #####
#in hours
tweetInterval = 3
tries = 0

songs = initSongs()

def sendASong(tries):
    while True:
        if tries == 5:
            print('this shit didn\'t work, apparently')
            with open('seazerlog.txt',\
                 'a', encoding='utf-8') as seazerLog:
                     seazerLog.write('FAILED, attempt {}, resetting queue.\n'.format(tries))
            resetFile = open(r'{}/userQueue.txt'.format(os.path.dirname(__file__)), 'w', encoding = 'utf8')
            resetFile.close()
            sendASong(0)
            break
        else:
            try:
                data = tweetSong(songs)
                print('Lines pulled from userQueue.txt:')
                print(data)
                with open('seazerlog.txt',\
                 'a', encoding='utf-8') as seazerLog:
                     seazerLog.write(str(data) + '\n')
                tries = 0
                break
            except:
                print('Error: Too long probably.')
                with open('seazerlog.txt',\
                 'a', encoding='utf-8') as seazerLog:
                     seazerLog.write('Failed, attempt {}, trying again.\n'.format(tries))
                tries = tries + 1
                time.sleep(1)

print(os.path.dirname(__file__))
with open('seazerlog.txt', 'w', encoding='utf-8') \
as seazerLog:
    seazerLog.write('Log opened.\n\n')

while True:
    print('updating every {} seconds'.format(60 * 60 * tweetInterval))
    sendASong(tries)
    #wait for tweetInterval number hours
    time.sleep(60 * 60 * tweetInterval)
