class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, n):
        """Добавление элемента в очередь"""
        new_node = Node(n)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return "ok"

    def pop(self):
        """Удаление элемента из очереди"""
        if self.head is None:
            return "error"
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return data

    def front(self):
        """Просмотр первого элемента без удаления"""
        if self.head is None:
            return "error"
        return self.head.data

    def size(self):
        """Получение текущего размера очереди"""
        return self.length

    def clear(self):
        """Очистка очереди"""
        self.head = None
        self.tail = None
        self.length = 0
        return "ok"


if __name__ == "__main__":
    queue = Queue()
    print(
        "Добро пожаловать в программу очередь! Доступные команды:\n"
        "push <число> - Добавить число в очередь\n"
        "pop - Удалить первый элемент\n"
        "front - Показать первый элемент\n"
        "size - Показать размер очереди\n"
        "clear - Очистить очередь\n"
        "exit - Выйти из программы\n"
        "Введите команду полностью (например: 'push 1')"
    )
    while True:
        try:
            user_input = input("Введите команду: ").strip()
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0]

            if command == "exit":
                print("bye")
                break
            elif command == "push":
                if len(parts) < 2:
                    print("Ошибка: после 'push' укажите число")
                else:
                    try:
                        num = int(parts[1])
                        print(queue.push(num))
                    except ValueError:
                        print("Ошибка: необходимо ввести целое число")
            elif command == "pop":
                print(queue.pop())
            elif command == "front":
                print(queue.front())
            elif command == "size":
                print(queue.size())
            elif command == "clear":
                print(queue.clear())
            else:
                print(f"Неизвестная команда: {command}")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            continue