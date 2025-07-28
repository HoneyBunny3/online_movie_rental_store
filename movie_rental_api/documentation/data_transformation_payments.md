# Data Transformation: Rebuilding payments.csv from rentals.csv

## Objective

To ensure clean data relationships and avoid integrity errors during database seeding, we rebuilt the `payments.csv` file so that it accurately reflects the rental activity recorded in `rentals.csv`.

This transformation enforces that:
- Every `payment` record corresponds to a valid rental
- `user_id`, `rental_id`, and `payment_date` are sourced directly from the `rentals` table
- No orphaned or mismatched records exist in `payments.csv`

---

## Source of Truth

**rentals.csv** was used as the authoritative dataset for this process. All payment records were derived from existing rentals, ensuring relational integrity between the two tables.

---

## Fields Populated

Each row in the new `payments.csv` contains the following fields:

| Field           | Source           | Description                                  |
|----------------|------------------|----------------------------------------------|
| payment_id      | Auto-generated   | Unique identifier starting from 1            |
| user_id         | rentals.csv      | Directly matched from rental's user_id       |
| rental_id       | rentals.csv      | Rental's primary key                         |
| payment_date    | rentals.csv      | Mirrors the rental_date                      |
| amount          | Randomized       | Float between 2.99 and 6.99                  |
| payment_method  | Randomized       | One of: credit_card, paypal, gift_card, debit_card |
| status          | Randomized       | One of: completed, pending, failed, refunded |

---

## Script Used

A standalone Python script named `rebuild_payments_from_rentals.py` was created and stored in the `scripts/` directory.

This script:
1. Loads `rentals.csv` from `data/cleaned/`
2. Constructs a matching payment entry for each rental
3. Randomizes realistic payment details
4. Saves the new dataset to `data/cleaned/payments.csv`

---

## Execution

To rebuild `payments.csv`, run the following:

```bash
python3 scripts/rebuild_payments_from_rentals.py
````

This will overwrite any existing `data/cleaned/payments.csv` with a clean, normalized version derived from the rentals table.

---

## Follow-Up

After running this script, re-seed your SQLite database using:

```bash
python3 database_setup.py
```

---

## Outcome

* 1000 clean `payment` records now mirror the 1000 rental records.
* Seeding the database completes without foreign key or NULL constraint violations.
* Data integrity between `rentals` and `payments` is guaranteed.