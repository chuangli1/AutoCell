//使用express构建web服务器 --11:25
const express = require('express');

var app = express();

// 端口号
var server = app.listen(6789);

//托管静态资源到public目录下
app.use(express.static('dist'));
console.log('App is running on port 6789......')