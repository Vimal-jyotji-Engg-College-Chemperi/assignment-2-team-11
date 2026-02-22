import threading
import time
import random

class SuzukiKasami:
    def __init__(self, n):
        self.N = n
        self.RN = [0] * n          # Request Number array
        self.LN = [0] * n          # Last served request number
        self.token_queue = []      # Queue of requesting nodes
        self.has_token = [False] * n
        self.has_token[0] = True   # Initially Node 0 has token
        self.lock = threading.Lock()

    def request_cs(self, i):
        with self.lock:
            self.RN[i] += 1
            print(f"Node {i} broadcasts request RN[{i}] = {self.RN[i]}")

            if not self.has_token[i]:
                if i not in self.token_queue:
                    self.token_queue.append(i)

    def receive_token(self, i):
        with self.lock:
            print(f"Node {i} enters Critical Section")
            time.sleep(1)

            # Update last served request
            self.LN[i] = self.RN[i]
            print(f"Node {i} exits Critical Section")

            # Check for pending requests
            for j in range(self.N):
                if self.RN[j] == self.LN[j] + 1 and j not in self.token_queue:
                    self.token_queue.append(j)

            # Pass token if needed
            if self.token_queue:
                next_node = self.token_queue.pop(0)
                self.has_token[i] = False
                self.has_token[next_node] = True
                print(f"Token passed from Node {i} to Node {next_node}")
            else:
                self.has_token[i] = True

class IoTNode(threading.Thread):
    def __init__(self, node_id, system):
        threading.Thread.__init__(self)
        self.node_id = node_id
        self.system = system

    def run(self):
        time.sleep(random.randint(1, 3))
        self.system.request_cs(self.node_id)

        while not self.system.has_token[self.node_id]:
            time.sleep(0.5)

        self.system.receive_token(self.node_id)


# Main Program
if __name__ == "__main__":
    N = 4  # Number of IoT nodes
    system = SuzukiKasami(N)

    nodes = []
    for i in range(N):
        node = IoTNode(i, system)
        nodes.append(node)
        node.start()

    for node in nodes:
        node.join()