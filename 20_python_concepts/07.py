import unittest
import threading

def increment_counter(counter, num, lock):
    for _ in range(num):
        with lock:
            counter[0] += 1

class TestMultiThreading(unittest.TestCase):

    def test_increment_counter(self):
        counter = [0]
        num_threads = 5
        num_increments_per_thread = 1000
        lock = threading.Lock()

        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=increment_counter, args=(counter, num_increments_per_thread, lock))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        expected_value = num_threads * num_increments_per_thread
        self.assertEqual(counter[0], expected_value)

if __name__ == '__main__':
    unittest.main()