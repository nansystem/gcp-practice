import strawberry

from ..types.shop import Location, Product, Shop

SHOPS: dict[str, Shop] = {
    "1": Shop(
        name="My Shop",
        location=Location(address="123 Main St"),
        products=[
            Product(name="Gelato", base_price=450),
            Product(name="Pudding", base_price=300),
        ],
    ),
    "2": Shop(
        name="My Shop 2",
        location=Location(address="456 Main St"),
        products=[
            Product(name="Ice Cream", base_price=500),
            Product(name="Cake", base_price=400),
        ],
    ),
}


@strawberry.type
class ShopQuery:
    @strawberry.field
    def shop(self, id: strawberry.ID) -> Shop:
        if id not in SHOPS:
            raise ValueError(f"Shop with id {id} not found")
        return SHOPS[id]
