//使用express构建web服务器 --11:25
const express = require('express');
const httpProxy = require('http-proxy');
const path = require('path');
const http = require('http');
const proxy = httpProxy.createProxyServer({});
proxy.on('error', function (err, req, res) {
    console.error(err);
});
process.on('uncaughtException', function (err) {
    console.error(err);
});

const app = express();
app.use(express.static('dist'));


const remoteInst = "http://localhost:5000";
console.log(remoteInst);
app.use(function(req, res, next) {
    if(!req.path.startsWith('/dist')) {
        proxy.web(req, res, { target: remoteInst, secure: false });
    } else {
        const str = 'Static resource does not exist: '+req.path;
        console.log(str);
        res.writeHead(404);  
        res.end(str);
    }
});

const server = http.createServer(app);

server.listen(6789);


// // 端口号
// var server1 = app.listen(6789);

// //托管静态资源到public目录下
// app.use(express.static('dist'));
// console.log("App is running on http://localhost:6789")