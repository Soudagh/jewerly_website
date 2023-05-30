from sqlalchemy import Integer, Column, Text, ForeignKey

from src.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(Text, nullable=False)
    brand = Column(Integer, ForeignKey('brands.id'), nullable=False)
    category = Column(Integer, ForeignKey('categories.id'), nullable=False)
    material = Column(Integer, ForeignKey('materials.id'), nullable=False)
    material_color = Column(Integer, ForeignKey('colors.id'), nullable=False)
    cutting = Column(Integer, ForeignKey('cuttings.id'), nullable=True)
    stone = Column(Integer, ForeignKey('stones.id'), nullable=True)
    weaving = Column(Integer, ForeignKey('weavings.id'), nullable=True)
    style = Column(Integer, ForeignKey('styles.id'), nullable=True)
    weight = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)