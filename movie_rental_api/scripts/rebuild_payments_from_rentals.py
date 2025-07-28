import pandas as pd
import random
from pathlib import Path

# Load rentals
rentals = pd.read_csv("data/cleaned/rentals.csv")

# Create a new payments DataFrame
payment_methods = ["credit_card", "paypal", "gift_card", "debit_card"]
payment_statuses = ["completed", "pending", "failed", "refunded"]

# Seed random for reproducibility
random.seed(42)

payments = pd.DataFrame({
    "payment_id": range(1, len(rentals) + 1),
    "user_id": rentals["user_id"],
    "rental_id": rentals["rental_id"],
    "payment_date": pd.to_datetime(rentals["rental_date"], errors="coerce"),
    "amount": [round(random.uniform(2.99, 6.99), 2) for _ in range(len(rentals))],
    "payment_method": [random.choice(payment_methods) for _ in range(len(rentals))],
    "status": [random.choice(payment_statuses) for _ in range(len(rentals))]
})

# Save to cleaned/ folder
output_path = Path("data/cleaned/payments.csv")
payments.to_csv(output_path, index=False)

print(f"payments.csv rebuilt with {len(payments)} rows from rentals.csv")