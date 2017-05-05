# Livesteam Video Link : https://www.youtube.com/watch?v=HN_tI601jNU

tree = [[[[[['5',[['6','7'], ['8','9']]],'A'],'2'], ['1',['3',['B','C']]]],'0'],['4',[['F','E'],'D']]]


# http://gynvael.vexillium.org/ext/029c3f5565df98b7cf43c5172e3064323678d81c.txt
msg = '''1000000111000101100011110000010000000111
0000010000111000000100000000000101000000
1000000101000100000100000000000001000000
0000000101001100001110100010110000001000
0000100001111000001001100000001010000010
1000001000000000000010100010000010100110
0001010000010110000001001100000001001100
00011101'''.replace('\n','')

ans = ''
subtree = tree

for c in msg:
	if c == '0':
		subtree = subtree[0]
	if c == '1':
		subtree = subtree[1]
	if isinstance(subtree, str):
		ans += subtree
		subtree = tree

print ans.decode('hex')

# Ans = 'I Like Trees. Flowers too.'