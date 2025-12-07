# First_principles_Python_antrader.py

“Tiny CLI tool that helps you design clean Python functions using first principles (def + docstring + body + return).

# First Principles Python AntTrader

A tiny CLI-style helper project that shows **how to design Python functions and simple trading logic using first principles** – not by copying random tutorials, but by thinking clearly first:

- What should the function do?
- What does it need as input?
- What should it return?
- How do we keep the logic small, explicit and testable?

The project is also a stepping stone toward a simple **AntTrader-style price action strategy** (M15 Break-of-Structure → M1 logic later), but the main focus here is:  
**clear functions, deterministic behavior, and first principles thinking.**

---

## Goals

This repo is meant to:

- help beginner/intermediate developers understand how to build functions from scratch
- demonstrate a clean `def + docstring + body + return` structure
- show how to use basic Python building blocks:
  - variables, lists, dictionaries
  - simple “state machine” decisions (`if / elif / else`)
- prepare the ground for a future automated trading bot (AntTrader) without jumping directly into heavy ML

---

## What this project does (current scope)

The project contains:

- small, focused example functions built from first principles
  - e.g. simple “business logic” functions like `laske_tuotot` / `calculate_profits`
  - a clear example of a **Break-of-Structure (BOS)** detector on M15 candles:
    - input: lists of highs and lows
    - output: `1` (bullish BOS), `-1` (bearish BOS), or `0` (no signal)
- basic “orchestrator” idea for a future strategy:

```python
def run_strategy():
    # 1. fetch data
    # 2. detect BOS
    # 3. (later) check trend / price action
    # 4. (later) calculate SL/TP
    # 5. (later) risk calculation
    # 6. (later) build trade object
    # 7. (later) log the decision
    # 8. (later) send to MT5
    pass
```
