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
}


//Movement
function keyPressed() {
  if (keyCode === LEFT_ARROW) {
    MainChacter.XPos -= MainChacter.Speed;
  } else if (keyCode === RIGHT_ARROW) {
    MainChacter.XPos += MainChacter.Speed;
  } else if (keyCode === UP_ARROW) {
    MainChacter.YPos -= MainChacter.Speed;
  } else if (keyCode === DOWN_ARROW) {
    MainChacter.YPos += MainChacter.Speed;
  }
}
