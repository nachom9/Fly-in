*This project has been created as part of the 42 curriculum by imelero-.*

# Fly-In Drones Simulator

## Description

Fly-In Drones is a pathfinding and simulation project where multiple drones must navigate through a network of interconnected zones to reach a final destination.

The goal is to simulate how drones move from a **start hub** to an **end hub**, respecting constraints such as:
- Zone capacity limits
- Connection capacity limits
- Special zone behaviors (restricted, priority, blocked)

The program parses a custom map file, computes optimal paths, and simulates drone movements turn by turn until all drones reach the goal.

---

## Instructions

### Installation

Clone the repository:

```bash
git clone <repository_url>
cd <repository_name>

Create a virtual environment and install dependencies:

make install
Execution

Run the simulator:

make run

By default, it uses:

map.txt

You can specify another map:

make run MAP=your_map.txt
Debug Mode
make debug MAP=your_map.txt
Linting
make lint

Strict mode:

make lint-strict
Clean Environment
make clean
Algorithm & Implementation
Pathfinding Strategy

The project uses a modified Dijkstra-like algorithm to compute paths dynamically.

Key characteristics:

Each zone transition has a cost
Costs are dynamically adjusted based on:
Number of drones in the next zone
Maximum capacity of the zone
Zone type (restricted zones increase cost)
Priority zones slightly reduce cost

This allows drones to:

Avoid congestion
Spread across multiple paths
Adapt to real-time conditions
Movement Simulation

The simulation runs in discrete turns:

Drones already in restricted zones are resolved first
Zones are processed in reverse order to prioritize forward movement
Each drone attempts to:
Compute a path to the goal
Move to the next zone if capacity allows

Connection capacities are temporarily reduced per turn to enforce constraints.

Handling Constraints

The system enforces:

Zone capacity (max_drones)
Connection capacity (max_link)
Blocked zones (cannot be entered)
Restricted zones (special delayed movement behavior)
Visual Representation

The simulation includes a visual output in the terminal:

Each drone movement is printed per turn

Format:

D1-zoneA-zoneB
Zones can have colors defined via metadata:
Colors are displayed using ANSI escape codes
This improves:
Readability of simulation steps
Tracking individual drone paths
Understanding congestion and flow
Features
Custom map parser with validation
Multiple drone support
Dynamic pathfinding
Zone types:
normal
restricted
priority
blocked
Connection capacity constraints
Turn-based simulation
Colored terminal output
Type hints with full mypy compliance
Makefile automation
Resources
Documentation & References
Python typing:
https://docs.python.org/3/library/typing.html
PEP 257 (Docstrings):
https://peps.python.org/pep-0257/
Dijkstra Algorithm:
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
Graph theory basics:
https://en.wikipedia.org/wiki/Graph_theory
AI Usage

AI (ChatGPT) was used as a support tool during development for:

Assisting with type hints and mypy compliance
Generating documentation (README and docstrings)

All algorithm design decisions, implementation logic, and debugging validation were performed and understood by the author.

Notes
The program strictly validates input maps and provides clear error messages.
All functions include type hints and pass mypy checks.
The project follows PEP 8 and PEP 257 conventions.