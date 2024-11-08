from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'my_flask_db'
DB_USER = 'myuser'
DB_PASSWORD = 'user1'

# SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary overhead

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Function to get a direct database connection for raw SQL queries
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Define the Item model using SQLAlchemy
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'

# Route to display the index page
@app.route('/')
def index():
    # Fetch all items from the database using SQLAlchemy
    items = Item.query.all()  # Fetch all rows from 'my_table'
    return render_template('index.html', items=items)

# Route to add a new item
@app.route('/add', methods=['POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        
        # Create a new Item instance and add it to the database using SQLAlchemy
        new_item = Item(name=item_name)
        db.session.add(new_item)
        db.session.commit()
        
        return redirect(url_for('index'))

# Route to delete an item
@app.route('/delete/<int:id>')
def delete_item(id):
    # Find the item by ID and delete it
    item_to_delete = Item.query.get_or_404(id)
    db.session.delete(item_to_delete)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()  # Create all tables
    app.run(debug=True)
