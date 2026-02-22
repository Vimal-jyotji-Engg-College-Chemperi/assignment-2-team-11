from suzuki_kasami import SuzukiKasami, IoTNode

def main():
    N = 4  # Number of IoT nodes

    print("\n===== Suzuki–Kasami Broadcast Algorithm Simulation =====\n")

    system = SuzukiKasami(N)

    nodes = []

    # Create IoT nodes
    for i in range(N):
        node = IoTNode(i, system)
        nodes.append(node)
        node.start()

    # Wait for all nodes to finish
    for node in nodes:
        node.join()

    print("\n===== Simulation Completed Successfully =====\n")


if __name__ == "__main__":
    main()
