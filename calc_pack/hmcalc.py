#!/usr/bin/python2.7

def tiles(width, height, tWidth, tHeight):
	area = width * height * 7
	tile = tWidth * tHeight * 5
	return area / tile

	
def paint(width, height, performance):
	area = width * height * 4
	return area / performance
	
def panels(width, height, tWidth, tHeight):
	area = width * height * 5;
	panel = tWidth * tHeight * 10;
	return area / panel
