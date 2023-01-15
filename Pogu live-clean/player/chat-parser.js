var video = document.getElementById('video');
var chatListContainer = document.getElementById('chat-list-container');
var chatWrapper = document.getElementById('chat-wrapper');

var videoID = window.location.href.split("#")[2];
var startTime = window.location.href.split("#")[3];

if (videoID == null || startTime == null) {
    alert("Invalid URL");
    window.location.href = window.location.origin + "/"; // redirect to home page
}

var chatGetter = new ChatGetter(videoID, startTime.replace("_", " "));
// var chatGetter = new ChatGetter("1602009987", "2022-09-26 17:51:25");

const MESSAGE_LIMIT = 300;

if (video != null) {
    video.addEventListener('timeupdate', async function() { // average update time is 0.260 seconds (4 times per second)
        var currentTime = video.currentTime;

        chatGetter.getNextMessages(currentTime).then((nextMessages) => {
            if (nextMessages.length != 0) {
                nextMessages.forEach((nextMessage) => {

                    chatListContainer.appendChild(nextMessage);
                    
                    chatWrapper.scrollTop = chatWrapper.scrollHeight; // scroll to bottom

                    // remove the top message if there is more than MESSAGE_LIMIT messages
                    if (chatListContainer.childElementCount > MESSAGE_LIMIT) {
                        chatListContainer.removeChild(chatListContainer.firstChild);
                        // console.log("removed top message");
                    }
                });
            }
        });

    });
}