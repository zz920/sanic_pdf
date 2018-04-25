from sample import send_a_request
from concurrent import futures


def send_multi_request():
    task_number, fail_number = 100, 0
    with futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_list = [executor.submit(send_a_request) for i in range(task_number)]
        print("All orders submitted")
        for future in futures.as_completed(future_list):
            if future.exception():
                fail_number += 1
    print("All task finished, result {} fail/{} total".format(fail_number, task_number))


if __name__ == "__main__":
    send_multi_request()
