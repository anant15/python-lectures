console.log("hello") 

var socket = io.connect(location.protocol+'//'+document.domain+':'+location.port);
// socket.on('connect', function(){
//     socket.emit('my event', {data: 'I\'m connected!'});
// });
//console.log(socket)

function send(){
    var msgBox = document.getElementById('msgBox')
    // client will send the message to the server
    socket.emit('msg', msgBox.value)
    //console.log(msgBox.value)
    console.log("Server should print the message")
    msgBox.value = "" 
}


// listener for the message received from the server
socket.on("push", function(data){
    console.log(data)
    var msgList = document.getElementById('msgList')
    msgList.innerHTML += "<p>" + data + "</p>"

})

// Now, we want Javascript to create fetching like calls.
function fetchUsers()
{
    fetch('/users').then(function(res)
    {
        res.json().then(
                        function(data)
                        {
                            console.log(data)
                        }
    )
})
}

// var x = 5

// if (x>2)
// {
//     console.log("greater")
// }
// else
// {
//     console.log("smaller")
// }
// function area(l, b)
// {
//     var a = l * b
//     return a
// }

// a1 = area(4, 5)

// for (var i=1; i<=5; i+=1)
// {
//     console.log(i)
// }
