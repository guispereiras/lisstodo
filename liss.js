// Importa o módulo http do Node.js
const http = require('http');

// Configura as informações do servidor
const hostname = '127.0.0.1';
const port = 3000;

// Cria um servidor HTTP
const server = http.createServer((req, res) => {
  // Configura o cabeçalho da resposta com o tipo de conteúdo
  res.setHeader('Content-Type', 'text/plain');
  
  // Envia a resposta "Olá, Mundo!"
  res.end('Olá, Mundo!\n');
});

// Inicia o servidor para escutar as requisições
server.listen(port, hostname, () => {
  console.log(`Servidor rodando em http://${hostname}:${port}/`);
});
