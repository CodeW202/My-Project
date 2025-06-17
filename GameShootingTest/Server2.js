// Express server to serve MainChacter.json and static files
const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3411;

// Allow CORS for p5.js sketches
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  next();
});

// Serve static files from 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// Route to serve the JSON file
app.get('/MainChacter', (req, res) => {
  const filePath = path.join(__dirname, 'MainChacter.json');
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      res.status(500).send({ error: 'Failed to load character data' });
    } else {
      res.json(JSON.parse(data));
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
