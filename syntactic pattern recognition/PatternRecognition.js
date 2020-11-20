import { Vector2 } from "./Vector2.js";

const EMPTY_MATRIX_ELEMENT = 0;
const FILLED_MATRIX_ELEMENT = 1;
const MATRIX_SIZE = 300;

/**
 * @typedef {Object} Termin
 * @property {string} name The name of the termin.
 * @property {Vector2} offset The offset from current pen position.
 */

 /**
  * Element replacement rules. X connected with Y
  * @typedef {Object} ReplacementRule
  * @property {string | Termin } x 
  * @property {string | Termin | undefined} y
 */

/** 
* Сlass for creating and recognizing figures by syntax.
*/
export class PatternRecognition {

    constructor(terminalDictionary, nonterminalDictionary, replacementRules, initialAxioms, canvasCtx) {
        /** 
         * @property {Array.<number[]>} matrix 2d matrix representation of a figure.
         */
        this.matrix = [];
        this.ctx = canvasCtx;
        /** 
         * @property {Termin[]} vt array of syntax terms (constants).
         */
        this.vt = terminalDictionary;
        /** 
         * @property {string[]} vn array of non-terminal syntax elements (variables).
         */
        this.vn = nonterminalDictionary;
        this.p = replacementRules;
        this.s = initialAxioms;

        this._resetMatrix();
    }

    _resetMatrix() {
        this.matrix = new Array(MATRIX_SIZE).fill(EMPTY_MATRIX_ELEMENT);
        for (let i = 0; i < this.matrix.length; i++) {
            this.matrix[i] = new Array(MATRIX_SIZE).fill(EMPTY_MATRIX_ELEMENT);
        }
    }

    generate(axiom, startPoint) {
        const start = startPoint.clone();
        this.ctx.beginPath();
        this.ctx.moveTo(start.x, start.y);

        const callstack = [axiom];
        do {
            const currentElement = callstack.pop();
            if (this._isTermElement(currentElement)) {
                this._draw(currentElement, start);
                continue;
            }

            const rule = this._getRule(currentElement);
            if (rule.y) {
                callstack.push(rule.y)
            }
            callstack.push(rule.x);
        } while (callstack.length != 0)

        this.ctx.stroke();
    }

    _isTermElement(term) {
        return term.offset instanceof Vector2;
    }

    /** 
     * @property {string} axiomName
     * @returns {}
     */
    _getRule(axiomName) {
        const nonterminalElement = this.vn.indexOf(axiomName) > -1;
        if (nonterminalElement) {
            return this.p[axiomName];
        }

        console.error(`item "${axiomName}" not found in dictionary`);
        return null;
    }

    /**
     * Draw figure part on the canvas and update matrix.
     * @param {Termin} termin
     * @param {Vector2} startPoint - starting point for drawing, after drawing the value mutates
     */
    _draw(termin, startPoint) {
        const endVector = startPoint.clone().add(termin.offset);

        this.ctx.lineTo(endVector.x, endVector.y);

        const delta = endVector.clone().sub(startPoint);
        if (delta.x === 0) {
            const action = Math.sign(delta.y);
            const max = Math.abs(delta.y);
            for (let y = 0; y < max; y++) {
                this.matrix[startPoint.y + action * y][startPoint.x] = FILLED_MATRIX_ELEMENT;
            }
        }

        if (delta.y === 0) {
            const action = Math.sign(delta.x);
            const max = Math.abs(delta.x);
            for (let x = 0; x < max; x++) {
                this.matrix[startPoint.y][startPoint.x + action * x] = FILLED_MATRIX_ELEMENT;
            }
        }

        // for 45 deg
        const actionX = Math.sign(delta.x);
        const actionY = Math.sign(delta.y);
        const max = Math.abs(delta.x);
        for (let x = 0; x < max; x++) {
            this.matrix[startPoint.y + actionY * x][startPoint.x + actionX * x] = FILLED_MATRIX_ELEMENT;
        }

        startPoint.copy(endVector);
    }

    /**
     * @param {string} axiomName
     * @param {Vector2} startPoint
     * @returns {boolean} isMatch
     */
    drawingMatchWithAxiom(axiomName, startPoint) {
        const start = startPoint.clone();
        const callstack = [axiomName];

        do {
            const currentElement = callstack.pop();
            if (this._isTermElement(currentElement)) {
                if (this._checkIsTerminFilled(start, currentElement)) {
                    start.add(currentElement.offset);
                } else {
                    return {
                        errorMsg: ['Required pattern not found:', currentElement],
                        successful: false
                    }
                }

                continue
            }

            const rule = this._getRule(currentElement);
            if (rule.y) {
                callstack.push(rule.y)
            }
            callstack.push(rule.x);
        } while (callstack.length != 0)

        return {
            successful: true,
        };
    }

    /**
     * @param {Vector2} startPoint - starting point for checking
     * @param {Termin} termin
     * @return {boolean} isFilled is this element rendered in the matrix
     */
    _checkIsTerminFilled(startPoint, termin) {
        const endVector = startPoint.clone().add(termin.offset);
        const delta = endVector.clone().sub(startPoint);

        if (delta.x === 0) {
            const action = Math.sign(delta.y);
            const max = Math.abs(delta.y);
            for (let y = 0; y < max; y++) {
                if (this.matrix[startPoint.y + action * y][startPoint.x] !== FILLED_MATRIX_ELEMENT) {
                    return false
                }
            }
        }

        if (delta.y === 0) {
            const action = Math.sign(delta.x);
            const max = Math.abs(delta.x);
            for (let x = 0; x < max; x++) {
                if (this.matrix[startPoint.y][startPoint.x + action * x] !== FILLED_MATRIX_ELEMENT) {
                    return false
                }
            }
        }

        // for 45 deg
        const actionX = Math.sign(delta.x);
        const actionY = Math.sign(delta.y);
        const max = Math.abs(delta.x);
        for (let x = 0; x < max; x++) {
            if (this.matrix[startPoint.y + actionY * x][startPoint.x + actionX * x] !== FILLED_MATRIX_ELEMENT) {
                return false;
            }
        }

        return true
    }
}