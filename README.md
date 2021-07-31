# API REST de Produtos

## Como testar

1. Acesse a [api](https://productsapi-web.herokuapp.com/).

2. Utilize o [Insomnia](https://insomnia.rest/download) ou o [Postman](https://www.postman.com/downloads/) para realizar as requisições HTTP.

3. Para consultar um produto especifico utilize a url `https://productsapi-web.herokuapp.com/product/<id>` com o metodo `GET` do `Insomnia` ou `Postman`.

4. Para adicionar um novo produto, selecione o formato `JSON` no corpo da requisição da ferramenta da sua escolha, informe os dados e modifique o cabeçalho para o método `POST` com a url `https://productsapi-web.herokuapp.com/product/` ou `https://productsapi-web.herokuapp.com/`.

5. Para editar os dados de algum produto, selecione o formato `JSON` no corpo da requisição da ferramenta da sua escolha, descreva as alterações e  `POST` com a url `https://productsapi-web.herokuapp.com/product/` ou `https://productsapi-web.herokuapp.com/`.
 metodo `PUT` com a url `https://productsapi-web.herokuapp.com/product/<id>`.

6. Para deletar um produto selecione o metodo `DELETE` e informe o id do produto a ser deletado na url `https://productsapi-web.herokuapp.com/product/<id>`.

7. Ao acessar a url `https://productsapi-web.herokuapp.com/` serão listados todos os produtos cadastrados.

## Clonando e editando o projeto

1. Faça clone do projeto para a sua máquina.
    ```zsh
    git clone https://github.com/faamaral/products_api.git
    ```

2. Com o python instalado em sua maquina, entre no diretorio do projeto clonado e crie um ambiente virtual para o projeto.
    > no Linux siga esses passos.
    - Instale o virtualenv caso não o tenha instalado.

        ```zsh
        sudo apt install python3-venv
        ```
    - Crie o ambiente virtual.

        ```zsh
        python3 -m venv nome-do-seu-ambiente-virtual
        ```

    - Ative o ambiente virtual.

        ```zsh
        source nome-do-seu-ambiente-virtual/bin/activate
        ```
    > No windows siga esses passos.
    - Instale o virtualenv caso não o tenha instalado.

        ```
        pip install virtualenv
        ```
    - Crie o seu ambiente virtual.
        ```
        virtualenv nome_do_ambiente_virtual
        ```
    - Ative o ambiente virtual.

        ```
        nome_do_ambiente_virtual/Scripts/Activate
        ```
    A visualização no terminal onde você digitou os comandos deverá se parecer com o seguinte.

    ```zsh
    (nome_do_ambiente_virtual) ~/user/user_api(main):
    ``` 

3. Instale as dependencias do projeto.
    > execute o seguinte comando
    ```zsh
    pip install -r requirements.txt
    ```

4. Execute as migrações caso você modifique o arquivo models.py.
    > São necessarias para aplicar as devidas modificações no banco de dados
    ```zsh
    flask db migrate -m "nome da migrate"
   
    flask db upgrade
    ```

6. Execute a aplicação em sua máquina.

    ```zsh
    python3 run.py
    ```

Agora voce pode modificar e testar a aplicação do projeto normalmente.