from database import Database
from product_analyzer import ProductAnalyzer
from utils import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

pa = ProductAnalyzer(db.collection)

writeAJson(pa.totalFromB(), 'Total de gastos do cliente B')
writeAJson(pa.leastSoldProduct(), 'Produto menos vendido')
writeAJson(pa.lessSpender(), 'Cliente que menos gastou')
writeAJson(pa.productsSoldWithTwoOrMoreUnits(),
           'Produtos vendidos com mais de 2 unidades')
