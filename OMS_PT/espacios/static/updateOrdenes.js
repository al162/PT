
const socket = new WebSocket(`ws://${window.location.host}/ws/socket-server`);

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    location.reload()
    console.log(data.message);
};

socket.onclose = function (e) {
    console.error('WebSocket cerrado:', e);
};