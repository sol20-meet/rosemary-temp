from database import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session
from model import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
	a=query_all()
	return render_template('index.html', reservations=a)

@app.route('/add' , methods=['GET','POST'])
def add():
	if request.method == 'GET':
		return render_template('add.html' , data=[{'name':'Roza'}, {'name':'Hanan'}, {'name':'Juleen'}, {'name':'Sol'}, {'name':'Ameer'}, {'name':'Hamoodi'}, {'name':'Tarek'}, {'name':'Elias'}, {'name':'Waseem'}, {'name':'Ghassan'}, {'name':'Hisham'}] , data1=[{'time':'12:00'},{'time':'12:15'},{'time':'12:30'},{'time':'12:45'},{'time':'13:00'},{'time':'13:15'},{'time':'13:30'},{'time':'13:45'},{'time':'14:00'},{'time':'14:15'},{'time':'14:30'},{'time':'14:45'},{'time':'15:00'},{'time':'15:15'},{'time':'15:30'},{'time':'15:45'},{'time':'16:00'},{'time':'16:15'},{'time':'16:30'},{'time':'16:45'},{'time':'17:00'},{'time':'17:15'},{'time':'17:30'},{'time':'17:45'},{'time':'18:00'},{'time':'18:15'},{'time':'18:30'},{'time':'18:45'},{'time':'19:00'},{'time':'19:15'},{'time':'19:30'},{'time':'19:45'},{'time':'20:00'},{'time':'20:15'},{'time':'20:30'},{'time':'20:45'},{'time':'21:00'},{'time':'21:15'},{'time':'21:30'},{'time':'21:45'},{'time':'22:00'},{'time':'22:00 +'}])
	else:
		print("Creating Reservation Object")
		reserveName = request.form['reserveName']
		fullName = request.form['fullName']
		reserveTime = request.form.get('comp_select1')
		reserveDay = request.form['reserveDay']
		numOfpeople = request.form.get('comp_select3')
		location = request.form.get('comp_select2')
		phone_num = request.form['phoneNum']
		waiterName = request.form.get('comp_select')
		isEating = request.form['isEating']
		closedMenu = request.form['closedMenu']
		notes = request.form['notes']

		add_res(reserveName,fullName,reserveTime,reserveDay,numOfpeople,location,phone_num,waiterName,None,isEating,closedMenu,notes)
		print("Done!")
		return redirect('/')

@app.route('/view' , methods=['GET' , 'POST'])
def view():
	if request.method == 'GET':
		a = query_all()
		return render_template('view.html' , Reservations = a)
	else:
		objId = request.form['deleteBtn']
		print(objId)
		print(objId)
		print(objId)
		print(objId)
		reservation = session.query(Reservation).filter(Reservation.id == objId).first()
		print(reservation)
		session.delete(reservation)
		session.commit()
		return redirect('/')



# @app.route('/view/<int:res_id>' , methods=['GET' , 'POST'])
# def view1():
# 	if request.method == 'GET':
# 		reservation = session.query(Reservation).filter(Reservation.id == res_id).first()
# 		reservation.isComing = True
# 		session.commit()
# 		return redirect('/view')
# 	else:
# 		redirect('/add')


# @app.route('/edit' , methods=['GET' , 'POST'])
# def edit():
# 	if request.methods == 'GET' :
# 		a = query_all()
# 		return render_template('edit.html' , res = a)
	
	

if __name__ == '__main__':
	app.run(debug=True)
