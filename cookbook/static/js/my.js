// alert('Hello Js!');


var button = document.querySelector("#btn-joke");
console.log(button);

function foo(event)
{
    // alert('Hello Js!');
    element = event.target;

    if ( element.classList.contains('btn-secondary') )
    {
        var new_class = 'btn-danger';
        var old_class = "btn-secondary";
    }
    else {
        var new_class = 'btn-secondary';
        var old_class = 'btn-danger';
    }

    element.classList.remove(old_class);
    element.classList.add(new_class);
}

button.addEventListener('click', foo, false);


// ajax
$( document ).on('click', '#ajax-btn', function(event) {
    console.log('Step 1');
    $.ajax({
                url: '/users/update-token-ajax/',
                success: function (data) {
                    // data - ответ от сервера
                    console.log('Step 3')
                    console.log(data);
                    $('#token').html(data.key);
                },
            });
});
