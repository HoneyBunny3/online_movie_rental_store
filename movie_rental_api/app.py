from flask import Flask, jsonify, request
from models import db, User, AdminUser, Movie, Rental, Payment, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Movie Rental API"})

# -------- USERS --------
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

# -------- MOVIES --------
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([m.to_dict() for m in movies])

# -------- RENTALS --------
@app.route('/rentals', methods=['GET'])
def get_rentals():
    rentals = Rental.query.all()
    return jsonify([r.to_dict() for r in rentals])

# -------- PAYMENTS --------
@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([p.to_dict() for p in payments])

# -------- REVIEWS --------
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([r.to_dict() for r in reviews])

# -------- ADMIN USERS --------
@app.route('/admins', methods=['GET'])
def get_admins():
    admins = AdminUser.query.all()
    return jsonify([a.to_dict() for a in admins])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)