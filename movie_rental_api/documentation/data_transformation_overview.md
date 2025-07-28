# Data Cleaning and Transformation Overview

## Purpose

This document outlines the data cleaning and transformation process applied to all datasets in the `data/cleaned/` directory prior to database seeding. The goal was to ensure referential integrity, eliminate null values in foreign key fields, and prepare all datasets for successful insertion into a normalized SQLite database.

---

## Target Datasets

The following six CSV files were cleaned:

- `users.csv`
- `admin_users.csv`
- `movies.csv`
- `rentals.csv`
- `payments.csv` (see separate detailed documentation)
- `reviews.csv`

---

## Tools Used

- **Language:** Python 3.11
- **Library:** pandas
- **Scripts:** `scripts/clean_data.py` and `scripts/rebuild_payments_from_rentals.py`
- **Storage Location:** `data/cleaned/`

---

## General Cleaning Actions

1. **Loaded Original Datasets:** All datasets were loaded from the extracted `movie_app_datasets` directory.
2. **Dropped Null-Only Columns:** Columns where all values were missing were removed entirely.
3. **Filled Foreign Keys:**
   - For `rentals`, any missing `user_id` or `movie_id` was filled with a random valid ID from the corresponding table.
   - For `reviews`, missing `user_id` and `movie_id` fields were similarly populated using existing data.
4. **Date Parsing:**
   - All `created_at`, `rental_date`, `due_date`, `return_date`, and `payment_date` fields were coerced into ISO 8601 datetime format (`YYYY-MM-DD`).
5. **Exported Cleaned Data:** Cleaned datasets were saved into `data/cleaned/` with the same file names.

---

## File-Specific Notes

### `users.csv`
- Null-free after original generation.
- No transformation necessary beyond date parsing.

### `admin_users.csv`
- Date fields (`created_at`) parsed as datetime.
- No additional foreign key cleanup required.

### `movies.csv`
- Missing values in optional fields (e.g. `description`, `rating`) were retained.
- No foreign key fields required transformation.

### `rentals.csv`
- Missing `user_id` and `movie_id` values were randomly filled from valid IDs in `users.csv` and `movies.csv`.
- Dates were parsed to datetime for `rental_date`, `due_date`, and `return_date`.

### `reviews.csv`
- Missing `user_id` and `movie_id` were randomly assigned from available values.
- Dates parsed to datetime.
- Rows without a `rating` were removed or retained depending on content validity.

---

## Result

All six datasets are now:
- Cleaned of nulls in key fields
- Aligned to support foreign key constraints
- Stored in `data/cleaned/` for use in database seeding

---

## Date of Cleaning

2025-07-28