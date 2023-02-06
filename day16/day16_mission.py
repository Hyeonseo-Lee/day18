import random
import math


class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printStores(start) :
	current = start
	if current == None :
		return

	while current.link != head:
		current = current.link
		x, y = current.data[1:]
		print(current.data[0], '편의점, 거리:', math.sqrt(x*x + y*y))
	print()

def  store_list(store) :
	global memory, head, current, pre

	node = Node()
	node.data = store
	memory.append(node)

	if head == None :
		head = node
		node.link = head
		return


	nX, nY = node.data[1:]
	ndist = math.sqrt(nX * nX + nY * nY)
	headX, headY = head.data[1:]
	hdist = math.sqrt(headX * headX + headY * headY)

	if hdist > ndist :	# 헤드 앞에 삽입
		node.link = head
		last = head
		while last.link != head :
			last = last.link
		last.link = node
		head = node
		return

	current = head		# 중간에 데이터를 넣을 경우
	while current.link != head :
		pre = current
		current = current.link
		currX, currY = current.data[1:]
		cuDist = math.sqrt(currX * currX + currY * currY)
		if cuDist > ndist :
			pre.link = node
			node.link = current
			return

	current.link = node
	node.link = head



memory = []
head, current, pre = None, None, None


if __name__ == "__main__" :

	store_ar = []
	store_name = 'A'
	for _ in range(10) :
		store = (store_name, random.randint(1, 100), random.randint(1, 100))
		store_ar.append(store)
		store_name = chr(ord(store_name) + 1)	# 편의점 이름을 A->B->C… 으로 변경

	for store in store_ar :
		store_list(store)

	printStores(head)
