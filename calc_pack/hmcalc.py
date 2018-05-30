#!/usr/bin/python2.7

def tiles(width, height, tWidth, tHeight):
	area = width * height * 5
	tile = tWidth * tHeight * 3
	return area / tile

	
def paint(width, height, performance):
	area = width * height * 2
	return area / performance
	
def panels(width, height, tWidth, tHeight):
	area = width * height * 3;
	panel = tWidth * tHeight * 5;
	return area / panel
