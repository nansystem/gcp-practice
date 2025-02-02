from datetime import datetime

import strawberry


@strawberry.type
class User:
    id: int
    name: str
    email: str
    created_at: datetime
