#coding:utf-8
from sqlalchemy import Table,Column,Integer,String,TIMESTAMP,create_engine,func,Boolean,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.schema import ForeignKey
import pymysql
from config import global_config


#设置一系列的基本参数
username = global_config.getRaw('config','database_username')
password = global_config.getRaw('config','database_password')
host = global_config.getRaw('config','database_host')
port = global_config.getRaw('config','database_port')
database = global_config.getRaw('config','database')

Base = declarative_base()
DB_CONNECT_STR = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8'
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
    location = Column(String(255),nullable=False) # 群所对应地点
    name = Column(String(255),nullable=False) # 群名
    path = Column(String(255),nullable=False) # 群所要发送的部分文件路径
    send = Column(Boolean,nullable=False,default=True) # 是否发送改群

def main():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()