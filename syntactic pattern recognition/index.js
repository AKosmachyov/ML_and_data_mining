import { Vector2 } from './Vector2.js';
import { PatternRecognition } from './PatternRecognition.js';
/**
 * @typedef {import('./PatternRecognition').PatternRecognition} PatternRecognition
 */

const STEP = 10;

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

function isTermElement(term) {
    return term.offset instanceof Vector2;
}

[...rootRules, squareRule2, squareRule3, squareRule4, triangleRule2, triangleRule3, triangleRule4].forEach(rule => {
    const { name, x, y } = rule;

    P[name] = {
        x: isTermElement(x) ? x : x.name,
        y: y == undefined ? undefined : isTermElement(y) ? y : y.name
    };
    Vn.push(name);
})

const canvas = document.getElementById('field');
const ctx = canvas.getContext('2d');
const PEN_START_POINT = new Vector2(40, 40);

const patternRecognition = new PatternRecognition(Vt, Vn, P, rootRuleNames, ctx);
patternRecognition.generate(rootRuleNames[0], PEN_START_POINT);
patternRecognition.generate(rootRuleNames[1], PEN_START_POINT);


rootRuleNames.forEach(rule => {
    const { successful, errorMsg = [] } = patternRecognition.drawingMatchWithAxiom(rule, PEN_START_POINT);
    console.log(rule, successful ? '✅' : '❌', ...errorMsg);
})