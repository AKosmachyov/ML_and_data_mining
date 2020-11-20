export class Vector2 {

    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }

    add(v) {
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