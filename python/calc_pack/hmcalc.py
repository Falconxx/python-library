#!/usr/bin/python

def tiles(width, height, tWidth, tHeight):
	area = width * height * 10
	tile = tWidth * tHeight *2
	return area / tile

	
def paint(width, height, performance):
	area = width * height * 3
	return area / performance
	
def panels(width, height, tWidth, tHeight):
	area = width * height * 5;
	panel = tWidth * tHeight * 4;
	return area / panel
