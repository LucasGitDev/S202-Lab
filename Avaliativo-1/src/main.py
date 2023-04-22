from zoologico_cli import ZoologicoCLI
from zoologico_dao import ZoologicoDAO
from database import Database


def main():
    database = Database("zoologico")
    zoologico_dao = ZoologicoDAO(database)
    zoologico_cli = ZoologicoCLI(zoologico_dao)
    zoologico_cli.menu()


if __name__ == "__main__":
    main()
