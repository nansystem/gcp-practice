import strawberry

from .resolvers.product import ProductQuery
from .resolvers.shop import ShopQuery
from .resolvers.user import UserMutation, UserQuery


@strawberry.type
class Query(UserQuery, ShopQuery, ProductQuery):
    pass


@strawberry.type
class Mutation(UserMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
