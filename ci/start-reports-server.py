#! /usr/bin/env python
import subprocess
import sys
import time
from threading import Thread


def kill_process_silently(process):
    try:
        process.kill()
    except:
        pass


def stop_processes():
    for process in processes:
        kill_process_silently(processes[process])


def start_reports_server():
    process = None

    while running:
        try:
            print 'Reports server started at localhost:' + reports_server_port
            process = subprocess.Popen(['python', '-m', 'SimpleHTTPServer', reports_server_port],
                                       cwd=reports_dir)
            processes[str(process.pid)] = process
            process.wait()
        except Exception as e:
            print 'Reports server stopped at localhost:' + reports_server_port
            kill_process_silently(process)
            print(str(e))
            time.sleep(5)


if __name__ == '__main__':
    reports_server_port = '1313'
    running = True
    processes = {}
    reports_dir = str(sys.argv[1])

    reports_thread = Thread(target=start_reports_server)
    reports_thread.daemon = True
    reports_thread.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        running = False
        stop_processes()
        sys.exit(0)
