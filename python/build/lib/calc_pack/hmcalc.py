#!/usr/bin/python3

def tiles(width, height, tWidth, tHeight):
	area = width * height * 5
	tile = tWidth * tHeight * 3
	return area / tile

	
def paint(width, height, performance):
	area = width * height * 2
	return area / performance
	
def panels(width, height, tWidth, tHeight):
	area = width * height * 9;
	panel = tWidth * tHeight * 8;
	return area / panel
