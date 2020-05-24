// Credits goes to https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django

function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    var uid_null = Math.floor(Math.random() * 1000000);
    if (r != null) return unescape(r[2]);
    return uid_null.toString();
}

$(function() {

    // When using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chat_zone = $("#chat_zone");
    // var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chatbot");
    var session_id = getQueryString('userid')
    var session_id = 'userid'
    var chatsock = new ReconnectingWebSocket(
        'ws://' +
        window.location.host +
        '/ws/chatbot/' +
        session_id + '_' + getQueryString('userid') + '/'
    );

    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        chat_zone.append(
            $("<p class='answer'></p>").html('AI: ' + data.message)
        );
    };

    $("#chat_form").on("submit", function(event) {

        try {
            var message_elem = $('#message');
            var message_val = message_elem.val();

            if (message_val) {
                // Send the message
                var message = {
                    type: 'text',
                    client_type: 'django',
                    message: message_val
                };
                chatsock.send(JSON.stringify(message));
                message_elem.val('').focus();

                // Add the message to the chat
                chat_zone.append(
                    $("<p class='question'></p>").text('Me: ' + message_val)
                );
            }
        } catch (err) {
            console.error(err.message);
        }

        return false;
    });
});