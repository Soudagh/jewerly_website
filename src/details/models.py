from sqlalchemy import Integer, Column, Text

from database import Base


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    brand_name = Column(Text, nullable=False)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    category_name = Column(Text, nullable=False)


class Style(Base):
    __tablename__ = 'styles'

    id = Column(Integer, primary_key=True)
    style_name = Column(Text, nullable=False)


class Color(Base):
    __tablename__ = 'colors'

    id = Column(Integer, primary_key=True)
    color_name = Column(Text, nullable=False)


class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True)
    material_name = Column(Text, nullable=False)


class Stone(Base):
    __tablename__ = 'stones'

    id = Column(Integer, primary_key=True)
    stone_name = Column(Text, nullable=False)


class Cutting(Base):
    __tablename__ = 'cuttings'

    id = Column(Integer, primary_key=True)
    cutting_name = Column(Text, nullable=False)


class Weaving(Base):
    __tablename__ = 'weavings'

    id = Column(Integer, primary_key=True)
    weaving_name = Column(Text, nullable=False)
