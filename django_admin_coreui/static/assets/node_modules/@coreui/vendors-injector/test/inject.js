const inject = require('..');
const path = require('path')
const { dirname } = path
const { resolve } = path

inject(resolve(__dirname, 'src/main.html'))
