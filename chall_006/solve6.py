# By Arun Kumar Shreevastava
# Mission 6
# http://goo.gl/S395x6

from PIL import Image, ImageDraw
import ast

MULIPLIER = 20

im = Image.new('RGBA', (25*MULIPLIER, 25*MULIPLIER), (255, 255, 255, 0)) 
draw = ImageDraw.Draw(im)

coordinates = [ast.literal_eval(_) for _ in open('m6.data').readlines()]

# First Approach
# Plot lines
# Result not much
# for i in range(len(coordinates)-1):
# 	startX = coordinates[i][0]*10
# 	startY = coordinates[i][1]*10
# 	endX = coordinates[i+1][0]*10
# 	endY = coordinates[i+1][1]*10

# 	draw.line((startX, startY, endX, endY), fill=128)


# 2nd Approach
# Worked but image was only 25*25 so i had to enlarge it
# for xy in coordinates:
# 	draw.point((xy[0],xy[1]), fill=128)

# Used rectangle to plot a bigger point
for xy in coordinates:
	draw.rectangle((xy[0]*MULIPLIER, xy[1]*MULIPLIER, xy[0]*MULIPLIER+MULIPLIER, xy[1]*MULIPLIER+MULIPLIER), fill=0)



im.save('result_m6.jpg', 'JPEG')

# Then used Barcode Scanner on my phone and got the answer but was too
# lazy to type it so used an online QR Code decoder to decode it
# https://zxing.org/w/decode.jspx

# Ans = Mirrored QR? Seriously?!