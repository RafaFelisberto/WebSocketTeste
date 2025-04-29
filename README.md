# 🧠 Teste de Estágio 

## Instruções
- Realize o git clone deste repositório
- Responda as perguntas no próprio Readme.md
- Suba o código no repositório
- Insira a mensagem retornada do servidor
- Nos envie o link do seu repositório

### Parte 1 – Conceito

Pesquise e explique com suas palavras:

- O que são WebSockets?
R: WebSockets é uma API, que funciona como uma conexão direta entre cliente e browser, através de um protocolo TCP.
- Como funcionam?
R: Conecta um cliente a um servidor de forma bidirecional permanente, assim permitindo que a troca de mensagens seja em tempo real.
- Quando é melhor usar WebSockets em vez de uma API REST tradicional?
R: Quando o que for necessário seja um servidor de baixa latência, no caso em que a resposta tenha que ser em tempo real, no caso do robô de simulação, isto seria extremamente bem vindo.

### Parte 2 – Prática

Você deve criar um pequeno script que se conecta ao **servidor WebSocket** que criamos e descobrir **qual mensagem ele está enviando**.

#### ✅ O que você deve fazer:
1. Criar um pequeno código na linguagem que preferir
2. Estabelecer a conexão com o servidor WebSocket
3. Ler a mensagem recebida
  
URL do servidor: websocket-fh6l.onrender.com

### Parte 3 - 🔎 Desafio teórico: Comunicação em tempo real entre usuários
Você precisa projetar um sistema simples de mensagens em tempo real para usuários logados.

---

#### 🧩 Cenário

O sistema permite que usuários escolham um **nome de usuário** ao entrar.

As mensagens podem ser:

- **Públicas**: todos os usuários conectados recebem.
- **Privadas**: enviadas para um **usuário específico** (por exemplo: `/msg joao oi`).

Outros requisitos:

- Um mesmo usuário pode estar conectado em **vários dispositivos ou abas ao mesmo tempo**.
- Se um usuário **cair e voltar**, ele deve continuar recebendo as mensagens normalmente.

---

#### ❓ Sua tarefa (teórica)

1. Que tipo de tecnologia de comunicação você usaria para esse cenário?
   R: Utilizaria Python, pois é uma linguagem que possui bibliotecas e ferramentas que facilitam a criação deste serviço. Porém também poderia ser possível utilizar ferramentas de JavaScript, para conexão do cliente.
2. Como garantiria o envio correto para:
   - Todos os usuários?
    R: Poderia utilizar um sistema sem a filtragem de nomes, que enviaria uma mensagem para todos os clientes, ou talvez um sistema de BroadCast, que enviaria a todas as conexões.
   - Apenas um usuário específico?
    R: Poderia filtrar um nome específico(ID de usuário) e assim enviaria uma mensagem a cada cliente especificamente.
   - Todas as sessões abertas de um mesmo usuário?
    R: Caso a conexão seja filtrada por usuário, o envio seria para todas as conexões, sem ter uma conexão em específico

3. Existe alguma ferramenta ou biblioteca que facilitaria esse tipo de comunicação?  
   Se sim, **qual?** E **por quê?**
      R: Existem bibliotecas, como a websockets de python que facilita esta comunicação, pois esta, já vem com funções que ajudam a iniciar e criar um websocket. Também há maneiras de utilizar ferramentas como JavaScript para realizar uma dinâmica entre os códigos.
---

#### 🎯 Objetivo

Entender se você consegue identificar os desafios da comunicação em tempo real e pensar em soluções viáveis e escaláveis para eles.


## Boa sorte! 💻
# WebSocketTest-Estagio
