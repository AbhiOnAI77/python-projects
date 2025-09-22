"""
Customer Support Ticket Simulation
---------------------------------
Project Goal:
Simulate how AI agents at a customer service helpdesk might categorize support tickets
into departments and flag urgent tickets. This simulation includes:
- Categorization by keywords
- Assignment of customer type
- Priority (High/Medium/Low) assignment
- Urgency detection
- Reporting summary
"""

from collections import Counter

# Phase 1: AI agent defines complaint categories & keywords
# =========================================================

TICKET_CATEGORIES = {
    "Delivery": ["delay", "not arrived", "late", "shipping", "delivery", "arrived", "package", "driver"],
    "Payment": ["refund", "payment", "charged", "invoice", "credit card", "bank", "billing", "subscription"],
    "Technical": ["error", "bug", "password", "login", "app", "crashing", "credentials", "system"],
    "General": ["info", "question", "support", "warranty", "cancel", "exchange", "return"],
    "Product": ["damaged", "defective", "wrong size", "doesn't fit", "quality", "smell"]
}

## Keywords that signal urgent attention
URGENT_KEYS = ["refund", "error", "complaint", "urgent"]

# Phase 2: Sample tickets for AI agent to review
# ==============================================

BASE_TICKETS = [
    "My order #ORD12345 was supposed to arrive 3 days ago but I still haven't received it. The tracking shows 'out for delivery' since Monday. Can you please check what happened?",
    "I noticed I was charged $49.99 twice on my credit card for the same wireless headphones order. I only ordered one pair. Please refund the duplicate charge.",
    "I've been trying to reset my password for 2 hours but I'm not receiving the reset email. I checked spam folder too. My email is correct in your system.",
    "The laptop I ordered arrived with a cracked screen and several scratches on the lid. The packaging seemed fine so this must have happened before shipping.",
    "My food delivery was 90 minutes late and arrived cold. I had to reheat everything. I'd like a refund or credit for my next order since dinner was ruined.",
    "What does your 2-year warranty cover for electronics? I bought a tablet 6 months ago and the battery isn't holding charge properly anymore.",
    "My payment was declined but my bank says there are no issues on their end. I tried 3 different cards and none worked. Is there a problem with your payment system?",
    "The delivery driver left my package outside in the rain even though I have delivery instructions to ring the bell. Now the contents are water damaged.",
    "I keep getting 'invalid credentials' error when trying to log in, but I'm 100% sure my username and password are correct. This started happening yesterday.",
    "I want to cancel my monthly subscription immediately. I've been charged for 3 months but haven't used the service since the first month.",
    "The product description said it was compatible with my device but it doesn't fit properly. The charging port is blocked when the case is on.",
    "I ordered a medium shirt but received a large. I need to exchange it for the correct size before my event next week. Do you have medium in stock?",
    "The promo code SAVE8989 isn't working at checkout. It says it's expired but your email said it's valid until the end of this month.",
    "I accidentally ordered 2 items to my old address. Can you change the shipping address before it ships? I moved last month and forgot to update it.",
    "The app keeps crashing every time I try to view my order history. I've tried restarting my phone and updating the app but it still doesn't work.",
    "I need a receipt for my business expense report but can't find it in my email or account. The order number is #ORD67890 from last Tuesday.",
    "The installation service technician never showed up for our scheduled 2-4 PM appointment. I took time off work and waited all afternoon.",
    "I'm trying to use my reward points for this purchase but the system says I don't have any, even though my account shows 2,500 points available.",
    "The furniture I ordered has a strong chemical smell and is making my family sick. We can't keep it in the house. Is this normal for new furniture?",
    "I ordered express shipping and paid extra $15 but the package is coming via regular shipping. Can I get a refund for the shipping upgrade?"
]

# Phase 3: AI agent categorization functions
# ==========================================

def categorize_ticket(text):
    """Categorize a ticket into a department based on keywords."""
    text_lower = text.lower()
    if any(word in text_lower for word in ['order', 'delivery', 'arrived', 'shipping', 'tracking']):
        return "Order & Shipping"
    elif any(word in text_lower for word in ['payment', 'charged', 'refund', 'billing', 'card']):
        return "Billing & Payments"
    elif any(word in text_lower for word in ['password', 'login', 'account', 'app', 'technical']):
        return "Technical Support"
    elif any(word in text_lower for word in ['damaged', 'defective', 'warranty', 'quality']):
        return "Product Issues"
    elif any(word in text_lower for word in ['cancel', 'subscription', 'service']):
        return "Account Management"
    else:
        return "General Inquiry"

def is_urgent(ticket, urgent_keys):
    """Check if a ticket contains urgent keywords."""
    ticket_lower = ticket.lower()
    return any(word in ticket_lower for word in urgent_keys)

# Phase 4: AI agent simulates ticket processing
# =============================================

SIMULATED_TICKETS = []

for i in range(1, 51):
    # AI agent picks a base ticket from historical data
    base_ticket = BASE_TICKETS[i % len(BASE_TICKETS)]
    text = base_ticket + f" [Ticket #{i:03d}]"

    # AI agent identifies the customer type
    if i % 10 in [1, 2, 3]:
        customer_type = "Champions"
    elif i % 10 in [4, 5]:
        customer_type = "At-Risk Customers"
    elif i % 10 in [6, 7, 8]:
        customer_type = "New Customers"
    else:
        customer_type = "Hibernating"

    # AI agent analyzes ticket text to assign category
    category = categorize_ticket(text)

    # AI agent assigns priority based on category & customer importance
    if category in ["Product Issues", "Order & Shipping", "Billing & Payments"]:
        priority = "High"
    elif customer_type == "Champions" or category == "Account Management":
        priority = "Medium"
    else:
        priority = "Low"

    # AI agent flags urgent tickets
    urgent = is_urgent(text, URGENT_KEYS)

    # AI agent stores ticket information for reporting
    SIMULATED_TICKETS.append({
        "id": i,
        "text": text,
        "customer_type": customer_type,
        "category": category,
        "priority": priority,
        "urgent": urgent
    })

# Phase 5: AI agent generates summary report
# ==========================================

category_count = Counter([t["category"] for t in SIMULATED_TICKETS])
urgent_count = sum([1 for t in SIMULATED_TICKETS if t["urgent"]])

print("=== Ticket Category Breakdown ===")
for cat, count in category_count.items():
    print(f"{cat}: {count}")

print(f"\nTotal Urgent Tickets: {urgent_count} / {len(SIMULATED_TICKETS)}")