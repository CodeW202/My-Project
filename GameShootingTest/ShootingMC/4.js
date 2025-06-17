var MainChacter = {
    "ID": "12fews",  
    "Name": "Winsteen",
    "WeaponName": "Sword",
    "XPos": 20,
    "YPos": 50,
    "XSize": 20,
    "YSize": 50,
    "Speed": 5
};

var Enemy = {
    "ID": "21w",  
    "Name": "Yama",
    "WeaponName": "Shield",
    "XPos": 300,
    "YPos": 50,
    "XSize": 20,
    "YSize": 50,
    "Speed": 2,
    "Direction": 1
};

let bullets = [];

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  
  // Draw the character as a rectangle
  fill(100, 150, 255); // Fill color for character
  rect(MainChacter.XPos, MainChacter.YPos, MainChacter.XSize, MainChacter.YSize);

  // Draw weapon as a smaller rectangle attached to character
  fill(200, 100, 100); // Fill color for weapon
  rect(MainChacter.XPos + MainChacter.XSize, MainChacter.YPos + 10, 10, 30);

  // Display character name
  fill(0);
  textSize(12);
  text("Name: " + MainChacter.Name, 10, height - 40);
  text("Weapon: " + MainChacter.WeaponName, 10, height - 25);
  text("ID: " + MainChacter.ID, 10, height - 10);

  // Move enemy up and down
  Enemy.YPos += Enemy.Speed * Enemy.Direction;
  if (Enemy.YPos <= 0 || Enemy.YPos + Enemy.YSize >= height) {
    Enemy.Direction *= -1;
  }

  // Draw the enemy
  fill(255, 100, 100); // Fill color for enemy
  rect(Enemy.XPos, Enemy.YPos, Enemy.XSize, Enemy.YSize);

  // Draw enemy weapon
  fill(100, 100, 200);
  rect(Enemy.XPos - 10, Enemy.YPos + 10, 10, 30);

  // Display enemy name
  fill(0);
  textSize(12);
  text("Enemy: " + Enemy.Name, width - 100, height - 40);
  text("Weapon: " + Enemy.WeaponName, width - 100, height - 25);
  text("ID: " + Enemy.ID, width - 100, height - 10);

  // Update and draw bullets
  for (let i = bullets.length - 1; i >= 0; i--) {
    bullets[i].x += bullets[i].speed;
    fill(0);
    rect(bullets[i].x, bullets[i].y, 10, 5);

    // Remove bullets that are offscreen
    if (bullets[i].x > width) {
      bullets.splice(i, 1);
    }
  }
}

function keyPressed() {
  if (keyCode === LEFT_ARROW) {
    MainChacter.XPos -= MainChacter.Speed;
  } else if (keyCode === RIGHT_ARROW) {
    MainChacter.XPos += MainChacter.Speed;
  } else if (keyCode === UP_ARROW) {
    MainChacter.YPos -= MainChacter.Speed;
  } else if (keyCode === DOWN_ARROW) {
    MainChacter.YPos += MainChacter.Speed;
  } else if (key === ' ') {
    // Fire bullet
    bullets.push({
      x: MainChacter.XPos + MainChacter.XSize,
      y: MainChacter.YPos + MainChacter.YSize / 2 - 2.5,
      speed: 7
    });
  }
}
