from collections import deque
from threading import Thread
from subprocess import Popen, PIPE


class Pinger(object):
    def __init__(self, hosts, thread_c=4):
        self.hosts = hosts
        self.thread_c = thread_c  # default is 4
        self.status = {"alive": [], "dead": []}

    def ping(self, ip):
        p = Popen(["ping", "-c", "1", "-W", "1", ip], stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        if p.returncode == 0:
            self.status["alive"].append(ip)
        else:
            self.status["dead"].append(ip)

    def dequeue(self):
        while True:
            if self.hosts:
                ip = self.hosts.popleft()
            else:
                return None
            self.ping(ip)

    def start(self):
        threads = []
        for i in range(self.thread_c):
            t = Thread(target=self.dequeue)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        return self.status


def main():
    hosts = deque(["127.0.0.1", "8.8.8.8", "8.8.4.4", "127.0.0.7"])
    ping = Pinger(hosts, thread_c=2)
    h = ping.start()
    print(h["alive"])


if __name__ == "__main__":
    main()
