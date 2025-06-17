var MainChacter = {
    "ID": "12fews",  
    "Name": "Winsteen",
    "WeaponName": "Sword",
    "XPos": 20,
    "YPos": 50,
    "XSize": 20,
    "YSize": 50,
    "Speed": 5,
    "WeaponSizeX": 10,
    "WeaponSizeY": 30
};

var MainCharacterBullet = {
  bullets: [],
  speed: 7,
  width: 10,
  height: 5
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
    "Direction": 1,
    "visible": true,
    "hideTimer": 0,
    "WeaponSizeX": 10,
    "WeaponSizeY": 30
};

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  // Update and draw bullets
  for (let i = MainCharacterBullet.bullets.length - 1; i >= 0; i--) {
    let b = MainCharacterBullet.bullets[i];
    b.x += MainCharacterBullet.speed;
    fill(0);
    rect(b.x, b.y, MainCharacterBullet.width, MainCharacterBullet.height);

    // Check for collision with enemy
    if (Enemy.visible &&
        b.x < Enemy.XPos + Enemy.XSize &&
        b.x + MainCharacterBullet.width > Enemy.XPos &&
        b.y < Enemy.YPos + Enemy.YSize &&
        b.y + MainCharacterBullet.height > Enemy.YPos) {
      Enemy.visible = false;
      Enemy.hideTimer = millis();
      MainCharacterBullet.bullets.splice(i, 1);
      continue;
    }

    // Remove bullets that are offscreen
    if (b.x > width) {
      MainCharacterBullet.bullets.splice(i, 1);
    }
  }

  // Draw the character as a rectangle
  fill(100, 150, 255); // Fill color for character
  rect(MainChacter.XPos, MainChacter.YPos, MainChacter.XSize, MainChacter.YSize);

  // Draw weapon as a smaller rectangle attached to character
  fill(200, 100, 100);
  rect(MainChacter.XPos + MainChacter.XSize + 10, MainChacter.YPos + 10, MainChacter.WeaponSizeX, MainChacter.WeaponSizeY);

  // Display character name
  fill(0);
  textSize(12);
  text("Name: " + MainChacter.Name, 10, height - 40);
  text("Weapon: " + MainChacter.WeaponName, 10, height - 25);
  text("ID: " + MainChacter.ID, 10, height - 10);

  // Check if enemy should reappear
  if (!Enemy.visible && millis() - Enemy.hideTimer >= 3000) {
    Enemy.visible = true;
  }

  // Move enemy up and down if visible
  if (Enemy.visible) {
    Enemy.YPos += Enemy.Speed * Enemy.Direction;
    if (Enemy.YPos <= 0 || Enemy.YPos + Enemy.YSize >= height) {
      Enemy.Direction *= -1;
    }

    // Draw the enemy
    fill(255, 100, 100);
    rect(Enemy.XPos, Enemy.YPos, Enemy.XSize, Enemy.YSize);

    // Draw enemy weapon
    fill(100, 100, 200);
    rect(Enemy.XPos - 10, Enemy.YPos + 10, Enemy.WeaponSizeX, Enemy.WeaponSizeY);

    // Display enemy name
    fill(0);
    textSize(12);
    text("Enemy: " + Enemy.Name, width - 100, height - 40);
    text("Weapon: " + Enemy.WeaponName, width - 100, height - 25);
    text("ID: " + Enemy.ID, width - 100, height - 10);
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
    MainCharacterBullet.bullets.push({
      x: MainChacter.XPos + MainChacter.XSize,
      y: MainChacter.YPos + MainChacter.YSize / 2 - MainCharacterBullet.height / 2
    });
  }
}
