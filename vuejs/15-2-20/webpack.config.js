const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const vueLoaderPlugin = require('vue-loader/lib/plugin.js');
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
                exclude: /node_modules/,
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
            },
            {
                test: /\.scss$/,
                use: [
                  'vue-style-loader',
                  'css-loader',
                  'sass-loader'
                ]
              }
        ]
    },
    plugins:[
        new HtmlWebpackPlugin({
            template: 'public/index.html'
        }),
        new vueLoaderPlugin()
    ]
}