import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import DBModelBase, Product

@pytest.fixture(scope="module")
def seeded_session():
    engine = create_engine("sqlite:///test.db")
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    yield db
    db.close()


def test_products_were_seeded(seeded_session):
    """Check that the database has 25 products after seeding."""
    count = seeded_session.query(Product).count()
    assert count == 25, f"Expected 25 products, but found {count}"

def test_both_categories_exist(seeded_session):
    """Check that both electronics and grocery products exist in the database."""
    electronics = seeded_session.query(Product).filter_by(category="electronics").count()
    grocery = seeded_session.query(Product).filter_by(category="grocery").count()
    assert electronics == 10, f"Expected 10 electronics, but found {electronics}"
    assert grocery == 15, f"Expected 15 grocery products, but found {grocery}"

def test_all_products_have_barcode_and_price(seeded_session):
    """Check that every product has a non-null barcode and price."""
    missing = seeded_session.query(Product).filter(
        (Product.barcode == None) | (Product.price == None)
    ).count()
    assert missing == 0, f"{missing} products are missing a barcode or price"