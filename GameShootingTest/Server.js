// Step-by-step: Basic Node.js Server to load MainChacter.json

// 1. Make sure you have Node.js installed: https://nodejs.org
// 2. Create your project folder and place MainChacter.json inside it
// 3. Create this file as server.js and run with: node server.js

const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3411;

const server = http.createServer((req, res) => {
  if (req.url === '/MainChacter') {
    fs.readFile(path.join(__dirname, 'MainChacter.json'), 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500);
        res.end('Error loading character');
        return;
      }
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(data);
    });
  } else {
    // Serve static files (index.html, sketch.js)
    let file = req.url === '/' ? '/index.html' : req.url;
    let filePath = path.join(__dirname, file);
    let ext = path.extname(filePath);
    let contentType = {
      '.html': 'text/html',
      '.js': 'application/javascript',
    }[ext] || 'text/plain';

    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(data);
    });
  }
});

server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
