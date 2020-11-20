import { Vector2 } from './Vector2.js';

const canvas = document.getElementById('field');
const ctx = canvas.getContext('2d');

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

const triangleRule4 = {
    name: 'F',
    x: downLeft
}

const triangleRule3 = {
    name: 'E',
    x: upLeft,
    y: triangleRule4
}

const triangleRule2 = {
    name: 'D',
    x: right,
    y: triangleRule3
}

const triangleRule = {
    name: 'Triangle',
    x: right,
    y: triangleRule2,
}

const squareRule4 = {
    name: 'C',
    x: down,
}

const squareRule3 = {
    name: 'B',
    x: left,
    y: squareRule4
}

const squareRule2 = {
    name: 'A',
    x: up,
    y: squareRule3
}

const squareRule = {
    name: 'Square',
    x: right,
    y: squareRule2
}

const rootRules = [
    squareRule,
    triangleRule
]

const rootRuleNames = rootRules.map(el => el.name);

const Vn = []; // nonterminal dictionary
const Vt = [down, right, up, left, upLeft, downLeft]; // terminal dictionary

const P = {}; // rules (name: {x, y}

[...rootRules, squareRule2, squareRule3, squareRule4, triangleRule2, triangleRule3, triangleRule4].forEach(rule => {
    const { name, x, y } = rule;

    P[name] = {
        x: isTermElement(x) ? x : x.name,
        y: y == undefined ? undefined : isTermElement(y) ? y : y.name
    };
    Vn.push(name);
})

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

// draw(right);
// draw(up);
// draw(left);
// draw(down);

ctx.stroke();

function getRule(name, Vn, Vt, P) {
    const terminalElement = Vt.find(el => el.name == name);
    if (terminalElement) {
        return terminalElement;
    }
    const nonterminalElement = Vn.indexOf(name) > -1;
    if (nonterminalElement) {
        return P[name]
    }

    console.error(`item "${name}" not found in dictionary`);
    return null;
}

function isTermElement(term) {
    return term.offset instanceof Vector2;
}

function checkIsValidFigureForRule(ruleName, startPoint, matrix, Vn, Vt, P) {
    const callstack = [ruleName];

    do {
        const currentElement = callstack.pop();
        if (isTermElement(currentElement)) {
            if (checkIsFilled(startPoint, currentElement, matrix)) {
                startPoint.add(currentElement.offset);
            } else {
                return {
                    errorMsg: ['Required pattern not found:', currentElement],
                    successful: false
                }
            }

            continue
        }

        const rule = getRule(currentElement, Vn, Vt, P);
        if (rule.y) {
            callstack.push(rule.y)
        }
        callstack.push(rule.x);
    } while (callstack.length != 0)

    return {
        successful: true,
    };
}

rootRuleNames.forEach(rule => {
    startPoint.copy(PEN_START_POINT);
    const { successful, errorMsg = [] } = checkIsValidFigureForRule(rule, startPoint, matrix, Vn, Vt, P);
    console.log(rule, successful ? '✅' : '❌', ...errorMsg);
})

function checkIsFilled(startPoint, term, matrix) {
    const endVector = startPoint.clone().add(term.offset);
    const delta = endVector.clone().sub(startPoint);

    if (delta.x == 0) {
        const action = Math.sign(delta.y);
        const max = Math.abs(delta.y);
        for (let y = 0; y < max; y++) {
            if (matrix[startPoint.y + action * y][startPoint.x] != 1) {
                return false
            }
        }
    }

    if (delta.y == 0) {
        const action = Math.sign(delta.x);
        const max = Math.abs(delta.x);
        for (let x = 0; x < max; x++) {
            if (matrix[startPoint.y][startPoint.x + action * x] != 1) {
                return false
            }
        }
    }

    // for 45 deg
    const actionX = Math.sign(delta.x);
    const actionY = Math.sign(delta.y);
    const max = Math.abs(delta.x);
    for (let x = 0; x < max; x++) {
        if (matrix[startPoint.y + actionY * x][startPoint.x + actionX * x] != 1) {
            return false;
        }
    }

    return true
}