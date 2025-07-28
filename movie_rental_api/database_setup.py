import pandas as pd
from flask import Flask
from models import db, User, AdminUser, Movie, Rental, Payment, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def load_data():
    with app.app_context():
        print("Dropping and recreating all tables...")
        db.drop_all()
        db.create_all()

        def safe_parse_dates(df, columns):
            for col in columns:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
            return df

        print("Loading users.csv...")
        users_df = pd.read_csv('data/movie_app_datasets/users.csv')
        users_df = safe_parse_dates(users_df, ['created_at'])
        users_df.dropna(subset=['user_id'], inplace=True)
        for _, row in users_df.iterrows():
            db.session.add(User(**row.to_dict()))

        print("Loading admin_users.csv...")
        admins_df = pd.read_csv('data/movie_app_datasets/admin_users.csv')
        admins_df = safe_parse_dates(admins_df, ['created_at'])
        admins_df.dropna(subset=['admin_id'], inplace=True)
        for _, row in admins_df.iterrows():
            db.session.add(AdminUser(**row.to_dict()))

        print("Loading movies.csv...")
        movies_df = pd.read_csv('data/movie_app_datasets/movies.csv')
        movies_df = safe_parse_dates(movies_df, ['created_at'])
        movies_df.dropna(subset=['movie_id'], inplace=True)
        for _, row in movies_df.iterrows():
            db.session.add(Movie(**row.to_dict()))

        print("Loading rentals.csv...")
        rentals_df = pd.read_csv('data/movie_app_datasets/rentals.csv')
        rentals_df = safe_parse_dates(rentals_df, ['rental_date', 'due_date', 'return_date'])
        rentals_df.dropna(subset=['rental_id'], inplace=True)
        for _, row in rentals_df.iterrows():
            db.session.add(Rental(**row.to_dict()))

        print("Loading payments.csv...")
        payments_df = pd.read_csv('data/movie_app_datasets/payments.csv')
        payments_df = safe_parse_dates(payments_df, ['payment_date'])
        payments_df.dropna(subset=['payment_id'], inplace=True)
        for _, row in payments_df.iterrows():
            db.session.add(Payment(**row.to_dict()))

        print("Loading reviews.csv...")
        reviews_df = pd.read_csv('data/movie_app_datasets/reviews.csv')
        reviews_df = safe_parse_dates(reviews_df, ['created_at'])
        reviews_df.dropna(subset=['review_id'], inplace=True)
        for _, row in reviews_df.iterrows():
            db.session.add(Review(**row.to_dict()))

        db.session.commit()
        print("All data loaded successfully.")

if __name__ == '__main__':
    load_data()