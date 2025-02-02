import strawberry

from app.graphql.types.product import Product


@strawberry.type
class ProductQuery:
    @strawberry.field
    def product(self, id: strawberry.ID) -> Product:
        return Product(
            name="Sample Product",
            base_price=1000,  # 10.00ドル相当
        )
