<<<<<<< HEAD
# OS_Lab_Assignment
=======
# OS Lab Assignments (ENCS351)

This repo contains two assignments for ENCS351 Operating Systems:

- **Assignment 1**: Process Creation and Management using Python's `os` module.
  - `process_management.py` — implements fork, exec, zombie/orphan demos, /proc inspection, nice/priority demo.
  - `output.txt` — sample outputs & terminal logs (include your run captures).
  - See `assignment1/README.md` for run instructions.

- **Assignment 2**: System startup and process simulation using `multiprocessing` and `logging`.
  - `startup_simulation.py`
  - `process_log.txt` — sample log from a run.

## Prerequisites
- Linux environment (WSL/Ubuntu recommended)
- Python 3.8+
- Git

## How to run (examples)
### Assignment 1
1. Task 1 - create children: `python3 process_management.py task1 4`
2. Task 2 - exec commands: `python3 process_management.py task2 "ls -l" "date"`
3. Zombie demo: `python3 process_management.py zombie`
4. Orphan demo: `python3 process_management.py orphan`
5. Inspect process: `python3 process_management.py inspect <PID>`
6. Priority demo: `python3 process_management.py priority 4`

### Assignment 2
Run:
```bash
python3 startup_simulation.py --n 3
>>>>>>> 2c6a365c41d3e4266bdb8d5a7865b2019790bbb1
