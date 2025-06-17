// Express server to serve MainChacter.json and static files
const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3411;

// Allow CORS for p5.js sketches
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

// Middleware to parse JSON bodies
app.use(express.json());

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

// Route to update the score
app.post('/updateScore', (req, res) => {
  const filePath = path.join(__dirname, 'MainChacter.json');
  const increaseBy = req.body.increaseBy || 1;

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send({ error: 'Failed to read character data' });
    }

    let character;
    try {
      character = JSON.parse(data);
    } catch (parseErr) {
      return res.status(500).send({ error: 'Invalid JSON format' });
    }

    character.score = (character.score || 0) + increaseBy;

    fs.writeFile(filePath, JSON.stringify(character, null, 2), 'utf8', (writeErr) => {
      if (writeErr) {
        return res.status(500).send({ error: 'Failed to update character score' });
      }
      res.send({ success: true, newScore: character.score });
    });
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
