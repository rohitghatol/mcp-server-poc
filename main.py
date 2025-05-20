import os


def list_dir(path: str = '.'):
    for entry in os.listdir(path):
        print(entry)


def make_dir(path: str):
    os.makedirs(path, exist_ok=True)
    print(f"Created directory {path}")


def remove_dir(path: str):
    try:
        os.rmdir(path)
        print(f"Removed directory {path}")
    except OSError as e:
        print(f"Error removing {path}: {e}")


def create_file(path: str):
    with open(path, 'w'):
        pass
    print(f"Created file {path}")


def delete_file(path: str):
    try:
        os.remove(path)
        print(f"Deleted file {path}")
    except OSError as e:
        print(f"Error deleting {path}: {e}")


def handle_command(cmd: str) -> bool:
    parts = cmd.strip().split()
    if not parts:
        return True
    command, *args = parts

    if command == 'exit':
        return False
    if command == 'ls':
        list_dir(args[0] if args else '.')
    elif command == 'mkdir' and args:
        make_dir(args[0])
    elif command == 'rmdir' and args:
        remove_dir(args[0])
    elif command == 'create' and args:
        create_file(args[0])
    elif command == 'delete' and args:
        delete_file(args[0])
    else:
        print('Unknown command')
    return True


def main() -> None:
    print('MCP File System Server')
    print("Type 'exit' to quit.")
    while True:
        try:
            cmd = input('> ')
        except EOFError:
            break
        if not handle_command(cmd):
            break


if __name__ == '__main__':
    main()
