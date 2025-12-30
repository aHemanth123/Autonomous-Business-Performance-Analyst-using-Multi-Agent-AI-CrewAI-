# Autonomous  Performance Analyst

An **agentic AI system** that autonomously analyzes business performance data, detects trends and anomalies, generates executive-level insights, and produces a **real PDF business report** using a coordinated **multi-agent architecture** built with **CrewAI**.

---

## 📌 Project Overview

This project demonstrates how **Multi-Agent AI** can be applied to real-world business analytics problems.

Instead of a single LLM prompt, the system uses **specialized agents**, each responsible for a specific analytical task, collaborating through **explicit task context chaining** to deliver decision-ready insights.

---

## 🧠 Why Multi-Agent AI?

- Clear separation of responsibilities  
- Improved reasoning quality  
- Deterministic task execution  
- Scalable and maintainable architecture  

Each agent operates independently but collaborates via explicit task dependencies.

---

## 🏗️ System Architecture

CSV Business Data
↓
Data Ingestion Agent
↓
Trend Analysis Agent and Anomaly Detection Agent
↓
Business Insight Agent
↓
Report Generator Agent
↓
Executive PDF Report


---

## 🤖 Agents

| Agent | Responsibility |
|-----|----------------|
| **Data Ingestion Agent** | Reads CSV data, extracts KPIs, and summarizes the dataset |
| **Trend Analysis Agent** | Identifies revenue and sales trends over time |
| **Anomaly Detection Agent** | Detects unusual spikes, drops, or risk signals |
| **Business Insight Agent** | Converts analytics into strategic recommendations |
| **Report Generator Agent** | Produces an executive-ready PDF report |

---

## 📊 Data

- **Input Format:** CSV  
- **Fields:**  
  - `date` (parsed as datetime)  
  - `region`  
  - `revenue`  
  - `sales`  
- Supports time-series and region-wise analysis

---

## 🧩 Tech Stack

- **Python**
- **CrewAI** (Multi-Agent Orchestration)
- **Pandas** (Data Processing)
- **ReportLab** (PDF Generation)
- **LLMs** (Ollama / OpenAI compatible)

--- 
## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

- Python **>= 3.10**
- Git
- Virtual environment support

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv

```

Activate 
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux


# Install Dependencies
pip install -r requirements.txt

 

