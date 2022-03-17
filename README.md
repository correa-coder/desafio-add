# Descrição

Esta aplicação permite cadastrar e carregar alunos em um banco de dados relacional utilizando a linguagem _Java_ e o framework **Spring Boot**.

# Uso
Rode a aplicação `DemoApplication.java` para iniciar um servidor local no endereço `localhost:8080`

> OBS: Esta aplicação está localizada em `src/main/java/com/example/demo`

Depois execute o script _Python_ `api_client.py` que pode ser encontrado na pasta `scripts`.

![Ui Screenshot](/scripts/ui_screenshot.png)

> OBS: Na interface gráfica a data de nascimento deve ser inserida no formato `ano-mês-dia`, por exemplo: 2022-03-16 (16/03/2022)


Para o funcionamento desse script é necessário ter instalado o **Python 3.7** (ou superior) e o módulo `requests`.


> A dependência `requests` pode ser instalada com o pip
```cmd
pip install requests
```

# Documentação
Uma breve descrição das _endpoints_ da API pode ser encontrada no diretório `docs/API endpoints.html` ou online neste link ....