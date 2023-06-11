import click

from database.database import Database

from devices.device_repository import DeviceRepository
from devices.devices import Device

from users.user_repository import UserRepository
from users.users import User

state = {}


def show_menu():
    click.echo("==== Menu ====")
    click.echo("1. Criar dispositivo")
    click.echo("2. Listar dispositivos")
    click.echo("3. Atualizar dispositivo")
    click.echo("4. Deletar dispositivo")
    click.echo("5. Buscar dispositivo por nome")
    click.echo("6. Ligar dispositivo")
    click.echo("7. Desligar dispositivo")
    click.echo("0. Sair")


def login_or_register():
    click.echo("==== Login ou Registro ====")
    click.echo("1. Fazer login")
    click.echo("2. Registrar novo usuário")

    option = click.prompt("Digite a opção desejada", type=int)

    if option == 1:
        login()
    elif option == 2:
        register()
    else:
        click.echo("Opção inválida. Tente novamente.")
        login_or_register()


def login():
    email = click.prompt("Digite seu email")
    user_repo = state['user_repo']
    user = user_repo.get_user_by_email(email)

    if user:
        state['user'] = user.email
        state['user_id'] = user._id
        click.echo("Login realizado com sucesso.")
    else:
        click.echo("Email não encontrado. Tente novamente.")


def register():
    email = click.prompt("Digite seu email")
    name = click.prompt("Digite seu nome")

    user_repo = state['user_repo']
    user = user_repo.get_user_by_email(email)

    if user:
        click.echo("Usuário já existe. Faça login com o email informado.")
        return

    user = User(email=email, name=name)
    user_repo.create_user(user)
    click.echo("Usuário registrado com sucesso.")


def create_device():
    if 'user' not in state:
        click.echo("Nenhum usuário logado.")
        return

    email = state['user']
    user_repo = state['user_repo']
    devices = user_repo.fetch_user_devices(email)

    click.echo("#" * 10)
    click.echo("Dispositivos existentes:")
    for device in devices:
        click.echo(f"Nome: {device.name}, Status: {device.status}, Temperatura: {device.temperature}")
    click.echo("#" * 10)

    name = click.prompt("Digite o nome do dispositivo")
    status = click.confirm("O dispositivo está ligado?")
    temperature = click.prompt("Digite a temperatura do dispositivo", type=float)

    device = Device(user_id=state["user_id"], name=name, status=status, temperature=temperature)
    device_repo = state['device_repo']
    device_repo.create_device(device)
    click.echo("Dispositivo criado com sucesso!")


def list_devices():
    if 'user' not in state:
        click.echo("Nenhum usuário logado.")
        return

    email = state['user']
    user_repo = state['user_repo']
    devices = user_repo.fetch_user_devices(email)

    click.echo("Dispositivos do usuário:")
    for device in devices:
        click.echo(f"Nome: {device.name}, Status: {device.status}, Temperatura: {device.temperature}")


def update_device():
    if 'user' not in state:
        click.echo("Nenhum usuário logado.")
        return

    email = state['user']
    user_repo = state['user_repo']
    devices = user_repo.fetch_user_devices(email)

    click.echo("#" * 10)
    click.echo("Dispositivos existentes:")
    for device in devices:
        click.echo(f"Nome: {device.name}, Status: {device.status}, Temperatura: {device.temperature}")
    click.echo("#" * 10)

    device_name = click.prompt("Digite o nome do dispositivo que deseja atualizar")

    for device in devices:
        if device.name == device_name:
            new_name = click.prompt("Digite o novo nome do dispositivo", default=device.name)
            new_status = click.confirm("O dispositivo está ligado?", default=device.status)
            new_temperature = click.prompt("Digite a nova temperatura do dispositivo", type=float, default=device.temperature)

            updated_device = Device(user_id=state['user_id'], name=new_name, status=new_status, temperature=new_temperature)
            device_repo = state['device_repo']
            device_repo.update_device(device._id, updated_device)
            click.echo("Dispositivo atualizado com sucesso!")
            return

    click.echo("Dispositivo não encontrado.")


