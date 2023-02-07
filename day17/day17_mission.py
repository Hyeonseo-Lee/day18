def is_queue_full() :
	global SIZE, queue, front, rear
	if (rear != SIZE-1) :
		return False
	elif (rear == SIZE -1) and (front == -1) :
		return True
	else :
		for i in range(front+1, SIZE) :
			queue[i-1] = queue[i]
			queue[i] = None
		front -= 1
		rear -= 1
		return False

def is_queue_empty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (is_queue_full()) :
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if (is_queue_empty()) :
        # print("큐가 비었습니다.")
        return None
    # front == 0
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (is_queue_empty()) :
        print("큐가 비었습니다.")
        return None
    return queue[front+1]


SIZE = int(input("대기줄의 크기를 입력하세요 ==> "))
# queue = [ None for _ in range(SIZE) ]
queue = ["뷔", "정국", "지민", "진", "슈가"]
front = rear = -1

if __name__ == "__main__" :



        # if not is_queue_full():
        #     for i in range(SIZE):
        #         data = input("입력할 데이터 ==> ")
        #         enQueue(data)
        #         print("대기줄 상태 : ", queue)
        #
            print("대기줄 상태 : ", queue)
            for s in range(5):
                data = deQueue()
                a= queue[0]
                print(f'{a}님 식당에 들어감')
                for i in range(1, 5):
                    queue[i-1]=queue[i]
                    queue[i]= None
                print("대기줄 상태 : ", queue)

            print("식당 영업 종료!")








