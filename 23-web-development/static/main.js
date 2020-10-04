console.log("hello") 

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

function fetchUsers(){
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
