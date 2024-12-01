from flask import render_template, request, redirect, url_for, flash
from models import db, Bike # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        # This route should retrieve all items from the database and display them on the page.
        bikes = Bike.query.all()
        print(bikes)
        return render_template('index.html', bikes=bikes)



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



    @app.route('/edit', methods=['GET','POST'])
    def edit():
        
        if request.method == 'POST':
     #       brand=request.form['brand'],
      #          model=request.form['model'],
       #         cc=int(request.form['cc']),
        #        fuel_capacity=int(request.form['fuel_capacity']),
         #       engine_type=request.form['engine_type'],
          #      seat_height=request.form['seat_height']
        #db.session.commit()
            return redirect(url_for('index'))
        else:
            id = request.args.get('id', '')
            bike = Bike.query.get_or_404(id)
            return render_template('edit.html', bike = bike)



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')


