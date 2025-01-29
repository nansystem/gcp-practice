import strawberry

from app.graphql.schema import schema

sdl = strawberry.printer.print_schema(schema)

with open("schema.graphql", "w") as f:
    f.write(sdl)
