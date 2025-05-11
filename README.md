# 🧠 MazeSolver (a.k.a. RoboRunner, MazeBot)

**MazeSolver** is a modular Python-based system for simulating and solving mazes using virtual robots. It uses a breadth-first search (BFS) algorithm to compute the shortest path through both predefined and randomly generated mazes, supporting both text and graphical interfaces.

---

## 🚀 Features

- 📐 Grid-based robot navigation with bounds checking  
- 🧱 Real-time obstacle detection and avoidance  
- 🧭 Direction-aware movement and orientation logic  
- 🗺️ Supports multiple maze maps:  
  - `almost_crazy_maze.txt` (uses `1`)  
  - `psycho_maze.txt` (uses `█`)  
  - `worlds_crazy_maze.txt` (uses `#`)  
- 🎨 Visual mode with Turtle graphics, or text-based simulation  
- 🧠 Pathfinding using BFS with early-exit optimization  
- 🔁 Replay of move history, with support for `reversed` and `silent` options  
- ⛓️ Customizable command-based control of robot behavior  

---

## 📁 Project Structure

```
.
├── robot.py                     # Entry point for launching robot REPL
├── import_helper.py             # Handles dynamic maze/world imports
├── maze/
│   ├── maze_solver.py           # BFS pathfinding and command generator
│   ├── obstacles.py             # Default obstacle logic
│   ├── almost_crazy_maze.py     # Obstacle parser for '1'-based maps
│   ├── psycho_maze.py           # Obstacle parser for '█'-based maps
│   ├── worlds_crazy_maze.py     # Obstacle parser for '#'-based maps
│   ├── *.txt                    # Maze layout files
├── world/
│   ├── text/
│   │   └── world.py             # Text-based robot simulation
│   ├── turtle/
│   │   └── world.py             # Turtle graphics-based visual simulation
│   └── turtle/
│       ├── soil.gif             # Background for turtle mode
│       ├── grass.gif            # Maze texture
│       └── timber2.gif          # Obstacle image
├── tests/
│   └── test_main.py             # Unit tests
```

---

## ▶️ How to Run

### Basic (default maze, text-based)
```bash
python3 robot.py
```

### With specific maze
```bash
python3 robot.py worlds_crazy_maze
python3 robot.py almost_crazy_maze
python3 robot.py psycho_maze
```

### With Turtle (GUI) mode
```bash
python3 robot.py turtle worlds_crazy_maze
```

---

## 🧪 Run Unit Tests

```bash
python3 -m unittest tests/test_main.py
```

---

## 🕹️ Robot Commands

| Command              | Description                                             |
|----------------------|---------------------------------------------------------|
| `HELP`               | Show help text                                          |
| `OFF`                | Power off the robot                                     |
| `FORWARD X`          | Move forward by `X` steps                               |
| `BACK X`             | Move backward by `X` steps                              |
| `RIGHT`              | Turn 90° right                                          |
| `LEFT`               | Turn 90° left                                           |
| `SPRINT X`           | Move forward by `X + (X-1) + ... + 1` steps             |
| `REPLAY`             | Replay all move commands                                |
| `REPLAY REVERSED`    | Replay in reverse order                                 |
| `REPLAY SILENT`      | Replay silently                                         |
| `REPLAY X-Y`         | Replay a range of previous commands                     |
| `MAZERUN`            | Run to the top edge using maze solver                   |
| `MAZERUN EDGE`       | Run to specified edge (`top`, `bottom`, `left`, `right`)|

---

## 🔍 How It Works

1. **Maze Generation**  
   - Parses maze layout from text files or generates obstacles randomly  
   - Obstacles are stored as coordinate tuples `(x, y)`  

2. **Pathfinding**  
   - Uses Breadth-First Search (BFS) to explore paths from the robot's position  
   - Prioritizes paths that lead toward the selected edge  
   - Tracks visited nodes and discards dead ends  

3. **Movement Translation**  
   - Converts a path of coordinates into robot-friendly commands (e.g., `forward`, `left`, `right`)  
   - Determines required turns and step distances between each point  

4. **Execution**  
   - Executes the generated command sequence in either text or turtle visual mode  
   - Collision detection and bounds enforcement are integrated  

---

## 🖼️ Turtle Mode

- Robot appears as a white turtle arrow  
- Obstacles are displayed using `timber2.gif`  
- Maze is rendered with `grass.gif` and bordered with green lines  
- Background is `soil.gif`  
- Supports real-time visual feedback via `turtle.update()`  

---

## 💡 Potential Improvements

- Add A* or Dijkstra’s algorithm for weighted pathfinding  
- Allow custom maze uploads via CLI  
- Implement multiple robots navigating simultaneously  
- Add animated or time-sensitive dynamic obstacles  
- Enable headless mode for automated testing  
- Visualize BFS exploration in turtle mode  

---

## 📦 Dependencies

This project only uses built-in Python modules:

- `random`  
- `turtle`  
- `sys`  
- `importlib`  
- `unittest`  

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

## 👨‍💻 Author

Created by [Your Name Here]. Contributions and feedback are welcome.
