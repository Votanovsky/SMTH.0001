const path = require('path')

module.exports = {
    entry: {
        index: "./js/index.js"
    },
    module: {
        rules: [
            {test: /\.(png|jpeg)$/, use: "image-loader"},
            {test: /\.css$/, use: ["style-loader", "css-loader"]}
        ]
    },
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'index_bundle.js'
    },
    mode: "development"
}
