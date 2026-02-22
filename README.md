**Suzuki–Kasami’s Broadcast Algorithm in IoT Network**


**Overview**

This is a modular implementation of Suzuki–Kasami’s Broadcast Mutual Exclusion Algorithm, designed to simulate controlled access to shared resources in IoT-based distributed systems.
The algorithm ensures that only one IoT node can access the critical section at any given time, maintaining consistency and coordination across connected devices.This implementation is built using Python and follows an Object-Oriented Programming (OOP) approach.

**Algorithm Description**

Suzuki–Kasami’s algorithm is a token-based distributed mutual exclusion algorithm introduced by Suzuki and Kasami in 1985.

It uses:

- Broadcast REQUEST messages

- A unique TOKEN for critical section access

- Sequence numbers to track requests

- Request number (RN) array

- Last served request (LN) array

Unlike permission-based algorithms, Suzuki–Kasami’s algorithm allows a process to enter the critical section only if it holds the TOKEN.

**Key Features**

- Fully Distributed (No central coordinator)

- Token-based mutual exclusion

- Reduced message complexity compared to permission-based algorithms

- Efficient for IoT networks

- Deadlock-free

- Starvation-free

- Object-Oriented implementation

**Project Structure**
suzuki-kasami-assignment/

├── suzuki_kasami.py   # Contains SuzukiKasamiProcess class  
├── main.py            # Executes and simulates IoT nodes  
└── README.md          # Project documentation  
Files Description
1️⃣ suzuki_kasami.py – Core Algorithm Module

Contains the main class:

SuzukiKasamiProcess

Responsible for:

Maintaining request numbers (RN array)

Handling token structure (LN array and queue)

Broadcasting requests

Receiving requests

Passing token

Entering and exiting critical section

2️⃣ main.py – Execution File

Creates multiple IoT node objects

Simulates distributed IoT devices using threads

Starts request-execute-release cycle

Displays system behavior

Installation & Setup
Prerequisites

Python 3.7 or higher

No external libraries required

Installation

Download or clone the project folder.

Navigate to the directory:

cd suzuki-kasami-assignment
Usage

Run the simulation:

python main.py

The program will simulate multiple IoT nodes requesting access to a shared resource.

How the Algorithm Works
1️⃣ Initialization

Create N IoT nodes

One node initially holds the TOKEN

Each node maintains:

RN array (Request Numbers)

Token structure (LN array + Queue)

2️⃣ Requesting Critical Section

When a node wants to enter:

Increment its request number

Broadcast REQUEST(node_id, sequence_number) to all other nodes

Wait until it receives the TOKEN

3️⃣ Receiving a Request

Upon receiving a REQUEST:

Update RN[sender] = received_sequence_number

If the node holds the TOKEN and is not in critical section:

Send TOKEN to requesting node

4️⃣ Entering Critical Section

A node enters the critical section only if:

It possesses the TOKEN

No need to wait for permissions from all nodes.

5️⃣ Releasing Critical Section

After execution:

Update LN[node_id] inside TOKEN

Check RN array for pending requests

Add eligible nodes to TOKEN queue

Pass TOKEN to next node in queue

Example Execution Flow

Assume 3 IoT nodes: N0, N1, N2

N0 initially holds TOKEN

N1 broadcasts request

N0 sends TOKEN to N1

N1 enters critical section

After completion, N1 passes TOKEN to next requester

Only one node holds the TOKEN at any time.

Message Complexity

For N nodes:

REQUEST messages: N − 1

TOKEN messages: 1

Total messages per critical section entry:

(N − 1) + 1 = N messages

This is more efficient than permission-based algorithms like Lamport’s.

API Reference
Class: SuzukiKasamiProcess
Constructor
SuzukiKasamiProcess(pid: int, total_nodes: int)

Parameters:

pid → Node ID

total_nodes → Total number of IoT nodes in the network

Methods

request_critical_section()

Broadcasts request and waits for TOKEN.

receive_request(sequence_number, sender_pid)

Handles incoming request and updates RN array.

receive_token(token)

Receives TOKEN and enters critical section if eligible.

enter_critical_section()

Executes critical section.

release_critical_section()

Updates LN and passes TOKEN to next node.

System Properties
Mutual Exclusion

Only one IoT node accesses shared resource at a time.

Fairness

Requests are handled in sequence number order.

Deadlock-Free

No circular waiting occurs.

Starvation-Free

Every requesting node eventually receives TOKEN.

Applications in IoT Network

Smart home device coordination

Sensor data synchronization

Distributed IoT transaction management

Edge device resource sharing

Industrial IoT automation

Advantages

Lower message overhead than permission-based algorithms

Efficient for moderate-sized IoT networks

Simple token management

No need for global clock synchronization

Suitable for wireless broadcast environments

Limitations

Token loss can block system

Not fault tolerant by default

Not ideal for very large-scale IoT networks

Requires reliable message delivery

Future Improvements

Add token recovery mechanism

Add fault tolerance

Simulate network delays and packet loss

Add visualization dashboard

Add performance comparison with Lamport’s algorithm

Conclusion

This demonstrates a complete implementation of Suzuki–Kasami’s Broadcast Mutual Exclusion Algorithm for IoT networks.

The simulation ensures safe and efficient access to shared IoT resources using a token-based mechanism and broadcast communication, making it suitable for understanding distributed synchronization in IoT environments.



