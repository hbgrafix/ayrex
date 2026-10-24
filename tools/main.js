const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

const canvasSize = 500;
const width = canvas.width = canvasSize;
const height = canvas.height = canvasSize;
const gridSize = width / 4;
const cellSize = gridSize / 3;
const origin = {x: 0 - cellSize / 2, y: 0 - cellSize / 2};


class Cell {
    constructor(x, y, size = cellSize, color = 'rgba(255, 255, 255, 0.25)', stroke = 'rgba(255, 255, 255, 1)') {
        this.x = origin.x + x;
        this.y = origin.x + y;
        this.color = color;
        this.stroke = stroke;
        this.width = size;
        this.height = size;
    }
    draw() {
        ctx.beginPath();
        ctx.rect(this.x, this.y, this.width, this.height);
        ctx.fillStyle = this.color;
        ctx.strokeStyle = this.stroke;
        ctx.stroke();
        ctx.fill();
    }
}
function drawRow (number = 1, count = 1, dimension) {
    const size = cellSize;
    for (let i = 0; i < number; i++) {
        if (dimension === "x") {
            x = i * size;
            y = count * size;
            color = 'rgba(255, 0, 0, 0.25)';
            stroke = 'rgba(255, 0, 0, 0.5)';
        } else if (dimension === "y") {
            x = count * size;
            y = i * size;
            color = 'rgba(0, 255, 0, 0.25)';
            stroke = 'rgba(0, 255, 0, 0.5)'
        } else if (dimension === "z") {
            x = i * size;
            y = i * size;
            color = 'rgba(0, 0, 255, 0.25)';
            stroke = 'rgba(0, 0, 255, 0.5)';
        }
        const cell = new Cell(x, y, size, color, stroke);
        cell.draw();
    }
}
function drawColumn (number = 1, count = 1, dimension = 'x') {
    ctx.clearRect(0, 0, width, height);
    for (let i = 0; i < count; i++) {
        drawRow(number, i, dimension);
    }
}

function drawGrid (gridSize) {
    drawColumn (gridSize, gridSize);
}

function drawBorder() {
    ctx.save()
    ctx.lineWidth = cellSize - 1;
    ctx.beginPath();
    ctx.rect(0, 0, width, height);
    ctx.strokeStyle = 'rgba(0, 0, 0, 1)';
    ctx.stroke();
    ctx.restore();
}


const playerCells = [];

const playerCell = new Cell(origin.x + width / 2 + cellSize / 2, origin.y + width / 2  + cellSize / 2);
console.log(playerCell);

window.addEventListener('keydown', (e) => {
    const offset = cellSize;
    switch (e.key) {
        case "ArrowUp":
            playerCell.y -= offset;
            break;
        case "ArrowDown":
            playerCell.y += offset;
            break;
        case "ArrowLeft":
            playerCell.x -= offset;
            break;
        case "ArrowRight":
            playerCell.x += offset;
            break;
    }

    renderCanvas();
    playerCell.draw();
    console.log(playerCell);
    playerCells.push(new Cell(playerCell.x, playerCell.y)); // create a new Cell object with the updated position
    //console.log(playerCells);
})


function renderCanvas() {
    ctx.clearRect(0, 0, width, height);
    drawGrid(gridSize);
    drawBorder();
    playerCell.draw();
}

renderCanvas();


canvas.addEventListener('click', (e) => {
    const cellX = Math.floor(e.clientX / cellSize * cellSize);
    const cellY = Math.floor(e.clientY / cellSize * cellSize) - cellSize;
    const clickedCell = new Cell (cellX, cellY);
    clickedCell.draw();
    // Handle click event on clickedCell
});

