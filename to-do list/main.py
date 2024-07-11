from to_do_list import ToDoList

def display_menu():
    print("\n--- To-Do List ---")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Limpar todas as tarefas")
    print("5. Sair")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            task = input("Digite a tarefa a ser adicionada: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
            try:
                task_number = int(input("Digite o número da tarefa a ser removida: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            confirm = input("Você tem certeza que deseja apagar todas as tarefas? (s/n): ")
            if confirm.lower() == 's':
                todo_list.clear_tasks()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
