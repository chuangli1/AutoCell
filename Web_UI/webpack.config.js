// nodejs 中的path模块
var path = require('path');
const webpack = require('webpack');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {

    mode: process.env.NODE_ENV,
    watch: (process.env.NODE_ENV==='development'),
    entry: ['babel-polyfill',path.resolve(__dirname, './main.js')],
    // 输出配置
    output: {
        path: path.resolve(__dirname, './dist'),
        publicPath: '/dist/',
        filename: '[name].[hash].js',
        chunkFilename: '[id].[chunkhash].js'
    },
    module: {
        
        rules: [
            // 使用vue-loader 加载 .vue 结尾的文件
            {
                test: /\.vue$/,
                loader: 'vue-loader',
              },
              { 
                test: /\.tsx?$/, 
                loader: "ts-loader",
                exclude: /node_modules/,
                options: {
                  appendTsSuffixTo: [/\.vue$/],
                }
              }
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        //new VuetifyLoaderPlugin(),
        new webpack.ProvidePlugin({
          "$":"jquery",
          "jQuery":"jquery",
          "window.jQuery":"jquery"
        }),
        // new MiniCssExtractPlugin({
        //   filename: 'style.css'
        // }),
      ],
      // resolve: {
      //   extensions:['.ts', '.js', '.json'],
      //   alias: {
      //     'vue$': 'vue/dist/vue.esm.js',
      //     'vue$': 'vue/dist/vue.common.js',
      //     jquery: path.join(__dirname, 'node_modules/jquery/dist/jquery.min'),
      //     modules: path.join(__dirname, "node_modules"),
      //   }
      // },
}