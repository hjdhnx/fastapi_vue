#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : curd_hiker_rule.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/12/2


from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, func, distinct
from common.curd_base import CRUDBase
from ..models.hiker_rule import HikerRuleType,HikerRule


class CURDHikerRuleType(CRUDBase):

    def get(self, db: Session, _id: int, to_dict: bool = True):
        """ 通过id获取 """
        record = db.query(self.model).filter(self.model.id == _id, self.model.is_deleted == 0).first()
        return record if not to_dict else {
            'id': record.id,
            'name': record.name,
            'count_num': record.count_num,
            'active': record.active,
        }

    def create(self, db: Session, *, obj_in, creator_id: int = 0):
        obj_in_data = obj_in if isinstance(obj_in, dict) else jsonable_encoder(obj_in)
        if db.query(self.model).filter(self.model.name == obj_in_data['name'],
                                       self.model.is_deleted == 0).first():  # 如果已经有这个开发者qq返回None
            return None
        obj_in_data['creator_id'] = creator_id
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, _id: int, obj_in, updater_id: int = 0):
        obj_in_data = obj_in if isinstance(obj_in, dict) else jsonable_encoder(obj_in)
        res = super().update(db, _id=_id, obj_in=obj_in_data, modifier_id=updater_id)
        return res

    def search(self, db: Session, *, name: str = "", count_num: int = None,
               page: int = 1, page_size: int = 25) -> dict:
        filters = []
        if count_num is not None:
            filters.append(self.model.count_num == count_num)
        if name:
            filters.append(self.model.name.like(f"%{name}%"))
        records, total, _, _ = self.get_multi(db, page=page, page_size=page_size, filters=filters)
        return {'results': records, 'total': total}

class CURDHikerRule(CRUDBase):

    def get(self, db: Session, _id: int, to_dict: bool = True):
        """ 通过id获取 """
        record = db.query(self.model).filter(self.model.id == _id, self.model.is_deleted == 0).first()
        return record if not to_dict else {
            'id': record.id,
            'name': record.name,
            'type_id': record.type_id,
            'dev_id': record.dev_id,
            'value': record.value,
            'url': record.url,
            'state': record.state,
            'auth': record.auth,
            'auth_date_time': record.auth_date_time,
            'time_over': record.time_over,
            'b64_value': record.b64_value,
            'home_url': record.home_url,
            'pic_url': record.pic_url,
            'is_json': record.is_json,
            'is_redirect': record.is_redirect,
            'is_tap': record.is_tap,
            'can_discuss': record.can_discuss,
            'is_json_list': record.is_json_list,
            'data_type': record.data_type,
            'version': record.version,
            'author': record.author,
            'note': record.note,
            'good_num': record.good_num,
            'bad_num': record.bad_num,
            'reply_num': record.reply_num,
            'is_safe': record.is_safe,
            'is_good': record.is_good,
            'is_white': record.is_white,
            'not_safe_note': record.not_safe_note,
            'last_active': record.last_active,
        }

    def create(self, db: Session, *, obj_in, creator_id: int = 0):
        obj_in_data = obj_in if isinstance(obj_in, dict) else jsonable_encoder(obj_in)
        if db.query(self.model).filter(self.model.name == obj_in_data['name'],
                                       self.model.is_deleted == 0).first():  # 如果已经有这个开发者qq返回None
            return None
        obj_in_data['creator_id'] = creator_id
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, _id: int, obj_in, updater_id: int = 0):
        obj_in_data = obj_in if isinstance(obj_in, dict) else jsonable_encoder(obj_in)
        res = super().update(db, _id=_id, obj_in=obj_in_data, modifier_id=updater_id)
        return res

    def search(self, db: Session, *, name: str = "", count_num: int = None,
               page: int = 1, page_size: int = 25) -> dict:
        filters = []
        if count_num is not None:
            filters.append(self.model.count_num == count_num)
        if name:
            filters.append(self.model.name.like(f"%{name}%"))
        records, total, _, _ = self.get_multi(db, page=page, page_size=page_size, filters=filters)
        return {'results': records, 'total': total}


curd_hiker_rule_type = CURDHikerRuleType(HikerRuleType)
curd_hiker_rule = CURDHikerRule(HikerRule)