
def stack_full() :
	global SIZE, stack, top
	if (top >= SIZE-1) :
		return True
	else :
		return False

def stack_empty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def push(data) :
	global SIZE, stack, top
	if (stack_full()) :
		return
	top += 1
	stack[top] = data

def pop() :
	global SIZE, stack, top
	if (stack_empty()) :
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek() :
	global SIZE, stack, top
	if (stack_empty()) :
		return None
	return stack[top]


SIZE = 100
stack = [ None for _ in range(SIZE) ]
top = -1


if __name__ == "__main__" :

	with open("진달래꽃.txt", 'r', encoding='UTF8') as rfp :
		lineAry = rfp.readlines()

	print("----- 원본 -----")
	for line in lineAry :
		push(line)
		print(line, end = ' ')
	print()

	print("----- 거꾸로 처리된 결과 -----")
	while True :
		line = pop()
		if line == None :
			break

		m_stack = [None for _ in range(len(line))]
		m_top = -1

		for ch in line :
			m_top += 1
			m_stack[m_top] = ch

		while True :
			if m_top == -1 :
				break
			ch = m_stack[m_top]
			m_top -= 1
			print(ch, end = ' ')
