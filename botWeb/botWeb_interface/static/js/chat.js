// Credits goes to https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django

$(function() {

    // When using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chat_zone = $("#chat_zone");   
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat");

    
    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        chat_zone.prepend(
            $("<p class='answer'></p>").text('AI: ' + data.message)
        );
    };

    $("#chat_form").on("submit", function(event) {

        try {
            var message_elem = $('#message');
            var message_val = message_elem.val();

            if (message_val) {
                // Send the message
                var message = {
                    message: message_val
                };
                chatsock.send(JSON.stringify(message));
                message_elem.val('').focus();

                // Add the message to the chat
                chat_zone.prepend(
                    $("<p class='question'></p>").text('Me: ' + message_val)
                );
            }
        }
        catch(err) {
            console.error(err.message);
        }

        return false;
    });
});
