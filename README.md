# Podcast Web Project

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4556a7f57ffe4fc9812d07c9fd08483b)](https://www.codacy.com/app/ezequielramos/djangoPodcastWebProject?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ezequielramos/djangoPodcastWebProject&amp;utm_campaign=Badge_Grade)

Aplicação WEB de um sistema de compartilhamento de arquivos de podcast (áudio) voltados ao meio acadêmico. 

## Objetivo

Criar um sistema de compartilhamento de podcast numa plataforma online voltada ao meio acadêmico, onde o conteúdo poderá ser publicado pelos professores e disponibilizado aos alunos; Permitir a avaliação dos áudios publicados e uma área voltada aos comentários dos alunos, bem como um ranking dos podcast melhores avaliados; Permitir classificar os podcasts por categorias.

## Ferramentas utilizadas no desenvolvimento

A aplicação é desenvolvida utilizando o conceito de web-service, a aplicação será dividida em duas partes isoladas que podem ser executadas separadamente. Uma irá conter toda parte de front-end, que será construído em HTML, CSS, Javascript com framework Bootstrap e AngularJS utilizando do conceito de design responsivo. A outra conterá o servidor de aplicação web que será construído em Python utilizando o framework Django, o banco de dados utilizado será o SQLite.

## Requisitos funcionais

- Cadastro de usuário
- Upload de Podcasts
- Incluir Comentários
- Download do Podcast
- Pesquisa de Podcast
- Ouvir Podcast
- Visualizar informações do Podcast

## Requerimentos

- Python3.5+ instalado
- Django instalado
- Executar no prompt de comando:
```
$ python3 manage.py migrate
$ python3 manage.py runserver
```

## Créditos

- Music: https://www.bensound.com