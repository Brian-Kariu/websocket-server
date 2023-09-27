const http = require('http');
const server = http.createServer();
server.on('request', (req, res) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.url}`);
    res.setHeader('Content-type', 'text/plain');
    res.end('Hello World!')
});
server.listen(3000)
