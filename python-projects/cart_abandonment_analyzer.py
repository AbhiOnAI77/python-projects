"""
Cart Abandonment Analyzer
-------------------------
Simulates shopping cart events, detects abandoned carts based on a time threshold,
calculates abandonment rate, and identifies peak abandonment hours.

Each event is represented as a dictionary with keys: user_id, product_id, event, timestamp, cart_value.
Events include 'cart_viewed', 'checkout_started', and 'order_completed'.
Timestamps are in "YYYY-MM-DD HH:MM" format.

Sample data defined below with the following edge cases:
A. Normal purchase within threshold: User 1, 7.
B. Simple abandonment: User 2, 6, 8.
C. Checkout started but no completion: User 3, 6.
D. Purchase at exactly 24h (should not count as abandoned): User 4.
E. Purchase after 26h (should count as abandoned if threshold=24): User 5.
F. Multiple abandoned products for same user: User 8.
"""

from datetime import datetime, timedelta
from collections import Counter

# Debug mode used for intermediate checks (set to True while developing)
DEBUG = False

# Sample data defined below with the following edge cases:
'''
Normal purchase within threshold: User 1, 7.
Simple abandonment: User 2, 6, 8.
Checkout started but no completion: User 3, 6.
Purchase at exactly 24h (should not count as abandoned): User 4.
Purchase after 26h (should count as abandoned if threshold=24): User 5.
Multiple abandoned products for same user: User 8.
'''

# Each event is represented as a dictionary with keys: user_id, product_id, event, timestamp, cart_value
# Events include 'cart_viewed', 'checkout_started', and 'order_completed'
# Timestamps are in "YYYY-MM-DD HH:MM" format

events = [
    # --- Day 1: 2025-09-06 ---
    # User 1: Completes purchase within 2 hours (not abandoned)
    {"user_id": 1, "product_id": "P101", "event": "cart_viewed", "timestamp": "2025-09-06 09:00", "cart_value": 120},
    {"user_id": 1, "product_id": "P101", "event": "order_completed", "timestamp": "2025-09-06 11:00", "cart_value": 120},

    # User 2: Views cart but does not purchase (abandoned)
    {"user_id": 2, "product_id": "P202", "event": "cart_viewed", "timestamp": "2025-09-06 14:00", "cart_value": 80},

    # --- Day 2: 2025-09-07 ---
    # User 3: Starts checkout but no purchase (abandoned)
    {"user_id": 3, "product_id": "P303", "event": "cart_viewed", "timestamp": "2025-09-07 10:00", "cart_value": 150},
    {"user_id": 3, "product_id": "P303", "event": "checkout_started", "timestamp": "2025-09-07 10:15", "cart_value": 150},

    # User 4: Buys after exactly 24 hours (edge case that should not be abandoned if threshold=24)
    {"user_id": 4, "product_id": "P404", "event": "cart_viewed", "timestamp": "2025-09-07 08:00", "cart_value": 200},
    {"user_id": 4, "product_id": "P404", "event": "order_completed", "timestamp": "2025-09-08 08:00", "cart_value": 200},

    # User 5: Buys after 26 hours (edge case that should be considered abandoned if threshold=24)
    {"user_id": 5, "product_id": "P505", "event": "cart_viewed", "timestamp": "2025-09-07 06:00", "cart_value": 300},
    {"user_id": 5, "product_id": "P505", "event": "order_completed", "timestamp": "2025-09-08 08:00", "cart_value": 300},

    # --- Day 3: 2025-09-08 ---
    # User 6: Checkout started but no completion (abandoned)
    {"user_id": 6, "product_id": "P606", "event": "cart_viewed", "timestamp": "2025-09-08 09:00", "cart_value": 50},
    {"user_id": 6, "product_id": "P606", "event": "checkout_started", "timestamp": "2025-09-08 09:15", "cart_value": 50},

    # User 7: Instant buy (not abandoned)
    {"user_id": 7, "product_id": "P707", "event": "cart_viewed", "timestamp": "2025-09-08 12:00", "cart_value": 180},
    {"user_id": 7, "product_id": "P707", "event": "order_completed", "timestamp": "2025-09-08 12:05", "cart_value": 180},

    # User 8: Views two products but buys neither (both abandoned)
    {"user_id": 8, "product_id": "P808", "event": "cart_viewed", "timestamp": "2025-09-08 16:00", "cart_value": 90},
    {"user_id": 8, "product_id": "P909", "event": "cart_viewed", "timestamp": "2025-09-08 16:10", "cart_value": 120}
]

# Timestamps converted to datetime objects for easier manipulation
for event in events: 
    event["timestamp"] = datetime.strptime(event["timestamp"], "%Y-%m-%d %H:%M")

if DEBUG:
    print("\n--- Debug: Sample Converted Events ---")
    for event in events[:5]:
        print(event)

# Group events by user and product
grouped_events = {}

for event in events:
    key = (event["user_id"], event["product_id"])
    if key not in grouped_events:
        grouped_events[key] = []
    grouped_events[key].append(event)

# Detect Abandoned Carts 
abandon_threshold = timedelta(hours=24)
abandoned_carts = []
completed_carts = []

for key, ev_list in grouped_events.items():
    ev_list = sorted(ev_list, key=lambda x: x["timestamp"])
    cart_start, order_time = None, None

    for ev in ev_list: 
        if ev["event"] in ["cart_viewed", "checkout_started"] and cart_start is None:
            cart_start = ev["timestamp"]
        if ev["event"] == "order_completed":
            order_time = ev["timestamp"]
            break # focus here is solely on first purchase 

    # Classify cart based on events and timing below
    if cart_start:
        if order_time and order_time - cart_start <= abandon_threshold:
            completed_carts.append(key)
        else:
            abandoned_carts.append(key)

# Abandonment Rate Calculation 
total_carts = len(abandoned_carts) + len(completed_carts)
abandonment_rate = (len(abandoned_carts) / total_carts) * 100 if total_carts > 0 else 0.0

# Peak abandonment hours analysis
abandonment_hours = Counter()

for key in abandoned_carts:
    evs = sorted(grouped_events[key], key=lambda x: x["timestamp"])
    cart_start = next((ev["timestamp"] for ev in evs if ev["event"] in ["cart_viewed", "checkout_started"]), None)
    if cart_start:
        abandonment_hours[cart_start.hour] += 1

# Final Results
print("\n--- Cart Abandonment Analysis Results ---")
print(f"\nTotal Carts Analyzed: {total_carts}")
print(f"\nAbandoned Carts:", len(abandoned_carts))
print(f"Completed Carts:", len(completed_carts))
print(f"\nAbandonment Rate: {abandonment_rate:.2f}%")

print("\nAbandonment Hours Distribution:")
for hour, count in sorted(abandonment_hours.items()):
    print(f"{hour:02d}:00 - {count} abandonments")

if abandonment_hours:
    peak_hour, peak_count = abandonment_hours.most_common(1)[0]
    print(f"\nPeak Abandonment Hour: {peak_hour:02d}:00 with {peak_count} abandonments")
else:
    print("\nNo abandonments recorded.")
