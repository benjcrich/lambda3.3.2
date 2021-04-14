$('#tweet_text_input').value = "Please enter a twitter user's handle";
$('#tweet_submit').click(function () {
    $.ajax({
        url: '/add_user?twitter_handle=' + $('#tweet_text_input').val(),
        type: 'GET',
    });
});