from sqlalchemy import String, Integer, Column, Text, DateTime, create_engine, ForeignKey, Boolean, JSON
from sqlalchemy.types import ARRAY
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker

from config import DB_USER, DB_NAME, DB_PORT, DB_HOST, DB_PASS

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    role_name = Column(Text, nullable=False)
    role_permissions = Column(JSON)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    hashed_password = Column(String(length=1024), nullable=False)
    email = Column(String(length=1024), unique=True, index=True, nullable=False)
    user_name = Column(Text, nullable=False)
    user_surname = Column(Text, nullable=False)
    favorite = Column(ARRAY(Integer), nullable=True)
    registration_date = Column(DateTime, default=datetime.utcnow())

    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)


class Brand(Base):
    __tablename__ = 'brands'

    brand_id = Column(Integer, primary_key=True)
    brand_name = Column(Text, nullable=False)


class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(Text, nullable=False)


class Style(Base):
    __tablename__ = 'styles'

    style_id = Column(Integer, primary_key=True)
    style_name = Column(Text, nullable=False)


class Color(Base):
    __tablename__ = 'colors'

    color_id = Column(Integer, primary_key=True)
    color_name = Column(Text, nullable=False)


class Material(Base):
    __tablename__ = 'materials'

    material_id = Column(Integer, primary_key=True)
    material_name = Column(Text, nullable=False)


class Stone(Base):
    __tablename__ = 'stones'

    stone_id = Column(Integer, primary_key=True)
    stone_name = Column(Text, nullable=False)


class Cutting(Base):
    __tablename__ = 'cuttings'

    cutting_id = Column(Integer, primary_key=True)
    cutting_name = Column(Text, nullable=False)


class Weaving(Base):
    __tablename__ = 'weavings'

    weaving_id = Column(Integer, primary_key=True)
    weaving_name = Column(Text, nullable=False)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(Text, nullable=False)
    brand = Column(Integer, ForeignKey('brands.brand_id'), nullable=False)
    category = Column(Integer, ForeignKey('categories.category_id'), nullable=False)
    material = Column(Integer, ForeignKey('materials.material_id'), nullable=False)
    material_color = Column(Integer, ForeignKey('colors.color_id'), nullable=False)
    cutting = Column(Integer, ForeignKey('cuttings.cutting_id'), nullable=True)
    stone = Column(Integer, ForeignKey('stones.stone_id'), nullable=True)
    weaving = Column(Integer, ForeignKey('weavings.weaving_id'), nullable=True)
    style = Column(Integer, ForeignKey('styles.style_id'), nullable=True)
    weight = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    products_id = Column(ARRAY(Integer), nullable=False)
    status = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow())


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
