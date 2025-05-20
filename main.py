import os
import shlex


def list_dir(path="."):
    try:
        for entry in os.listdir(path):
            print(entry)
    except Exception as e:
        print(f"error: {e}")


def make_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"created {path}")
    except Exception as e:
        print(f"error: {e}")


def remove_dir(path):
    try:
        os.rmdir(path)
        print(f"deleted {path}")
    except Exception as e:
        print(f"error: {e}")


def create_file(path):
    try:
        open(path, "a").close()
        print(f"created {path}")
    except Exception as e:
        print(f"error: {e}")


def remove_file(path):
    try:
        os.remove(path)
        print(f"deleted {path}")
    except Exception as e:
        print(f"error: {e}")


def help_text():
    print(
        "Commands:\n"
        "  ls [path]        - list directory contents\n"
        "  mkdir <path>     - create directory\n"
        "  rmdir <path>     - remove directory\n"
        "  touch <path>     - create empty file\n"
        "  rm <path>        - delete file\n"
        "  help             - show this message\n"
        "  exit             - quit"
    )


def dispatch(cmd, args):
    if cmd == "ls":
        path = args[0] if args else "."
        list_dir(path)
    elif cmd == "mkdir":
        if not args:
            print("error: missing path")
        else:
            make_dir(args[0])
    elif cmd == "rmdir":
        if not args:
            print("error: missing path")
        else:
            remove_dir(args[0])
    elif cmd == "touch":
        if not args:
            print("error: missing path")
        else:
            create_file(args[0])
    elif cmd == "rm":
        if not args:
            print("error: missing path")
        else:
            remove_file(args[0])
    elif cmd == "help":
        help_text()
    else:
        print(f"unknown command: {cmd}")


def main():
    print("MCP File System Server. Type 'help' for commands, 'exit' to quit.")
    while True:
        try:
            line = input("mcp> ")
        except EOFError:
            break
        if not line:
            continue
        parts = shlex.split(line)
        cmd = parts[0]
        if cmd == "exit":
            break
        dispatch(cmd, parts[1:])
    print("bye")


if __name__ == "__main__":
    main()
