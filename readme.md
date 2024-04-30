# Desafio Painel SUS

## Descrição do desafio
Imagine que você teve acesso a um banco de dados de atendimentos de saúde exportado de um sistema de terceiros. Sua equipe de Ciência de Dados precisa acessar esses dados de forma sistematizada. Após uma reunião, decidiu-se que a melhor abordagem seria criar uma API REST para fornecer acesso aos dados.

Seu desafio é criar essa API REST usando Python e o framework Flask.

## Instruções de uso


### Download do projeto

Com o **git** ([git instalação](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git)) instalado na máquina, use o terminal do computador e dê o seguinte comando para fazer o download do projeto:

<!--MAIN_BEGIN-->
```bash
git clone https://github.com/jeronimofjr/painel-sus 
```
<!--MAIN_END-->
 É também possível fazer o download do projeto através da interface gráfica do github, aperte em **code** e depois em **Download Zip** (extraia a pasta painel-sus).  

### Mudança para a pasta do projeto

Após ter feito o download do projeto, acesse a pasta do projeto com o seguinte comando:
<!--MAIN_BEGIN-->
```bash
cd painel-sus/
```
<!--MAIN_END-->

### Execução do ambiente

Para a execução do projeto é necessário a instalação do **docker** e **docker-compose**:
* [Docker instalação](https://docs.docker.com/engine/install/)
*  [Docker-compose instalação](https://docs.docker.com/compose/install/)

 caso já estejam instalados, basta adicionar os comandos abaixo:

<!--MAIN_BEGIN-->
```bash
# construção das imagens de cada serviço
docker compose build

# inicialização dos contêineres
docker compose up
```
<!--MAIN_END-->

Após isso,  a **API REST** estará pronta para uso.