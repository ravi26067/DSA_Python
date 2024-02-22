from Queue.queue_using_stack import Queue


def test_enqueue():
    q = Queue()
    q.enQueue(5)
    q.enQueue(10)
    q.enQueue(1)
    assert q.s1 == [5, 10, 1]


def test_dequeue():
    q = Queue()
    q.enQueue(5)
    q.enQueue(10)
    q.enQueue(1)
    assert q.deQueue() == 5
    assert q.s1 == [10, 1]


def test_dequeue_empty_queue():
    q = Queue()
    assert q.deQueue() == -1


def test_print_queue():
    q = Queue()
    q.enQueue(5)
    q.enQueue(10)
    q.enQueue(1)
    assert q.printQueue() == "Queue: [5, 10, 1]"


def test_print_empty_queue():
    q = Queue()
    assert q.printQueue() == "Queue is empty"
