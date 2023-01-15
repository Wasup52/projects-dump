class ChatGetter {
    twitchApiUrl = "https://gql.twitch.tv/gql";
    twitchApiHeaders = {
        "Client-Id" : "kimne78kx3ncx6brgo4mv6wki5h1ko", // this is the client id of the twitch web app
    };

    constructor(videoID) {
        this.videoID = videoID;
    }

    static createChatElement(node) {
        var chatLine = document.createElement("li");
        chatLine.classList.add("chat-line");

            var timeContainer = document.createElement("div");
            timeContainer.classList.add("time-container");
                var time = document.createElement("p");
                time.classList.add("time");
                time.innerText = node.createdAt;

            timeContainer.appendChild(time);

            var contentContainer = document.createElement("div");
            contentContainer.classList.add("content-container");
                var username = document.createElement("span");
                username.classList.add("username");
                username.innerText = node.commenter.displayName;
                var message = document.createElement("div");
                message.classList.add("message");
                var messageContent = this.getMessageFromFragments(node.message.fragments);

            contentContainer.appendChild(username);
            contentContainer.appendChild(message);

        chatLine.appendChild(timeContainer);
        chatLine.appendChild(contentContainer);

        return chatLine;
    }

    static getMessageFromFragments(fragments) {
        var message = createElement("span");
        message.innerText = ": ";
        for(var i = 0; i < fragments.length; i++) {
            if (fragments[i].emote != null) {
                message += this.getEmoteFromId(fragments[i].emote.emoteID);
            } else {
                message += fragments[i].text;
            }
        }
        return message;
    }

    static getEmoteFromId(emoteId) {
        // create the element <span><img src="https://static-cdn.jtvnw.net/emoticons/v2/' + emoteId + '/default/dark/1.0"></span>
        var emote = document.createElement("span");
        var emoteImg = document.createElement("img");
        emoteImg.src = "https://static-cdn.jtvnw.net/emoticons/v2/" + emoteId + "/default/dark/1.0";
        emote.appendChild(emoteImg);
    }

    async getChatFromSecOffset(secOffset) {
        var query = this.getSecOffsetQuery(secOffset);
        console.log(query);
        var response = await this.makeRequest(query);
        return response;

        // var chat = this.parseResponse(response);
        // return chat;
    }

    getChatFromCursorOffset(cursor) {
        var query = this.getCursorOffsetQuery(cursor);
        var response = this.makeRequest(query);
        return response;

        // var chat = this.parseResponse(response);
        // return chat;
    }

    getCursorOffsetQuery(cursor) {
        var query = {
            "operationName": "VideoChatReplay",
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
}