$( document ).on('click', '#categories', function(event) {
    $.ajax({
                url: '/api/v0/categories/',
                success: function (data) {
                    // data - ответ от сервера
                    console.log('Step 3')
                    //console.log(data);
                    for (i = 0; i < data.length; i++) {
                        // словарь
                       item = data[i];
                       name = item.name;
                       console.log(name);
                       $('#div_categories').append('<li>' + name + '</li>' );
                    }
                    //$('#wrapper').append('<a href="http://google.com">Гугли!</a>');
                    //$('#div_categories').html(data);
                },
            });
});


$( document ).on('click', '#posts', function(event) {
    $.ajax({
                url: '/api/v0/recipes/',
                success: function (data) {
                    // data - ответ от сервера
                    //console.log(data);
                    for (i = 0; i < data.length; i++) {
                        // словарь
                       item = data[i];
                       name = item.name;
                       console.log(name);
                       $('#div_posts').append('<li>' + name + '</li>' );
                    }
                    //$('#wrapper').append('<a href="http://google.com">Гугли!</a>');
                    //$('#div_categories').html(data);
                },
            });
});


$( document ).on('click', '#all', function(event) {
$.ajax({
                url: '/api/v0/categories/',
                success: function (data) {
                    // data - ответ от сервера
                    console.log('Step 3')
                    //console.log(data);
                    for (i = 0; i < data.length; i++) {
                        // словарь
                       item = data[i];
                       name = item.name;
                       console.log(name);
                       $('#div_categories').append('<li>' + name + '</li>' );
                    }
                    //$('#wrapper').append('<a href="http://google.com">Гугли!</a>');
                    //$('#div_categories').html(data);
                },
            });
    $.ajax({
                url: '/api/v0/recipes/',
                success: function (data) {
                    // data - ответ от сервера
                    //console.log(data);
                    for (i = 0; i < data.length; i++) {
                        // словарь
                       item = data[i];
                       name = item.name;
                       console.log(name);
                       $('#div_posts').append('<li>' + name + '</li>' );
                    }
                    //$('#wrapper').append('<a href="http://google.com">Гугли!</a>');
                    //$('#div_categories').html(data);
                },
            });
});