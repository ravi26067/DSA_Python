import queue_using_stack


def test_enqueue():
    q = queue_using_stack.Queue()
    q.enQueue(5)
    q.enQueue(10)
    q.enQueue(1)
    assert q.s1 == [5, 10, 1]


def test_dequeue():
    q = queue_using_stack.Queue()
    q.enQueue(5)
    q.enQueue(10)
    q.enQueue(1)
    assert q.deQueue() == 5
    assert q.s1 == [10, 1]


def test_dequeue_empty_queue():
    q = queue_using_stack.Queue()
    assert q.deQueue() == -1


def test_print_queue():
    q = queue_using_stack.Queue()
    q.enQueue(5)
    q.enQueue(10)
    q.enQueue(1)
    assert q.printQueue() == "Queue: [5, 10, 1]"


def test_print_empty_queue():
    q = queue_using_stack.Queue()
    assert q.printQueue() == "Queue is empty"
