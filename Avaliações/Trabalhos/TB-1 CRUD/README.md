Este diretório contém o código fonte e todas as estruturas necessárias para a realização de um CRUD utilizando o framework Flask em Python.


# O que é um CRUD?
Um CRUD é um acrônimo para as operações básicas de manipulação de dados que consistem em:

### **C**reate
-> É a funcionalidade de inserir dados novos ao sistema implementado certificando-se que cumpra com os requisitos e seja devidamento armazenado.
Na web é normalmente associado ao método HTTP POST:
> request HTTP [POST]
### **R**ead  
-> É a funcionalidade que permite ter acesso aos dados para leitura, sendo incapaz de altera-los por si só, assim apenas retornando os dados que foram requiridos que existem no sistema.
Na web é normalmente associado ao método HTTP GET:
> request HTTP [GET]
### **U**pdate
-> É a funcionalidade de acessar um dado existente no sistema e alterar o seu valor, garantindo que a modificação seja efetuada corretamente. 
É possível fazer um Update de diversas formas, apesar de o seu método HTTTP associado ser o PUT, é possível implementar utilizando dos métodos GET e POST
> request HTTP [PUT]
### **D**elete
-> É a funcionalidade de acessar dados existentes no sistemas e solicitar a exclusão, para que sejam removidos do sistema.
Seu método HTTP é o DELETE
> request HTTP [DELETE]

# REQUISITOS do SISTEMA
* Um sistema Web que contemple um CRUD de pelo menos duas tabelas com dependência de 1-N ou de N-N;

* O sistema deve conter cadastro de usuário e senha e deve ter acesso restrito a usuário logado;

* O sistema deve gerenciar a sessão do usuário através de cookies;

*O sistema deve apresentar um front-end mínimo, sendo o foco o back end.

* O sistema pode ser feito em qualquer linguagem/framework, tendo como sugestão Python/Flask;

* Pode ser usado qualquer SGBD relacional, tendo como sugestão PostgreSQL



