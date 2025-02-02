import strawberry

from .product import Product


@strawberry.type
class Location:
    address: str | None


@strawberry.type
class Shop:
    name: str
    location: Location | None
    products: list[Product]
