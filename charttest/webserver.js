var util   = require('util'),
sys = require('sys'),
ws = require('/usr/local/lib/node_modules/nodejs-websocket'),
sleep = require('/usr/local/lib/node_modules/sleep'),
server = ws.createServer(function(conn) {
	console.log('new connection');
    
    for (var i = 0; i < 100; i++){
        conn.send(i + '');
        sleep.sleep(1);
    }
    
	conn.on('close', function(code, reason) {
		console.log('connection closed');
	});
});

server.listen(8000);