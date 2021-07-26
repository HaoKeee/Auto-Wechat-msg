#coding:utf-8
from sqlalchemy import Table,Column,Integer,String,TIMESTAMP,create_engine,func,Boolean,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker,relationship
from sqlalchemy.schema import ForeignKey
import pymysql


#设置一系列的基本参数
Base = declarative_base()
DB_CONNECT_STR = "mysql+pymysql://root:@localhost:3306/wechat_groups?charset=utf8"
engine = create_engine(DB_CONNECT_STR,encoding="utf8",convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


class Groups(Base):
    __tablename__ = 'groups'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(255),nullable=False)