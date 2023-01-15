// -------- Video Player --------

var videoSrc = window.location.href.split("#")[1];
document.getElementById("video-src").src = videoSrc;

var video = videojs('video', {
    playbackRates: [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
});

video.fill(true);
video.play();

function seekTime() {
    // us pop up to enter time
    var time = prompt("Enter time in format hh:mm:ss");
    var timeArray = time.split(":");
    
    if(timeArray.length == 3) {
        seconds = parseInt(timeArray[0])*3600 + parseInt(timeArray[1])*60 + parseInt(timeArray[2]);
    } else if(timeArray.length == 2) {
        seconds = parseInt(timeArray[0])*60 + parseInt(timeArray[1]);
    } else if(timeArray.length == 1) {
        seconds = parseInt(timeArray[0]);
    }

    video.currentTime(seconds);
    console.log("seekTime");
}

window.addEventListener('load', function () {
    Mousetrap.bind('s', seekTime);
});

// ------------------------------

var chatListContainer = document.getElementById('chat-list-container');
var chatWrapper = document.getElementById('chat-wrapper');

var videoID = window.location.href.split("#")[2];
var startTime = window.location.href.split("#")[3];

const DONT_UPDATE_IN_FULLSCREEN = true;
const MESSAGE_LIMIT = 300;

if (videoID == null || startTime == null) {
    alert("Invalid URL");
    window.location.href = window.location.origin + "/"; // redirect to home page
}

var chatGetter = new ChatGetter(videoID, startTime.replace("_", " "));

// -------- check if scrolling up or down --------

var autoScroll = true;
var lastScrollTop = 0;
chatWrapper.addEventListener("scroll", function(){ // or window.addEventListener("scroll"....
    var st = window.pageYOffset || chatWrapper.scrollTop;

    if (st > lastScrollTop){
        // scrolling down
    } else {
        // scrolling up
        autoScroll = false;
        // console.log("stop auto scroll");
    }

   lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling

    if (chatWrapper.clientHeight + chatWrapper.scrollTop == chatWrapper.scrollHeight) {
        autoScroll = true;
        // console.log("restart auto scroll");
    }
}, false);

// -------- parse chat messages --------

function addMessageToChat(message, reversed, autoScroll) {
    if (!reversed) {
        // append the message to the bottom of the chat list
        chatListContainer.appendChild(message);

        if (autoScroll) {
            chatWrapper.scrollTop = chatWrapper.scrollHeight; // scroll to bottom
        }

        // remove the top message if there is more than MESSAGE_LIMIT messages
        if (chatListContainer.childElementCount > MESSAGE_LIMIT) {
            chatListContainer.removeChild(chatListContainer.firstChild);
        }
    } else {
        // append the message to the top of the chat list
        chatListContainer.insertBefore(message, chatListContainer.firstChild);

        if (autoScroll) {
            chatWrapper.scrollTop = 0; // scroll to top
        }

        // remove the bottom message if there is more than MESSAGE_LIMIT messages
        if (chatListContainer.childElementCount > MESSAGE_LIMIT) {
            chatListContainer.removeChild(chatListContainer.lastChild);
        }
    }
}

if (video != null) {
    video.on('timeupdate', async function() { // average update time is 0.260 seconds (4 times per second)
        var currentTime = video.currentTime();

        if (!document.webkitIsFullScreen && DONT_UPDATE_IN_FULLSCREEN) {
            chatGetter.getNextMessages(currentTime).then((nextMessages) => {
                if (nextMessages.length != 0) {
                    nextMessages.forEach((nextMessage) => {
    
                        if (window.innerWidth > 1000) {
                            addMessageToChat(nextMessage, false, autoScroll);
                        } else {
                            addMessageToChat(nextMessage, true, autoScroll);
                        }
                    });
                }
            });
        }

        // console.log("messages length: " + chatGetter.messages.length);
    });
}


// -------- reverse chat if screen width is less than 1000px --------


var reversed = false;// console.log("messages length: " + chatGetter.messages.length);

// event listener for the resizing of the window
window.addEventListener('resize', function() {

    if (window.innerWidth < 1000 && !reversed) {
        // reverse the list "chat-list-container"
        for (var i = chatListContainer.childNodes.length - 1; i >= 0; i--) {
            chatListContainer.appendChild(chatListContainer.childNodes[i]);
        }

        reversed = true;
        // console.log("reversed the list");
    } else if (window.innerWidth >= 1000 && reversed) {
        // reverse the list "chat-list-container"
        for (var i = chatListContainer.childNodes.length - 1; i >= 0; i--) {
            chatListContainer.appendChild(chatListContainer.childNodes[i]);
        }

        reversed = false;
        // console.log("reversed the list");
    }

    // console.log("window width: " + windowWidth);
});