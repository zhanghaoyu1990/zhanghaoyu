#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    # 表名
    __tablename__ = 'user'

    # 表结构
    id = Column(int)
