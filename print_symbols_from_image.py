import numpy as np
import cv2

filename = ''
string_to_display = input()
len_string = len(string_to_display)
# img = cv2.imread('masked.png')
img = np.zeros(((len_string+1)*10, 30), np.uint8)
cv2.imshow('img', img)
cv2.waitKey(0)
for i in range(len_string):
	cv2.putText(img, str(string_to_display[i]), (5, int((i+1+0.5)*10)), cv2.FONT_HERSHEY_SIMPLEX, 0.35,
                (255, 255, 255), 1)
cv2.imshow('img', img)	
cv2.waitKey(0)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.resize(gray, None,fx=1/20, fy=1/20, interpolation = cv2.INTER_CUBIC)
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
rows = []
for i in range(thresh.shape[0]):
	row = []
	for j in range(thresh.shape[1]):
		row.append(thresh[i][j])
	rows.append(row)

for i in range(len(rows)):
	row = rows[i]
	row_string = ' '
	# print(row)
	for j in range(len(row)):
		symbol = '$' if row[j] == 0 else '_'
		row_string+=symbol
	print(row_string)