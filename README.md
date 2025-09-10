# Short Python Projects
## Mini code blocks showcasing applied business logic and real-world problem solving

### Project 1: EMI Calculator
A Python-based **EMI (Equated Monthly Installment) Calculator** that helps users estimate their monthly payments for car loans.  
Includes **loan eligibility validation, down payment checks, and multi-year repayment comparison (3, 5, and 7 years).**

#### Features
- Validates down payment against car on-road price.
- Checks loan eligibility based on maximum loan ratio.
- Calculates EMI using the standard financial formula.
- Compares EMIs for 3, 5, and 7-year periods.
- Displays total payable amount for each option.
- Clean and formatted currency output.

#### Use Cases
- Car buyers estimating monthly repayments.
- Financial enthusiasts exploring interest calculations.

#### Python Concepts Demonstrated
- Loops
- Conditions
- User input handling
- Applied financial logic (EMI calculation formula)

### Project 2: Cart Abandonment Analyzer
A single-file Python script that simulates Mixpanel-like cart events and analyzes cart abandonment. Identifies abandoned carts using a time-based threshold, reports abandonment rate, and highlights peak abandonment hours. Designed to demonstrate applied business logic and event-time analysis without external datasets or dependencies.

#### Features
- Hardcoded, realistic sample events (15 events) including edge cases (exactly 24h purchase, >24h delayed purchase, checkout started but not completed).
- Groups events by (user_id, product_id) to represent unique carts.
- Defines abandonment using a configurable time threshold (default 24 hours).
- Calculates abandonment metrics:
    - Total carts analyzed (unique user–product pairs)
    - Number of abandoned vs completed carts
    - Abandonment rate (%)
- Identifies peak abandonment hours (hour-of-day distribution).
- Lightweight — no external libraries required (uses standard library only).
- DEBUG flag to toggle intermediate prints for development/testing.

#### Use Cases
- Demonstrates event-based data analysis with a clear, real-world business context.
- Can be used as a template to develop more advanced analytics scripts (e.g., for e-commerce, SaaS, or subscription churn).
- Provides a foundation for integrating with product analytics tools like Mixpanel or GA4 in future iterations.

#### Python Concepts Demonstrated
- Lists & dictionaries (data structures)
- Tuple keys for dictionary grouping (user_id, product_id)
- Loops and conditional logic (for, if/else)
- datetime and timedelta for time arithmetic
- Aggregation with collections.Counter
- Basic script structure and simple debug controls
