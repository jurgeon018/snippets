from threading import Thread, currentThread
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep, time
import random


def get_devices():
    devices = [
        ('www.device1.com', 443),
        ('www.device2.com', 443),
        ('www.device2.com', 8443),
        ('www.device3.com', 443),
        ('www.device4.com', 443),
        ('www.device5.com', 443),
        ('www.device5.com', 8443),
        ('www.device6.com', 443),
        ('www.device7.com', 443),
        ('www.device8.com', 443),
        ('www.device9.com', 443),
        ('www.device9.com', 8443),
        ('www.device10.com', 8083),
    ]
    return devices


def paginate(devices):
    per_page = 4
    paginated_devices = [devices[i:i+per_page] for i in range(0, len(devices), per_page)]
    return paginated_devices


def get_cert(host, port):
    if port in [8443, 8083, ]:
        sleep(10)
    elif port in [443, ]:
        sleep(2)
    else:
        raise Exception(f'!!!{host}:{port}')


def scan_device(device):
    start = time()
    host = device[0]
    port = device[-1]
    cert = get_cert(host, port)
    seconds = time() - start
    seconds = round(seconds)
    thread = currentThread().getName()
    print(f'Host {host} has been scanned on port {port} in {seconds} seconds in thread {thread}.')
    return cert


def perform_scan_devices(devices):
    for device in devices:
        scan_device(device)


def scan_devices():
    devices = get_devices()
    paginated_devices = paginate(devices)
    paginated_devices = [devices, ]
    start = time()

    threads = []
    for page in paginated_devices:
        p = paginated_devices.index(page) + 1
        thread = Thread(target=perform_scan_devices, args=[page, ], name=f'Thread-of-page-{p}')
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    end = round(time() - start)
    print(f'{len(devices)} devices has been scanned in {end} seconds.')

    # with ThreadPoolExecutor() as executor:
    #     results = executor.map(perform_scan_devices, paginated_devices)
    #     for result in results:
    #         print(result)

    # with ThreadPoolExecutor() as executor:
    #     results = []
    #     for page in paginated_devices:
    #         result = executor.submit(perform_scan_devices, page)
    #         results.append(result)
    #     results = as_completed(results)
    #     for result in results:
    #         print(result.result())

    # with ThreadPoolExecutor() as executor:
    #     results = []
    #     for page in paginated_devices:
    #         result = executor.submit(perform_scan_devices, page)
    #         results.append(result)
    #     for result in results:
    #         print(result.result())

    # with ThreadPoolExecutor() as executor:
    #     for page in paginated_devices:
    #         result = executor.submit(perform_scan_devices, page)
    #         print(result.result())


if __name__ == '__main__':
    scan_devices()
