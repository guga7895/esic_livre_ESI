# EsicLivre

Micro serviço para interação com o eSIC municipal de São Paulo.


## Install


### Virtual Environment

Recomendamos usar alguma ferramenta para isolar o ambiente do projeto uma vez que este usa bibliotecas com versões ultrapassadas para seu funcionamento, a ferramenta que usamos é o virtual env. Para saber mais como o virtual env funciona acesse [este link](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/), aqui daremos um breve explicação de como utilizá-lo para este projeto.


#### Instalando virtual environment

```
$ pip install virtualenv
```


#### Criando um ambiente isolado

Para criar um ambiente isolado execute o comando `virtualenv meu_ambiente` de dentro da pasta do projeto, como convenção utilize o nome `env`:

```
$ virtualenv env
```

Isso criará uma pasta com o nome passado no argumento (no exemplo teremos a pasta `env`) com uma versão separada, daquela instalada no seu sistema, do python e do pip, e é dentro desse ambiente que instalaremos as bibliotecas nescessárias.

Para começar a usar o ambiente criado execute o comando:

```
$ source env/bin/activate
```

Uma vez dentro do ambiente virtual criado, pode prosseguir com a intalação, **sempre com o ambiente ativo!**.


### Instalando as dependencias do projeto

Para instalar as dependencias do projeto execute o comando:

```
$ python setup.py develop
```

Caso o pip falhar ao instalar alguma biblioteca, force a instalação dela em seperado, na versão indicada pelo arquivo *setup.py*, por exemplo:

```
$ pip install six==1.7.3
```


### Configurações locais

Para configurar o projeto faça uma cópia do arquivo *settings/local_settings.example.py* renomeando-o para *settings/local_settings.py*, e modifique a cópia como indicado no própio arquivo.

Vale resaltar que o projeto depende da utilização do firefox na **versão 44.0**, que está disponivel [neste link](https://ftp.mozilla.org/pub/firefox/releases/44.0/).

Também é nescessário a chave ssh pública da máquina, geralmente encontrada no arquivo: */home/usuario/.ssh/id_rsa.pub*. Se ainda não tem uma chave pública ou quer saber mais a respeito acesse [este link](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2).

Para criar a chave nescessária para este projeto execute o comando e siga as instruções:

```
$ ssh-keygen -t rsa
```

Assim que possuir uma chave pública, copiea para o arquivo dentro do projeto em: */settings/keypub*


## Prepare DB

O projeto atualmente usa o banco de Dados [Postgres](https://www.postgresql.org), embora não seja obrigatório. Daremos as instruções nescessárias para preparar um similar ao usado em produção atual.


### Instalação do postgresql

Recomendamos [este guia](https://www.digitalocean.com/community/tutorials/como-instalar-e-utilizar-o-postgresql-no-ubuntu-16-04-pt) de como instalar o postgresql para o ubuntu.


### Criando um usuário e o banco de dados

Para criar o usuário do banco de dados execute o comando de dentro do console do postgresql:

```
postgres=# CREATE USER <usuario> WITH PASSWORD '<senha>';
```

Para criar o banco de dados execute o comando de dentro do console do postgresql:

```
postgres=# CREATE DATABASE <base> OWNER <usuario>;
```


## Criando as tabelas

Se não configurou ainda, coloque o nome do usuario e a URL de acesso ao banco no campo `SQLALCHEMY_DATABASE_URI` do arquivo *settings/local_settings.py*, como no exemplo:

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@localhost/{database}'
```

Para criar as tabelas execute o script:

```
$ python manage.py initdb
```


## Run!

```
$ python manage.py run
```


## API

Needs doc...
