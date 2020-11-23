const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin')
function resolve (dir) {
  return path.join(__dirname, '..', dir)
}
module.exports = {
  watch:true,
  entry: './src/index.ts',
  mode: 'development',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  resolve: {
    // Add `.ts` and `.tsx` as a resolvable extension.
    extensions: [".ts", ".tsx", ".js"],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',//内部为正则表达式  vue结尾的
      '@': resolve('src'),
    },

  },
  module: {
    rules: [
      // ... 其它规则
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          esModule: true,
        }
      },
      {
        test: /\.tsx?$/, loader: "ts-loader", 
        options: {
          appendTsSuffixTo: [/\.vue$/]
        }
      }
    ]
  },
  devServer: {
    contentBase: path.join(__dirname, "dist"),
    port:6789,
    historyApiFallback:{
       rewrites:[
          {from:/./,to:'./src/index.html'}
       ]
      }
     },
  plugins: [
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: './src/index.html',
      inject: true
    }),
    new VueLoaderPlugin()
  ]
};