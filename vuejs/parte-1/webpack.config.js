const path = require('path')
module.exports={
    entry: './src/app.js',
    output:{
        path: __dirname + '/dist/src',
        filename: 'bundle.js'
    },
    module:{
        rules:[
            {
                test: /\.js$/,
                excludes: /node_modules/,
                loader: 'babel-loader'
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.css$/,
                use:[
                    'vue-style-loader',
                    {
                        loader: 'css-loader',
                    },
                    'postcss-loader'
                ]
            }
        ]
    }
}