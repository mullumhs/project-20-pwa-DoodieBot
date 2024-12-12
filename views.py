from flask import render_template, request, redirect, url_for, flash
from models import db, Bike # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):
# to register home page and print things fromdata base
    @app.route('/', methods=['GET'])
    def get_items():
        search_query = request.args.get('query')
    
        if search_query:
            print (search_query)
            bikes = Bike.query.filter(Bike.brand.ilike(f'%{search_query}%')).all()
        else:
            bikes = Bike.query.all()
        return render_template('index.html', bikes=bikes)

# for searching and querying items from the data base
    @app.route('/search', methods=['GET'])
    def bike_search():
        if request.method == 'post':
            query = request.form['search']
            return redirect(url_for('get_items', query = query ))

# adding an item to the data base
    @app.route('/add', methods=['GET','POST'])
    def create_item():
        if request.method == 'POST':
            new_bike = Bike(
                brand=request.form['brand'],
                model=request.form['model'],
                cc=int(request.form['cc']),
                fuel_capacity=int(request.form['fuel_capacity']),
                engine_type=request.form['engine_type'],
                seat_height=request.form['seat_height']
            )
            db.session.add(new_bike)
            db.session.commit()
            return redirect(url_for('get_items'))
        return render_template('add.html', message='Item added successfully')


# dealing with editing an existing item inj the data base 
    @app.route('/edit', methods=['GET','POST'])
    def edit():

        
     # if statement to gather all atributs of an item   
        if request.method == 'POST':
            id = request.form['id']
            print(id)
            bike = Bike.query.get(id)
            
            print(bike.model)

            bike.brand=request.form['brand']
            bike.model=request.form['model']
            bike.cc=int(request.form['cc'])
            bike.fuel_capacity=int(request.form['fuel_capacity'])
            bike.engine_type=request.form['engine_type']
            bike.seat_height=request.form['seat_height']
            db.session.commit()
            return redirect(url_for('get_items'))
        id = request.args.get("id")
        bike = db.get_or_404(Bike, id)
        return render_template('edit.html', bike = bike)


# delete function 
    @app.route('/delete', methods=['GET'])
    def delete_item():
        id = request.args.get("id")
        bike = db.get_or_404(Bike, id)
        print(bike)
        db.session.delete(bike)
        db.session.commit() 
        return redirect(url_for('get_items'))




        