def delete_device():
    if 'user' not in state:
        click.echo("Nenhum usuário logado.")
        return

    email = state['user']
    user_repo = state['user_repo']
    devices = user_repo.fetch_user_devices(email)

    click.echo("#" * 10)
    click.echo("Dispositivos existentes:")
    for device in devices:
        click.echo(f"Nome: {device.name}, Status: {device.status}, Temperatura: {device.temperature}")
    click.echo("#" * 10)

    device_name = click.prompt("Digite o nome do dispositivo que deseja deletar")

    for device in devices:
        if device.name == device_name:
            device_repo = state['device_repo']
            device_repo.delete_device(device._id)
            click.echo("Dispositivo deletado com sucesso!")
            return

    click.echo("Dispositivo não encontrado.")


def search_device_by_name():
    if 'user' not in state:
        click.echo("Nenhum usuário logado.")
        return

    device_name = click.prompt("Digite o nome do dispositivo que deseja buscar")

    device_repo = state['device_repo']
    devices = device_repo.get_device_by_name(device_name)

    if devices:
        click.echo("Dispositivo encontrado:")
        for device in devices:
            click.echo(f"Nome: {device.name}, Status: {device.status}, Temperatura: {device.temperature}")
    else:
        click.echo("Dispositivo não encontrado.")


def turn_on_device():
    if 'user' not in state:
        click.echo("Nenhum usuário logado.")
        return

    email = state['user']
    user_repo = state['user_repo']
    devices = user_repo.fetch_user_devices(email)

    click.echo("#" * 10)
    click.echo("Dispositivos existentes:")
    for device in devices:
        click.echo(f"Nome: {device.name}, Status: {device.status}, Temperatura: {device.temperature}")
    click.echo("#" * 10)

    device_name = click.prompt("Digite o nome do dispositivo que deseja ligar")

    for device in devices:
        if device.name == device_name:
            device_repo = state['device_repo']
            device_repo.update_device(name=device.name, user_id=device.user_id, status=True, temperature=None)
            click.echo("Dispositivo ligado com sucesso!")
            return

    click.echo("Dispositivo não encontrado.")


def turn_off_device():
    if 'user' not in state:
        click.echo("Nenhum usuário logado.")
        return

    email = state['user']
    user_repo = state['user_repo']
    devices = user_repo.fetch_user_devices(email)

    click.echo("#" * 10)
    click.echo("Dispositivos existentes:")
    for device in devices:
        click.echo(f"Nome: {device.name}, Status: {device.status}, Temperatura: {device.temperature}")
    click.echo("#" * 10)

    device_name = click.prompt("Digite o nome do dispositivo que deseja desligar")

    for device in devices:
        if device.name == device_name:
            device_repo = state['device_repo']
            device_repo.update_device(name=device.name, user_id=device.user_id, status=False, temperature=None)
            click.echo("Dispositivo desligado com sucesso!")
            return

    click.echo("Dispositivo não encontrado.")


def main():
    database = Database()
    state['database']: Database = database
    user_repo = UserRepository(database)
    state['user_repo']: UserRepository = user_repo
    device_repo = DeviceRepository(database)
    state['device_repo']: DeviceRepository = device_repo

    running = True

    while running:
        login_or_register()

        if 'user' not in state:
            click.echo("Usuário não logado.")
            continue

        while True:
            show_menu()
            option = click.prompt("Digite a opção desejada", type=int)

            if option == 1:
                create_device()
            elif option == 2:
                list_devices()
            elif option == 3:
                update_device()
            elif option == 4:
                delete_device()
            elif option == 5:
                search_device_by_name()
            elif option == 6:
                turn_on_device()
            elif option == 7:
                turn_off_device()
            elif option == 0:
                running = False
                break
            else:
                click.echo("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
