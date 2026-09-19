from multiprocessing import Process


def task(name):
    print(f"{name} running")


if __name__ == "__main__":
    p1 = Process(target=task, args=("process-1",))
    p2 = Process(target=task, args=("process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main process finished")