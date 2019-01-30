from flask import (
    make_response,
    abort
)
from config import db
from models import (
    Person,
    PersonSchema
)


def get_all():
    people = Person.query.order_by(Person.lname).all()
    person_jsons = PersonSchema(many=True)

    return person_jsons.dump(people).data

def get_one(person_id):
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is not None:
        person_json = PersonSchema
        return person_json.dump(person).data
    else:
        abort(
            404, 'Person not found for Id: {person_id}'.format(person_id=person_id)
        )

def create(person):
    fname = person.get('fname')
    lname = person.get('lname')

    existing_person = Person.query \
        .filter(Person.fname == fname) \
        .filter(Person.lname == lname) \
        .one_or_none()

    if existing_person is None:
        person_schema = PersonSchema()
        new_person = schema.load(person, session=db.session).data

        db.session.add(new_person)
        db.session.commit()

        return schema.dump(new_person).data, 201

    else:
        abort(
            409, f'Person {fname} {lname} exists already.'
        )

def delete(person_id):
    pass

def update(person_id):
    pass