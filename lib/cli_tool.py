import argparse
from .models import Task, User 


users = {}


def add_task(args):
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return
    # look up by title
    for t in user.tasks:
        if t.title == args.title:
            t.complete()
            return
    print("❌ Task not found.")

def main():
    parser = argparse.ArgumentParser(
        description="Task Manager CLI (add tasks, complete tasks)"
    )
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()