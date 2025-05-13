from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first() 
    users_one = users_one.to_dict() if users_one else users_one

    res = {
        'users_one': users_one,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    id:int = raw_data.id
    name:str = raw_data.name
    contact_information:str = raw_data.contact_information


    record_to_be_added = {'id': id, 'name': name, 'contact_information': contact_information}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()


    user_edit_records = db.query(models.Users).filter(models.Users.name == name).first()
    for key, value in {'id': id, 'name': name, 'contact_information': name}.items():
          setattr(user_edit_records, key, value)
    db.commit()
    db.refresh(user_edit_records)
    user_edit_records = user_edit_records.to_dict() 


    delete_records = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == int).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        delete_records = record_to_delete.to_dict() 

    res = {
        'users_inserted_record': users_inserted_record,
        'user_edit_records': user_edit_records,
        'delete_records': delete_records,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:int = raw_data.id
    name:str = raw_data.name
    contact_information:str = raw_data.contact_information


    record_to_be_added = {'id': id, 'name': name, 'contact_information': contact_information}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()


    user_edit_records = db.query(models.Users).filter(models.Users.name == name).first()
    for key, value in {'id': id, 'name': name, 'contact_information': name}.items():
          setattr(user_edit_records, key, value)
    db.commit()
    db.refresh(user_edit_records)
    user_edit_records = user_edit_records.to_dict() 


    delete_records = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == int).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        delete_records = record_to_delete.to_dict() 

    res = {
        'users_inserted_record': users_inserted_record,
        'user_edit_records': user_edit_records,
        'delete_records': delete_records,
    }
    return res

