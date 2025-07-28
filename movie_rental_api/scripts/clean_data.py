import pandas as pd
import os
import random

# Paths
raw_dir = os.path.join("data", "raw")
clean_dir = os.path.join("data", "cleaned")
os.makedirs(clean_dir, exist_ok=True)

# Load base data
users = pd.read_csv(os.path.join(raw_dir, "users.csv"))
movies = pd.read_csv(os.path.join(raw_dir, "movies.csv"))
rentals = pd.read_csv(os.path.join(raw_dir, "rentals.csv"))
payments = pd.read_csv(os.path.join(raw_dir, "payments.csv"))
reviews = pd.read_csv(os.path.join(raw_dir, "reviews.csv"))
admin_users = pd.read_csv(os.path.join(raw_dir, "admin_users.csv"))

# Clean rentals
if 'user_id' in rentals.columns:
    rentals['user_id'] = rentals['user_id'].apply(
        lambda x: x if pd.notnull(x) and x != '' else random.choice(users['user_id'].dropna().tolist())
    )

if 'movie_id' in rentals.columns:
    rentals['movie_id'] = rentals['movie_id'].apply(
        lambda x: x if pd.notnull(x) and x != '' else random.choice(movies['movie_id'].dropna().tolist())
    )

# Clean payments
if 'user_id' in payments.columns:
    payments['user_id'] = payments['user_id'].apply(
        lambda x: x if pd.notnull(x) and x != '' else random.choice(users['user_id'].dropna().tolist())
    )

if 'rental_id' in payments.columns:
    payments['rental_id'] = payments['rental_id'].apply(
        lambda x: x if pd.notnull(x) and x != '' else random.choice(rentals['rental_id'].dropna().tolist())
    )

# Clean reviews
if 'user_id' in reviews.columns:
    reviews['user_id'] = reviews['user_id'].apply(
        lambda x: x if pd.notnull(x) and x != '' else random.choice(users['user_id'].dropna().tolist())
    )

if 'movie_id' in reviews.columns:
    reviews['movie_id'] = reviews['movie_id'].apply(
        lambda x: x if pd.notnull(x) and x != '' else random.choice(movies['movie_id'].dropna().tolist())
    )

# Ensure rental_date is datetime
rentals['rental_date'] = pd.to_datetime(rentals['rental_date'], errors='coerce')

# Fill missing payment_date using latest rental_date from rentals table per user_id
if 'payment_date' in payments.columns:
    def get_latest_rental_date(user_id):
        user_rentals = rentals[rentals['user_id'] == user_id]
        if not user_rentals.empty:
            return user_rentals['rental_date'].max()
        return pd.NaT

    payments['payment_date'] = payments.apply(
        lambda row: row['payment_date']
        if pd.notnull(row['payment_date'])
        else get_latest_rental_date(row['user_id']),
        axis=1
    )


# Save cleaned files
users.to_csv(os.path.join(clean_dir, "users.csv"), index=False)
admin_users.to_csv(os.path.join(clean_dir, "admin_users.csv"), index=False)
movies.to_csv(os.path.join(clean_dir, "movies.csv"), index=False)
rentals.to_csv(os.path.join(clean_dir, "rentals.csv"), index=False)
payments.to_csv(os.path.join(clean_dir, "payments.csv"), index=False)
reviews.to_csv(os.path.join(clean_dir, "reviews.csv"), index=False)

print("Data cleaned and saved to /data/cleaned/")