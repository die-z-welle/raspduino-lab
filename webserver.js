var util   = require('util'),
sys = require('sys'),
ws = require('/usr/lib/node_modules/nodejs-websocket'),
spawn = require('child_process').spawn,
server = ws.createServer(function(conn) {
	console.log('new connection');
	conn.on('close', function(code, reason) {
		console.log('connection closed');
	});
}),
mosq = spawn('mosquitto_sub',['-t','messwerte/test']);

mosq.stdout.on('data', function (data) {
	server.connections.forEach(function(conn) {
		conn.sendText(data);
	});
	console.log('' + data);
});

mosq.stderr.on('data', function (data) {
	console.log('error: ' + data);
});

server.listen(8000);
