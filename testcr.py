import json
from testap import db


class Office(db.Model):
    __tablename__ = 'emp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90),nullable= False)
    lastname = db.Column(db.String(80),nullable= False)


    def json(self):
        return{'id':self.id, 'name':self.name, 'lastname':self.lastname}

    def add_emp(_name, _lastname) :
        new_emp = Office(name=_name, lastname=_lastname) 
        db.session.add(new_emp)
        db.session.commit()

    def get_emp(id):
        return[Office.json(Office.query.filter_by(id=id).first())]  


    def update_emp(_id, _name, _lastname):
        emp_to_update = Office.query.filter_by(id=_id).first()
        emp_to_update.name= _name
        emp_to_update.lastname=_lastname
        db.session.commit()

    def delete_emp(_id, _name, _lastname):
        emp_to_delete = Office.query.filter_by(id=_id).first()
        emp_to_delete.name= _name
        emp_to_delete.lastname=_lastname
        db.session.commit()

class Stud(db.Model):
    __tablename__= 'student'
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(90),nullable= False)
    slastname = db.Column(db.String(80),nullable= False)

    def json(self):
        return{'id':self.id, 'sname':self.sname, 'slastname':self.slastname}
  
    def add_stud(_sname, _slastname) :
        new_stud = Stud(sname=_sname, slastname=_slastname) 
        db.session.add(new_stud)
        db.session.commit()

    def get_stud(id):
      return[Stud.json(Stud.query.filter_by(id=id).first())]  

    def delete_stud(_id, _sname, _slastname):
        stud_to_delete = Stud.query.filter_by(id=_id).first()
        stud_to_delete.sname= _sname
        stud_to_delete.slastname=_slastname
        db.session.commit()

def update_stud(_id, _sname, _slastname):
        stud_to_update = Stud.query.filter_by(id=_id).first()
        stud_to_update.sname= _sname
        stud_to_update.slastname=_slastname
        db.session.commit()
