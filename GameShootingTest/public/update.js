function updateScore() {
    fetch('http://localhost:3411/updateScore', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ increaseBy: 1 })
    })
    .then(response => response.json())
    .then(data => console.log('Score updated:', data))
    .catch(error => console.error('Error updating score:', error));
  }

  //for sketch.js
  //      updateScore();  // <-- Call backend here too