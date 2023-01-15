class ChatGetter {
    twitchApiUrl = "https://gql.twitch.tv/gql";
    twitchApiHeaders = {
        "Client-Id" : "kimne78kx3ncx6brgo4mv6wki5h1ko", // this is the client id of the twitch web app
    };
    videoUpdateTime = 0.260;

    constructor(videoID, startTime) {
        this.videoID = videoID;
        this.startTime = Date.parse(startTime);
        this.messages = [];
        this.getMessagesFromSecOffset(0);
        this.isUpdating = false;
    }

    static createChatElement(node) {
        var chatLine = document.createElement("li");
        chatLine.classList.add("chat-line");

            var timeContainer = document.createElement("div");
            timeContainer.classList.add("time-container");
                var time = document.createElement("p");
                time.classList.add("time");
                time.innerText = Utils.formatTime(node.contentOffsetSeconds);

            timeContainer.appendChild(time);

            var contentContainer = document.createElement("div");
            contentContainer.classList.add("content-container");
                var username = document.createElement("span");
                username.classList.add("username");
                username.style.color = node.message.userColor;
                username.innerText = node.commenter.displayName;
                var message = this.getMessageFromFragments(node.message.fragments);

            contentContainer.appendChild(username);
            contentContainer.appendChild(message);

        chatLine.appendChild(timeContainer);
        chatLine.appendChild(contentContainer);

        return chatLine;
    }

    static getMessageFromFragments(fragments) {
        var message = document.createElement("div");
        message.classList.add("message");

        var columnsTextSpan = Utils.createTextSpan(":");
        columnsTextSpan.style.paddingRight = "0.5rem";

        message.appendChild(columnsTextSpan);

        for(var i = 0; i < fragments.length; i++) {
            if (fragments[i].emote != null) {
                message.appendChild(this.getEmoteFromId(fragments[i].emote.emoteID));
            } else {
                message.appendChild(Utils.createTextSpan(fragments[i].text));
            }
        }
        return message;
    }

    static getEmoteFromId(emoteId) {
        // create the element <span><div class="chat-image-container"><img src="https://static-cdn.jtvnw.net/emoticons/v2/' + emoteId + '/default/dark/1.0"></div></span>
        var emote = document.createElement("span");

        var div = document.createElement("div");
        div.classList.add("chat-image-container");

        var img = document.createElement("img");
        img.src = "https://static-cdn.jtvnw.net/emoticons/v2/" + emoteId + "/default/dark/1.0";
        
        div.appendChild(img);
        emote.appendChild(div);

        return emote;
    }

    getTimeDiffFromStartInSec(time) {
        var parsedTime = Date.parse(time);
        var diff = parsedTime - this.startTime;

        return diff / 1000;
    }

    async getChatFromSecOffset(secOffset) {
        var query = this.getSecOffsetQuery(secOffset);
        var response = await this.makeRequest(query);
        return response;

        // var chat = this.parseResponse(response);
        // return chat;
    }

    async getChatFromCursorOffset(cursor) {
        var query = this.getCursorOffsetQuery(cursor);
        var response = await this.makeRequest(query);
        return response;

        // var chat = this.parseResponse(response);
        // return chat;
    }

    getCursorOffsetQuery(cursor) {
        var query = {
            "operationName": "VideoCommentsByOffsetOrCursor",
            "variables": {
                "videoID": this.videoID,
                "cursor": cursor
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a"
                }
            }
        };
        return query;
    }

    getSecOffsetQuery(secOffset) {
        var query = {
            "operationName": "VideoCommentsByOffsetOrCursor",
            "variables": {
                "videoID": this.videoID,
                "contentOffsetSeconds": secOffset
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a"
                }
            }
        };
        return query;
    }

    async makeRequest(query) {
        var response = await fetch(this.twitchApiUrl, {
            method: 'POST',
            headers: this.twitchApiHeaders,
            body: JSON.stringify(query)
        });
        return response.json();
    }

    async getMessagesFromSecOffset(secOffset) {
        var json = await this.getChatFromSecOffset(secOffset);

        for(var i = 0; i < json.data.video.comments.edges.length; i++) {
            var node = json.data.video.comments.edges[i].node;

            var messageTimestamp = chatGetter.getTimeDiffFromStartInSec(node.createdAt.replace("Z", "").replace("T", " "));
            var chatElement = ChatGetter.createChatElement(node);

            this.messages.push({
                "cursor": json.data.video.comments.edges[i].cursor,
                "timestamp": messageTimestamp,
                "element": chatElement
            });
        }
    }

    async getMessagesFromCursorOffset(cursorOffset) {
        var json = await this.getChatFromCursorOffset(cursorOffset);

        for(var i = 0; i < json.data.video.comments.edges.length; i++) {
            var node = json.data.video.comments.edges[i].node;

            var messageTimestamp = chatGetter.getTimeDiffFromStartInSec(node.createdAt.replace("Z", "").replace("T", " "));
            var chatElement = ChatGetter.createChatElement(node);

            this.messages.push({
                "cursor": json.data.video.comments.edges[i].cursor,
                "timestamp": messageTimestamp,
                "element": chatElement
            });
        }
    }

    async getNextMessages(videoTime) {
        if (this.messages.length == 0 || this.messages[this.messages.length - 1].time < videoTime) {
            await this.getMessagesFromSecOffset(Math.floor(videoTime));
        }

        var nextMessages = [];
        this.messages.forEach(message => {
            var leftBorder = videoTime - this.videoUpdateTime/2;
            var rightBorder = videoTime + this.videoUpdateTime/2;
            if (leftBorder <= message.timestamp && message.timestamp <= rightBorder) {
                // console.log("message time: " + message.timestamp + " leftBorder: " + leftBorder + " rightBorder: " + rightBorder);
                nextMessages.push(message.element);
            }
        });

        await this.updateMessages(videoTime);

        return nextMessages;
    }

    async updateMessages(videoTime) {
        // console.log("video time: " + videoTime + " mesages length before filter: " + this.messages.length);

        this.messages = this.messages.filter(message => {
            return message.timestamp > videoTime ;
        });

        if (this.messages.length == 0) {
            await this.getMessagesFromSecOffset(Math.floor(videoTime));
        }

        if (this.messages.length <= 30 && !this.isUpdating) {
            this.isUpdating = true;
            console.log("video time: " + videoTime + " messages length: " + this.messages.length);
            var cursor = this.messages[this.messages.length - 1].cursor;
            await this.getMessagesFromCursorOffset(cursor);
            this.isUpdating = false;
        }

        // console.log("video time: " + videoTime + " messages length: " + this.messages.length + " isUpdating: " + this.isUpdating);
    }
}