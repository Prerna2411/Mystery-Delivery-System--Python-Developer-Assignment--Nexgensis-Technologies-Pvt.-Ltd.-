# 🚚 Mystery Delivery System

A Python-based logistics simulation system developed for the **Nexgensis Technologies Python Developer Assignment**.

The project simulates one full day of operations for a fictional logistics company **FastBox**, involving **warehouses, delivery agents, and packages**. The system intelligently assigns packages to the **nearest delivery agent using Euclidean distance**, simulates deliveries, and generates a performance report.

---

## 📌 Problem Statement

The objective is to simulate a logistics environment where:

- Multiple **warehouses** store packages
- Multiple **delivery agents** are available
- Packages must be assigned to the **nearest agent**
- Deliveries are simulated and analyzed

The final system produces:

- 📦 Delivered package count
- 📍 Total distance travelled by each agent
- ⚡ Agent efficiency score
- 🏆 Best-performing delivery agent

---

## ✨ Features

### Core Features

✅ Read and parse JSON input data manually  
✅ Euclidean distance calculation  
✅ Nearest agent assignment  
✅ Delivery simulation  
✅ Distance tracking per agent  
✅ Efficiency calculation  
✅ Best agent identification  
✅ Report generation in JSON format

### Bonus Features Implemented

✅ Random delivery delays (0–15 mins)  
✅ Export top performer to CSV

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries Used:**
  - `json`
  - `math`
  - `random`
  - `csv`

> No external dependencies required.

---

## 📂 Project Structure

```text
mystery-delivery-system/
│
├── main.py                 # Main simulation logic
├── test_case_1.json               # Input test data
├── report.json             # Generated delivery report
├── top_performer.csv       # Best agent export
├── README.md               # Project documentation

```

---

## ⚙️ How It Works

### Step 1: Read JSON Data

The system reads:

- Warehouses
- Delivery Agents
- Packages

from a JSON file.

Example:

```json
{
  "warehouses": {
    "W1": [0, 0]
  },
  "agents": {
    "A1": [5, 5]
  },
  "packages": [
    {
      "id": "P1",
      "warehouse": "W1",
      "destination": [30, 40]
    }
  ]
}
```

---

### Step 2: Agent Assignment

Each package is assigned to the **nearest delivery agent** using **Euclidean Distance** between:

```text
Agent → Warehouse
```

Distance Formula:

\[
\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

---

### Step 3: Delivery Simulation

For every package:

```text
Agent → Warehouse → Destination
```

The system calculates:

- Pickup distance
- Delivery distance
- Total travel distance

Optional **random delays** are also added for realism.

---

### Step 4: Performance Evaluation

Each delivery agent is evaluated based on:

### Efficiency Formula

```text
Efficiency = Total Distance / Packages Delivered
```

📌 **Lower efficiency = better performance**

Because less average distance is travelled per package.

---

## 📊 Sample Output

### Console Output

```text
========== FINAL REPORT ==========

{
    "A1": {
        "packages_delivered": 4,
        "total_distance": 76.39,
        "efficiency": 19.1
    },
    "A2": {
        "packages_delivered": 1,
        "total_distance": 31.36,
        "efficiency": 31.36
    },
    "A3": {
        "packages_delivered": 7,
        "total_distance": 137.9,
        "efficiency": 19.7
    },
    "A4": {
        "packages_delivered": 0,
        "total_distance": 0,
        "efficiency": 0
    },
    "best_agent": "A1"
}
```

---

## 📄 Generated Files

### 1. `report.json`

Stores final delivery analytics.

Example:

```json
{
    "best_agent": "A1"
}
```

### 2. `top_performer.csv`

Exports best-performing delivery agent.

Example:

```csv
Best Agent,Packages Delivered,Total Distance,Efficiency
A1,4,76.39,19.1
```

---

## 🧠 Engineering Assumptions

Since certain routing behaviors were not explicitly defined in the assignment, the following logical assumptions were made:

### 1. Independent Package Trips

Each package delivery is treated as an **independent trip**.

This means:

```text
Agent starts from original location
for every package delivery
```

instead of continuing from the previous delivery destination.

**Reason:**  
The assignment did not specify route continuity or package sequencing.

---

### 2. Tie-Breaking Logic

If two agents are equally close to a warehouse:

```text
Lexicographically smaller Agent ID wins
```

Example:

```text
A1 preferred over A2
```

---

### 3. Package Order

Packages are processed in the same order as they appear inside the input JSON file.

---

### 4. Random Delays

Delivery delays between:

```text
0–15 minutes
```

were introduced as an optional realism feature.

These delays **do not impact efficiency calculations**.

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/Prerna2411/Mystery-Delivery-System--Python-Developer-Assignment--Nexgensis-Technologies-Pvt.-Ltd.-.git
```

### Navigate to Project Folder

```bash
cd mystery-delivery-system
```

### Run Program

```bash
python main.py
```

---

## ✅ Validation

The system validates that:

```text
Total Packages Delivered
=
Total Packages in Input
```

to ensure simulation correctness.

---


---

