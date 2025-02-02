import strawberry


@strawberry.input
class PriceFormat:
    display_cents: bool
    currency: str


@strawberry.type
class PriceResult:
    name: str


@strawberry.type
class Product:
    name: str
    base_price: int

    @strawberry.field
    def price(self, format: PriceFormat) -> PriceResult:
        """
        PriceFormat に応じた PriceResult を返します。
        """
        if format.currency.upper() == "USD":
            currency_name = "US Dollar"
        elif format.currency.upper() == "EUR":
            currency_name = "Euro"
        else:
            currency_name = format.currency

        return PriceResult(name=currency_name)
