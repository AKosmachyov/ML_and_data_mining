const canvas = document.getElementById('field');
const ctx = canvas.getContext('2d');

class Vector2 {

    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }

    add(v, w) {
        this.x += v.x;
        this.y += v.y;
        return this;
    }

    addVectors(v, w) {
        const result = new Vector2();
        this.x = v.x + w.x;
        this.y = v.y + w.y;
        return result;
    }

    sub(v) {
        this.x -= v.x;
        this.y -= v.y;
        return this;
    }

    clone() {
        return new this.constructor(this.x, this.y);
    }

    copy(v) {
        this.x = v.x;
        this.y = v.y;
        return this;
    }

}

const MATRIX_SIZE = 30;
const STEP = 4;
const PEN_START_POINT = new Vector2(3, 10);
const MATRIX_FILL_ELEMENT = '';

const matrix = new Array(MATRIX_SIZE).fill(MATRIX_FILL_ELEMENT);
for (let i = 0; i < matrix.length; i++) {
    matrix[i] = new Array(MATRIX_SIZE).fill(MATRIX_FILL_ELEMENT)
}

const down = {
    name: 'down',
    offset: new Vector2(0, STEP),
}
const right = {
    name: 'right',
    offset: new Vector2(STEP, 0),
}
const up = {
    name: 'up',
    offset: new Vector2(0, -STEP),
}
const left = {
    name: 'left',
    offset: new Vector2(-STEP, 0),
}
const upLeft = {
    name: 'up-left 45',
    offset: new Vector2(-STEP, -STEP),
}
const downLeft = {
    name: 'down-left 45',
    offset: new Vector2(-STEP, STEP),
}

const squareRule4 = {
    name: 'D',
    x: down.name,
}

const squareRule3 = {
    name: 'C',
    x: left.name,
    y: squareRule4
}

const squareRule2 = {
    name: 'B',
    x: up.name,
    y: squareRule3
}

const SquareRule = {
    name: 'square',
    x: right.name,
    y: squareRule2
}

const Vn = [SquareRule.name, squareRule2.name, squareRule3.name, squareRule4.name]; // nonterminal dictionary
const Vt = [down, right, up, left, upLeft, downLeft]; // terminal dictionary

const P = [
    SquareRule,
    squareRule2,
    squareRule3,
    squareRule4
] // rules

const numberOfFigures = 2

let startPoint = PEN_START_POINT.clone();
ctx.beginPath();
ctx.moveTo(startPoint.x, startPoint.y);

function draw(term) {
    const endVector = startPoint.clone().add(term.offset);
    
    ctx.lineTo(endVector.x, endVector.y);

    const delta = endVector.clone().sub(startPoint);
    if (delta.x == 0) {
        const action = Math.sign(delta.y);
        const max = Math.abs(delta.y);
        for (let y = 0; y < max; y++) {
            matrix[startPoint.y + action * y][startPoint.x] = 1;
        }
    }

    if (delta.y == 0) {
        const action = Math.sign(delta.x);
        const max = Math.abs(delta.x);
        for (let x = 0; x < max; x++) {
            matrix[startPoint.y][startPoint.x + action * x] = 1;
        }
    }

    // for 45 deg
    const actionX = Math.sign(delta.x);
    const actionY = Math.sign(delta.y);
    const max = Math.abs(delta.x);
    for (let x = 0; x < max; x++) {
        matrix[startPoint.y + actionY * x][startPoint.x + actionX * x] = 1;
    }

    startPoint.copy(endVector);
}

draw(right);
draw(right);
draw(upLeft);
draw(downLeft);

// draw(down);
// draw(down);

// draw(right);
// draw(up);
// draw(left);
// draw(down);

ctx.stroke();

console.table(matrix);