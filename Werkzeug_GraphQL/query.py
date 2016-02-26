import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()
    ping = graphene.String(to=graphene.String())
    restaurant = graphene.String(name=graphene.String(), id=graphene.String())

    def resolve_hello(self, args, info):
        return {"max": "Welt", "kai": "World"}

    def resolve_ping(self, args, info):
        return 'Pinging {}'.format(args.get('to'))

    def resolve_restaurant(self, args, info):
        return {'id': args.get('id'), 'name': args.get('name')}

schema = graphene.Schema(query=Query)
