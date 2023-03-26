

class ProductAnalyzer:
    def __init__(self, collection):
        self.collection = collection

    def totalFromB(self):
        result = self.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"cliente_id": "B"}},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": 2, "total": {"$avg": "$total"}}}
        ])
        return result

    def leastSoldProduct(self):
        result = self.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {
                "$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
        ])
        return result

    def lessSpender(self):
        result = self.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"},
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": 1}},
            {"$group": {"_id": "$'_id.data'", "cliente": {"$first": "$_id.cliente"},
                        "total": {"$first": "$total"}}}
        ])
        return result

    def productsSoldWithTwoOrMoreUnits(self):
        result = self.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 2}}},
            {"$group": {"_id": "$produtos.nome", "total": {
                "$sum": "$produtos.quantidade"}}}
        ])
        return result
