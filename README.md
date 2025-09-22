# Short Python Projects

Mini Python projects demonstrating applied business logic and real-world problem solving.

---

## Badges
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Project 1: EMI Calculator](https://img.shields.io/badge/EMI_Calculator-Completed-brightgreen)](./emi_calculator.py)
[![Project 2: Cart Abandonment Analyzer](https://img.shields.io/badge/EMI_Calculator-Completed-brightgreen)](./cart_abandonment_analyzer.py)
![Project 3: AI Helpdesk Ticket Simulation](https://img.shields.io/badge/AI_Helpdesk-Completed-brightgreen)

---

## Table of Contents
- [Project 1: EMI Calculator](#project-1-emi-calculator)
- [Project 2: Cart Abandonment Analyzer](#project-2-cart-abandonment-analyzer)
- [Project 3: AI Helpdesk Ticket Simulation](#project-3-ai-helpdesk-ticket-simulation)
- [Tech Stack / Skills](#tech-stack--skills)

---

## Project 1: EMI Calculator
**EMI (Equated Monthly Installment) Calculator** for car loans with **loan eligibility validation, down payment checks, and multi-year comparison (3, 5, 7 years).**

**Features:**

| Feature | Description |
|---------|-------------|
| Down Payment Validation | Checks against car on-road price |
| Loan Eligibility | Validates based on maximum loan ratio |
| EMI Calculation | Uses standard financial formula |
| Multi-Year Comparison | Calculates EMI for 3, 5, and 7-year options |
| Total Payable | Displays total amount for each option |
| Output | Formatted currency display |

**Use Cases:** Car buyers estimating payments, financial enthusiasts exploring interest calculations  

**Python Concepts:** Loops, conditional logic, user input handling, applied financial formulas  

---

## Project 2: Cart Abandonment Analyzer
Single-file Python script simulating **Mixpanel-like cart events** to identify abandoned carts and calculate metrics.

**Features:**

| Feature | Description |
|---------|-------------|
| Sample Events | 15 hardcoded events including edge cases |
| Unique Cart Grouping | By `(user_id, product_id)` |
| Abandonment Threshold | Configurable, default 24 hours |
| Metrics | Total carts, abandoned vs completed, abandonment rate |
| Peak Hours | Hour-of-day analysis |
| Lightweight | Uses only Python standard library |
| Debug Mode | Toggle intermediate prints |

**Use Cases:** Demonstrates event-based analysis, template for e-commerce/SaaS, foundation for analytics tool integration  

**Python Concepts:** Lists & dicts, tuple keys, loops & conditionals, datetime & timedelta, aggregation with Counter  

---

## Project 3: AI Helpdesk Ticket Simulation
Simulation of AI agents **categorizing tickets, flagging urgency, and assigning priority**.

**Features:**

| Feature | Description |
|---------|-------------|
| Complaint Categories | Keywords for department classification |
| Ticket Expansion | Sample tickets expanded to larger dataset |
| Customer Types | Champions, At-Risk, New, Hibernating |
| Category Assignment | Departments: Order & Shipping, Billing & Payments, Technical Support, Product Issues, Account Management, General Inquiry |
| Priority Levels | High, Medium, Low |
| Urgency Flag | Keywords trigger urgent status |
| Summary Report | Counts per category & urgent tickets |
| Agent Comments | Illustrates AI reasoning |

**Use Cases:** Simulates AI-based support workflows, tests categorization and priority assignment, demonstrates automated triaging  

**Python Concepts:** Loops, conditions, string handling, dictionary/list manipulation, Counter, modular structure, AI simulation logic  

---

## Tech Stack / Skills
- Python 3.x  
- Data structures: lists, dicts, tuples  
- Applied business logic & problem-solving  
- Event-time analysis & simulation  
- Automation & AI reasoning logic
