import requests

BASE_URL = 'http://127.0.0.1:5000/api/'  # URL base do servidor Flask

def menu():
    print("Selecione uma opção:")
    print("1. Listar usuários")
    print("2. Criar usuário")
    print("3. Buscar usuário por ID")
    print("4. Atualizar usuário por ID")
    print("5. Deletar usuário por ID")
    print("6. Listar posts")
    print("7. Buscar post por ID")
    print("8. Criar post")
    print("9. Atualizar post por ID")
    print("10. Deletar post por ID")
    print("0. Sair")

def listar_usuarios():
    response = requests.get(BASE_URL + 'users')
    print(response.json())

def criar_usuario():
    name = input("Digite o nome do usuário: ")
    new_user = {'name': name}
    response = requests.post(BASE_URL + 'users', json=new_user)
    print(response.json())

def buscar_usuario_por_id():
    user_id = input("Digite o ID do usuário: ")
    response = requests.get(BASE_URL + f'users/{user_id}')
    print(response.json())

def atualizar_usuario_por_id():
    user_id = input("Digite o ID do usuário: ")
    name = input("Digite o novo nome do usuário: ")
    updated_user = {'name': name}
    response = requests.put(BASE_URL + f'users/{user_id}', json=updated_user)
    print(response.json())

def deletar_usuario_por_id():
    user_id = input("Digite o ID do usuário que deseja deletar: ")
    response = requests.delete(BASE_URL + f'users/{user_id}')
    print(response.json())

def listar_posts():
    response = requests.get(BASE_URL + 'posts')
    print(response.json())

def buscar_post_por_id():
    post_id = input("Digite o ID do post: ")
    response = requests.get(BASE_URL + f'posts/{post_id}')
    print(response.json())

def criar_post():
    author = input("Digite o autor do post: ")
    title = input("Digite o título do post: ")
    content = input("Digite o conteúdo do post: ")
    new_post = {'author': author, 'title': title, 'content': content}
    response = requests.post(BASE_URL + 'posts', json=new_post)
    print(response.json())

def atualizar_post_por_id():
    post_id = input("Digite o ID do post: ")
    title = input("Digite o novo título do post: ")
    content = input("Digite o novo conteúdo do post: ")
    updated_post = {'title': title, 'content': content}
    response = requests.put(BASE_URL + f'posts/{post_id}', json=updated_post)
    print(response.json())

def deletar_post_por_id():
    post_id = input("Digite o ID do post que deseja deletar: ")
    response = requests.delete(BASE_URL + f'posts/{post_id}')
    print(response.json())

if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Digite sua escolha: ")

        if opcao == '1':
            listar_usuarios()
        elif opcao == '2':
            criar_usuario()
        elif opcao == '3':
            buscar_usuario_por_id()
        elif opcao == '4':
            atualizar_usuario_por_id()
        elif opcao == '5':
            deletar_usuario_por_id()
        elif opcao == '6':
            listar_posts()
        elif opcao == '7':
            buscar_post_por_id()
        elif opcao == '8':
            criar_post()
        elif opcao == '9':
            atualizar_post_por_id()
        elif opcao == '10':
            deletar_post_por_id()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
