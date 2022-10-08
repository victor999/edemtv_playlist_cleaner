# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:31:58 2022

@author: Victor

edem tv m3u8 cleaner
removing FHD, orig and +1, +2, etc channels 
"""

import string

def convert(fileName):
	f = open(fileName, encoding="utf8")
	lines = f.readlines()
	stationLinesCounter = 0
	linesRes = []
	
	print(lines)
	
	for line in lines:
		if stationLinesCounter > 0:
			stationLinesCounter -= 1
			continue
		if 'FHD' in line:
			stationLinesCounter = 2
			continue
		if '+1' in line:
			stationLinesCounter = 2
			continue
		if '+2' in line:
			stationLinesCounter = 2
			continue
		if '+3' in line:
			stationLinesCounter = 2
			continue
		if '+4' in line:
			stationLinesCounter = 2
			continue
		if '+5' in line:
			stationLinesCounter = 2
			continue
		if '+6' in line:
			stationLinesCounter = 2
			continue
		if '+7' in line:
			stationLinesCounter = 2
			continue
		if '+8' in line:
			stationLinesCounter = 2
			continue
		if 'orig' in line:
			stationLinesCounter = 2
			continue
		print(line)
		linesRes.append(line)
		
	f2 = open('playlistRes.m3u8', "w", encoding="utf8")
	f2.writelines(linesRes)
		
			


def main():
	fileName = 'playlist.m3u8'
	convert(fileName)

if __name__ == "__main__":
	main()