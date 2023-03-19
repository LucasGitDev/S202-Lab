from database import Database
from utils import writeAJson

db = Database(database="dex", collection="pokemons")
# db.resetDatabase()


def getPokemonByDex(number: int):
    return db.collection.find({"id": number})


def getStrongestPokemon():
    return db.collection.find().sort("base.Attack", -1).limit(1)


def getDefensivePokemon():
    return db.collection.find().sort("base.Defense", -1).limit(1)


def getSpecialAttackPokemon():
    return db.collection.find().sort("base.Sp. Attack", -1).limit(1)


def getSpecialDefensePokemon():
    return db.collection.find().sort("base.Sp. Defense", -1).limit(1)


def getSpeedPokemon():
    return db.collection.find().sort("base.Speed", -1).limit(1)


def getBaseGTE(value: int, base: str):
    return db.collection.find({f"base.{base}": {"$gte": value}})


def getBaseLTE(value: int, base):
    return db.collection.find({f"base.{base}": {"$lte": value}})


def getByEnglishName(name: str):
    return db.collection.find({"name.english": name})


def getByType(type: str):
    return db.collection.find({"type": {"$all": [type]}})


def firstOption():
    pokemonType = input("Digite o tipo do pokemon: ")
    pokemons = getByType(pokemonType)
    writeAJson(pokemons, f"pokemonsDoTipo {pokemonType}")
    for pokemon in pokemons:
        print(f"{pokemon['name']['english']} - {pokemon['type']}")


def secondOption():
    pokemonName = input("Digite o nome do pokemon: ")
    pokemon = getByEnglishName(pokemonName)
    writeAJson(pokemon, f"pokemon {pokemonName}")
    for p in pokemon:
        print(f"{p['name']['english']} - {p['type']}")


def thirdOption():
    value = int(input("Digite o valor da base: "))
    base = input("Digite a base: ")
    pokemons = getBaseGTE(value, base)
    writeAJson(pokemons, f"pokemonsComBase {base} - MaiorOuIgualA {value}")
    for pokemon in pokemons:
        print(f"{pokemon['name']['english']} - {pokemon['type']}")


def fourthOption():
    pokemon = getSpeedPokemon()
    writeAJson(pokemon, f"pokemonComMaiorVelocidade")
    for p in pokemon:
        print(f"{p['name']['english']} - {p['type']}")


def fifthOption():
    print("1 - Ataque")
    print("2 - Defesa")
    print("3 - Ataque Especial")
    print("4 - Defesa Especial")
    print("5 - Velocidade")
    op = int(input("Digite a opção desejada: "))
    if op == 1:
        pokemon = getStrongestPokemon()
    elif op == 2:
        pokemon = getDefensivePokemon()
    elif op == 3:
        pokemon = getSpecialAttackPokemon()
    elif op == 4:
        pokemon = getSpecialDefensePokemon()
    elif op == 5:
        pokemon = getSpeedPokemon()
    
    writeAJson(pokemon, f"pokemonComMaiorBase {op}")
    for p in pokemon:
        print(f"{p['name']['english']} - {p['type']}")


def main():

    op = 1
    while op != 0:
        print("1 - Buscar pokemon por tipo")
        print("2 - Buscar pokemon por nome em inglês")
        print("3 - Buscar pokemon com base X maior ou igual a um valor")
        print("4 - Buscar pokemon com maior velocidade")
        print("5 - Buscar pokemon com maior ataque, defesa, ataque especial, defesa especial ou velocidade")
        print("0 - Sair")
        op = int(input("Digite a opção desejada: "))

        if op == 1:
            firstOption()
        elif op == 2:
            secondOption()
        elif op == 3:
            thirdOption()
        elif op == 4:
            fourthOption()
        elif op == 5:
            fifthOption()
            
        print("*" * 20)
        print()


if __name__ == "__main__":
    main()
