import multiprocessing

process_ls = ['p1', 'p2', 'p3', 'p4']

def count(name):
    for i in range(1, 100):
        print(name, ' : ', i, end=' ')

# 1. Process : 하나의 함수에 process 할당
def multiprocessing_process():
    proc = multiprocessing.Process(target=count, args=(['ps']))
    proc.start()
    proc.join()

# 2. Pool을 이용해 하나의 함수를 지정한 process들이 나눠서 수행
def multiprocessing_pool():

    # 멀티 쓰레딩 pool 사용 : Pool은 함수 실행에 대한 병렬화
    pool = multiprocessing.Pool(processes=4)
    pool.map(count, process_ls) # process들에게 해당 함수 작업을 할당
    pool.close()

    pool.join() # 작업 완료 기다려주기 (block 상태 됨)

# 3. Queue : 각각의 프로세스 사이에 서로 communication이 필요할때 사용 (또다른 방법은 pipe)
# put data
def creator(data, q):
    for item in data:
        q.put(item)

# get data
def my_consumer(q):
    while True:
        data = q.get()
        processed = data * 2
        print(processed)

        # 들어온 data가 -1이면 끝끝
        if data == -1:
            break

def multiprocessing_queue():
    q = multiprocessing.Queue()
    data = [5, 10, 13, -1]
    process_one = multiprocessing.Process(target = creator, args=(data, q))
    process_two = multiprocessing.Process(target = my_consumer, args=(q,))
    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()

if __name__ =='__main__':
    print('\n process : ')
    multiprocessing_process()
    print('\n pool : ')
    multiprocessing_pool()
    print('\n queue : ')
    multiprocessing_queue()