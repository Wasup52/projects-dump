var video = document.getElementById('video');
var chatListContainer = document.getElementById('chat-list-container');
var chatWrapper = document.getElementById('chat-wrapper');
var chatGetter = new ChatGetter("1602009987", "2022-09-26 17:51:25");

var testResponse = [
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "5904b3f7-6fc1-4b2a-92a7-80b8c0f3bf5f",
            "commenter": {
                "id": "142519043",
                "login": "jlwalien",
                "displayName": "JLWALIEN",
                "__typename": "User"
            },
            "contentOffsetSeconds": 3,
            "createdAt": "2022-09-26T17:51:28.789Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "lets gooooo",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FFFFFF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "5524202d-013b-49ce-ba2f-8554fc81fe82",
            "commenter": {
                "id": "270085496",
                "login": "orouu",
                "displayName": "Orouu",
                "__typename": "User"
            },
            "contentOffsetSeconds": 4,
            "createdAt": "2022-09-26T17:51:29.825Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "ZEN",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "YXJ0aXN0LWJhZGdlOzE7",
                        "setID": "artist-badge",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#B5FFFC",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "bce463e6-ef74-4372-b861-98e58217dffc",
            "commenter": {
                "id": "788444461",
                "login": "tomhollandgoat",
                "displayName": "tomhollandgoat",
                "__typename": "User"
            },
            "contentOffsetSeconds": 5,
            "createdAt": "2022-09-26T17:51:30.948Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "oooh",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjszOw==",
                        "setID": "subscriber",
                        "version": "3",
                        "__typename": "Badge"
                    },
                    {
                        "id": "Z2xoZi1wbGVkZ2U7MTs=",
                        "setID": "glhf-pledge",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#F9FF00",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "b19687fe-27bf-453d-ac1b-3869532629f2",
            "commenter": {
                "id": "142519043",
                "login": "jlwalien",
                "displayName": "JLWALIEN",
                "__typename": "User"
            },
            "contentOffsetSeconds": 6,
            "createdAt": "2022-09-26T17:51:32.406Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "zen",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FFFFFF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "a0d0a4d0-fcc8-4e0f-aa63-25085806e3e7",
            "commenter": {
                "id": "156772389",
                "login": "vide0club",
                "displayName": "VIDE0CLUB",
                "__typename": "User"
            },
            "contentOffsetSeconds": 6,
            "createdAt": "2022-09-26T17:51:32.507Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "SHEEESH",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjszOw==",
                        "setID": "subscriber",
                        "version": "3",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#E9E099",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "5e95fab3-1eba-417e-a91f-03eb3c9135d7",
            "commenter": {
                "id": "674686955",
                "login": "lydoz_",
                "displayName": "Lydoz_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 6,
            "createdAt": "2022-09-26T17:51:32.521Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "ouaiiiis",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#B22222",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "7c833d72-61f9-4039-b69d-e1f7732d04e6",
            "commenter": {
                "id": "454419747",
                "login": "karimgoatzer",
                "displayName": "karimgoatzer",
                "__typename": "User"
            },
            "contentOffsetSeconds": 8,
            "createdAt": "2022-09-26T17:51:33.914Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FlopkujowFlopkujowFlopkujow",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FF7F50",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "9acd5357-32bd-4323-959f-d8596eb16b86",
            "commenter": {
                "id": "159783999",
                "login": "grayturtles",
                "displayName": "GrayTurtles",
                "__typename": "User"
            },
            "contentOffsetSeconds": 9,
            "createdAt": "2022-09-26T17:51:34.925Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "POGGERS",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#00E4FF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "a8fb2c15-0e4d-460f-a793-6bf1f27b5cdd",
            "commenter": {
                "id": "247929494",
                "login": "lytike_",
                "displayName": "lytike_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 10,
            "createdAt": "2022-09-26T17:51:35.748Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "oeeeeeeeeeee",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#DAA520",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "9ecea350-cce5-4dc9-929d-1c529240b577",
            "commenter": {
                "id": "788444461",
                "login": "tomhollandgoat",
                "displayName": "tomhollandgoat",
                "__typename": "User"
            },
            "contentOffsetSeconds": 10,
            "createdAt": "2022-09-26T17:51:35.932Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "SHEEEEEEEEEESH",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjszOw==",
                        "setID": "subscriber",
                        "version": "3",
                        "__typename": "Badge"
                    },
                    {
                        "id": "Z2xoZi1wbGVkZ2U7MTs=",
                        "setID": "glhf-pledge",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#F9FF00",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "24332b1e-765d-4d25-803f-4958b1c6b1b7",
            "commenter": {
                "id": "464026762",
                "login": "shunsuii_",
                "displayName": "Shunsuii_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 10,
            "createdAt": "2022-09-26T17:51:36.666Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FLOPKUJOOOW",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bm9fdmlkZW87MTs=",
                        "setID": "no_video",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#22A9B2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "f75f9984-c819-478f-bb67-abd8329ea390",
            "commenter": {
                "id": "543831426",
                "login": "friget_koelkast",
                "displayName": "Friget_Koelkast",
                "__typename": "User"
            },
            "contentOffsetSeconds": 11,
            "createdAt": "2022-09-26T17:51:37.178Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "ça commence !!!!!!",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#8A2BE2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "f06d5c31-3219-4aa5-abc7-db6154715263",
            "commenter": {
                "id": "142519043",
                "login": "jlwalien",
                "displayName": "JLWALIEN",
                "__typename": "User"
            },
            "contentOffsetSeconds": 13,
            "createdAt": "2022-09-26T17:51:39.332Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "tout lmonde tout lmonde est zen",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FFFFFF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "f82f36e3-0b1a-4c24-a22f-77f2d1a448a4",
            "commenter": {
                "id": "114544471",
                "login": "popochounet",
                "displayName": "popochounet",
                "__typename": "User"
            },
            "contentOffsetSeconds": 14,
            "createdAt": "2022-09-26T17:51:40.522Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "OH LA DINGZ",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#8A2BE2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "812fdd5a-40dc-43f7-9841-340e249e8de9",
            "commenter": {
                "id": "462359338",
                "login": "jamydumonde",
                "displayName": "jamydumonde",
                "__typename": "User"
            },
            "contentOffsetSeconds": 14,
            "createdAt": "2022-09-26T17:51:40.558Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "sheeeeeeeeeesh",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bW9kZXJhdG9yOzE7",
                        "setID": "moderator",
                        "version": "1",
                        "__typename": "Badge"
                    },
                    {
                        "id": "Zm91bmRlcjswOw==",
                        "setID": "founder",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "c3ViLWdpZnRlcjsyNTs=",
                        "setID": "sub-gifter",
                        "version": "25",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#00FF7F",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "38371e0a-da4e-46d4-abc9-2d90a7d0e730",
            "commenter": {
                "id": "565424736",
                "login": "fatfatine",
                "displayName": "fatfatine",
                "__typename": "User"
            },
            "contentOffsetSeconds": 16,
            "createdAt": "2022-09-26T17:51:41.888Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FF69B4",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "13d72e9c-50c0-43d7-a248-11723fb52b27",
            "commenter": {
                "id": "454419747",
                "login": "karimgoatzer",
                "displayName": "karimgoatzer",
                "__typename": "User"
            },
            "contentOffsetSeconds": 16,
            "createdAt": "2022-09-26T17:51:42.56Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Flopkujow Sadge",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FF7F50",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "5323b33a-e7bf-4a8c-9533-524e6e1dce24",
            "commenter": {
                "id": "733285890",
                "login": "ninlgamma",
                "displayName": "ninlgamma",
                "__typename": "User"
            },
            "contentOffsetSeconds": 18,
            "createdAt": "2022-09-26T17:51:44.603Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Avec CYPRIEN",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FF0000",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "639c647d-35ff-40d9-ae04-d53fa8a22109",
            "commenter": {
                "id": "247929494",
                "login": "lytike_",
                "displayName": "lytike_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 23,
            "createdAt": "2022-09-26T17:51:49.292Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FLOP KOJOW",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#DAA520",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "65d63253-0e08-473b-b149-7c4e83ddd091",
            "commenter": {
                "id": "131529726",
                "login": "vitaze_",
                "displayName": "vitaze_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 23,
            "createdAt": "2022-09-26T17:51:49.484Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "hey",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#1E90FF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "1240fa20-ab28-468d-903c-346ca4c5b57f",
            "commenter": {
                "id": "78338756",
                "login": "gienco",
                "displayName": "Gienco",
                "__typename": "User"
            },
            "contentOffsetSeconds": 24,
            "createdAt": "2022-09-26T17:51:49.954Z",
            "message": {
                "fragments": [
                    {
                        "emote": {
                            "id": "emotesv2_ecbe45519c3445a08c5157cc369bf7aa;0;9",
                            "emoteID": "emotesv2_ecbe45519c3445a08c5157cc369bf7aa",
                            "from": 0,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "MaximeRave",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_c62b0024999c4049a0f49f375e25c5d1;11;18",
                            "emoteID": "emotesv2_c62b0024999c4049a0f49f375e25c5d1",
                            "from": 11,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "grimkJam",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_b23473e041924b6e931dd22521231ccf;20;29",
                            "emoteID": "emotesv2_b23473e041924b6e931dd22521231ccf",
                            "from": 20,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "hugoDanse2",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_6485c1664da7405db99ee312f961c143;31;48",
                            "emoteID": "emotesv2_6485c1664da7405db99ee312f961c143",
                            "from": 31,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "madrozDoubleLogobi",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_ecbe45519c3445a08c5157cc369bf7aa;50;59",
                            "emoteID": "emotesv2_ecbe45519c3445a08c5157cc369bf7aa",
                            "from": 50,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "MaximeRave",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_c62b0024999c4049a0f49f375e25c5d1;61;68",
                            "emoteID": "emotesv2_c62b0024999c4049a0f49f375e25c5d1",
                            "from": 61,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "grimkJam",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_b23473e041924b6e931dd22521231ccf;70;79",
                            "emoteID": "emotesv2_b23473e041924b6e931dd22521231ccf",
                            "from": 70,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "hugoDanse2",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_6485c1664da7405db99ee312f961c143;81;98",
                            "emoteID": "emotesv2_6485c1664da7405db99ee312f961c143",
                            "from": 81,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "madrozDoubleLogobi",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_ecbe45519c3445a08c5157cc369bf7aa;100;109",
                            "emoteID": "emotesv2_ecbe45519c3445a08c5157cc369bf7aa",
                            "from": 100,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "MaximeRave",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_c62b0024999c4049a0f49f375e25c5d1;111;118",
                            "emoteID": "emotesv2_c62b0024999c4049a0f49f375e25c5d1",
                            "from": 111,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "grimkJam",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_b23473e041924b6e931dd22521231ccf;120;129",
                            "emoteID": "emotesv2_b23473e041924b6e931dd22521231ccf",
                            "from": 120,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "hugoDanse2",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": null,
                        "text": " ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_6485c1664da7405db99ee312f961c143;131;148",
                            "emoteID": "emotesv2_6485c1664da7405db99ee312f961c143",
                            "from": 131,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "madrozDoubleLogobi",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bW9kZXJhdG9yOzE7",
                        "setID": "moderator",
                        "version": "1",
                        "__typename": "Badge"
                    },
                    {
                        "id": "Z2xoZi1wbGVkZ2U7MTs=",
                        "setID": "glhf-pledge",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FFFFFF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "194a7fb3-b776-49ff-ae42-4684896a1662",
            "commenter": {
                "id": "733295541",
                "login": "nathan_bvb",
                "displayName": "nathan_bvb",
                "__typename": "User"
            },
            "contentOffsetSeconds": 27,
            "createdAt": "2022-09-26T17:51:53.186Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Flop kujow",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "79db1d98-4e03-4f4d-aadd-ed3681c86666",
            "commenter": {
                "id": "543831426",
                "login": "friget_koelkast",
                "displayName": "Friget_Koelkast",
                "__typename": "User"
            },
            "contentOffsetSeconds": 31,
            "createdAt": "2022-09-26T17:51:57.426Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FLOPKUJOW",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#8A2BE2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "82d31065-28c1-493a-90ec-b53c76cb6408",
            "commenter": {
                "id": "800401368",
                "login": "ly0a",
                "displayName": "ly0a",
                "__typename": "User"
            },
            "contentOffsetSeconds": 32,
            "createdAt": "2022-09-26T17:51:58.606Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "zen",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#DAA520",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "10826a72-da08-4c83-90f9-63405df77f42",
            "commenter": {
                "id": "454419747",
                "login": "karimgoatzer",
                "displayName": "karimgoatzer",
                "__typename": "User"
            },
            "contentOffsetSeconds": 34,
            "createdAt": "2022-09-26T17:52:00.078Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Pour ceux qui savent pas, grim est mort, F Flopkujow Sadge",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FF7F50",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "0fcedf54-cd31-434b-9180-6857e4eb1e61",
            "commenter": {
                "id": "78338756",
                "login": "gienco",
                "displayName": "Gienco",
                "__typename": "User"
            },
            "contentOffsetSeconds": 36,
            "createdAt": "2022-09-26T17:52:02.083Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "DRRRRRRRRRRRAAAAAAAAAAAAA ah non c pas le bon",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bW9kZXJhdG9yOzE7",
                        "setID": "moderator",
                        "version": "1",
                        "__typename": "Badge"
                    },
                    {
                        "id": "Z2xoZi1wbGVkZ2U7MTs=",
                        "setID": "glhf-pledge",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FFFFFF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "abab1540-9e05-4477-863b-561199a9e18c",
            "commenter": {
                "id": "227922728",
                "login": "koqtel_",
                "displayName": "KoqTel_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 37,
            "createdAt": "2022-09-26T17:52:03.163Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "NARMOL ",
                        "__typename": "VideoCommentMessageFragment"
                    },
                    {
                        "emote": {
                            "id": "emotesv2_28477589b3fd4b6fa52ada10bc4e867b;7;17",
                            "emoteID": "emotesv2_28477589b3fd4b6fa52ada10bc4e867b",
                            "from": 7,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "madrozPhoto",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bm9fYXVkaW87MTs=",
                        "setID": "no_audio",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#DAA520",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "489f817e-cc6e-4291-9070-791384b551de",
            "commenter": {
                "id": "190475306",
                "login": "djgalettesansfrangipane",
                "displayName": "DJgaletteSansFrangipane",
                "__typename": "User"
            },
            "contentOffsetSeconds": 37,
            "createdAt": "2022-09-26T17:52:03.558Z",
            "message": {
                "fragments": [
                    {
                        "emote": {
                            "id": "306349075;0;11",
                            "emoteID": "306349075",
                            "from": 0,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "etienn7CATUE",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FF4500",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "cb20feb4-6571-4c77-8013-36284a8c65cb",
            "commenter": {
                "id": "733295541",
                "login": "nathan_bvb",
                "displayName": "nathan_bvb",
                "__typename": "User"
            },
            "contentOffsetSeconds": 39,
            "createdAt": "2022-09-26T17:52:04.729Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "dans le chat",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "e9b77ad8-1ad3-4b4b-99a8-cae508db7e35",
            "commenter": {
                "id": "733285890",
                "login": "ninlgamma",
                "displayName": "ninlgamma",
                "__typename": "User"
            },
            "contentOffsetSeconds": 39,
            "createdAt": "2022-09-26T17:52:05.083Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "catJAM",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FF0000",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "eb7af4c3-e868-430e-ac94-95eb0a8b8ccc",
            "commenter": {
                "id": "451816162",
                "login": "r4p1d0_11",
                "displayName": "r4p1d0_11",
                "__typename": "User"
            },
            "contentOffsetSeconds": 41,
            "createdAt": "2022-09-26T17:52:07.611Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "ZEEZEEEEEENNNNN",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "29cd5c6f-5768-4bee-bbce-b9e493f36a7f",
            "commenter": {
                "id": "733295541",
                "login": "nathan_bvb",
                "displayName": "nathan_bvb",
                "__typename": "User"
            },
            "contentOffsetSeconds": 42,
            "createdAt": "2022-09-26T17:52:08.209Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "ça spammait",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "a3d48208-3448-4c18-be34-3f468eb967ee",
            "commenter": {
                "id": "464026762",
                "login": "shunsuii_",
                "displayName": "Shunsuii_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 42,
            "createdAt": "2022-09-26T17:52:08.472Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bm9fdmlkZW87MTs=",
                        "setID": "no_video",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#22A9B2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "d94af5e1-a339-463a-9b2b-ffd97d05f03b",
            "commenter": {
                "id": "142519043",
                "login": "jlwalien",
                "displayName": "JLWALIEN",
                "__typename": "User"
            },
            "contentOffsetSeconds": 43,
            "createdAt": "2022-09-26T17:52:09.153Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "flopkujow",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FFFFFF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "af064ec4-9cb4-4868-9d21-cdb2a217d237",
            "commenter": {
                "id": "543831426",
                "login": "friget_koelkast",
                "displayName": "Friget_Koelkast",
                "__typename": "User"
            },
            "contentOffsetSeconds": 45,
            "createdAt": "2022-09-26T17:52:11.222Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FLOPKUJOW !",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#8A2BE2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "ec412d30-25e2-4139-8234-20c64c2f5df4",
            "commenter": {
                "id": "98552625",
                "login": "yadcsen",
                "displayName": "Yadcsen",
                "__typename": "User"
            },
            "contentOffsetSeconds": 48,
            "createdAt": "2022-09-26T17:52:13.901Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Betty ma princesse",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FF0000",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "83a70186-5e41-44e9-8863-2948115d5dd8",
            "commenter": {
                "id": "131225267",
                "login": "big_nico",
                "displayName": "big_nico",
                "__typename": "User"
            },
            "contentOffsetSeconds": 48,
            "createdAt": "2022-09-26T17:52:14.473Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "CC",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#8A2BE2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "8743abc6-3a4d-40a9-bb19-c1eda244e462",
            "commenter": {
                "id": "247929494",
                "login": "lytike_",
                "displayName": "lytike_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 49,
            "createdAt": "2022-09-26T17:52:15.074Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "flopkujow",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#DAA520",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "f33fad4f-4c54-4c1a-8f16-633d74ee8d51",
            "commenter": {
                "id": "160111109",
                "login": "alboz__",
                "displayName": "ALBOZ__",
                "__typename": "User"
            },
            "contentOffsetSeconds": 49,
            "createdAt": "2022-09-26T17:52:15.353Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "pipi",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "a242ff78-c048-4fcf-9120-435432432abc",
            "commenter": {
                "id": "37273683",
                "login": "projet19",
                "displayName": "projet19",
                "__typename": "User"
            },
            "contentOffsetSeconds": 50,
            "createdAt": "2022-09-26T17:52:15.739Z",
            "message": {
                "fragments": [
                    {
                        "emote": {
                            "id": "emotesv2_8098e37bc383472aa5efbc824bc2b613;0;7",
                            "emoteID": "emotesv2_8098e37bc383472aa5efbc824bc2b613",
                            "from": 0,
                            "__typename": "EmbeddedEmote"
                        },
                        "text": "zrtDance",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#008000",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "720d0650-f3ae-4050-8157-0ebc2f56ecfd",
            "commenter": {
                "id": "733285890",
                "login": "ninlgamma",
                "displayName": "ninlgamma",
                "__typename": "User"
            },
            "contentOffsetSeconds": 51,
            "createdAt": "2022-09-26T17:52:16.714Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "MaxRave",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FF0000",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "6e6d05e1-94b6-4a5e-b2eb-fe48cb6a6497",
            "commenter": {
                "id": "159783999",
                "login": "grayturtles",
                "displayName": "GrayTurtles",
                "__typename": "User"
            },
            "contentOffsetSeconds": 55,
            "createdAt": "2022-09-26T17:52:21.057Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Flopkujow Sadge GuitarTime",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#00E4FF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "cb4b1a01-7fd7-42de-94ed-5216b561af5e",
            "commenter": {
                "id": "800401368",
                "login": "ly0a",
                "displayName": "ly0a",
                "__typename": "User"
            },
            "contentOffsetSeconds": 56,
            "createdAt": "2022-09-26T17:52:22.635Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "flopkujow",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#DAA520",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "3114d6f0-8a31-4078-bf67-5daf132ca8a5",
            "commenter": {
                "id": "191848104",
                "login": "kc_thonpaire",
                "displayName": "kc_thonpaire",
                "__typename": "User"
            },
            "contentOffsetSeconds": 57,
            "createdAt": "2022-09-26T17:52:22.915Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FLOPKUJOW",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "4cb9f2a6-f5a4-47e2-af4e-0631effa3fb9",
            "commenter": {
                "id": "24378859",
                "login": "dhieen",
                "displayName": "DHIEEN",
                "__typename": "User"
            },
            "contentOffsetSeconds": 69,
            "createdAt": "2022-09-26T17:52:34.936Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "first",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "2a1c319a-d753-4169-bc90-62cff81daf72",
            "commenter": {
                "id": "543831426",
                "login": "friget_koelkast",
                "displayName": "Friget_Koelkast",
                "__typename": "User"
            },
            "contentOffsetSeconds": 75,
            "createdAt": "2022-09-26T17:52:41.698Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FLOPKUJOW",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#8A2BE2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "051bb5b0-175b-458a-827c-24537ceafef3",
            "commenter": {
                "id": "641312245",
                "login": "bouloumm",
                "displayName": "bouloumm",
                "__typename": "User"
            },
            "contentOffsetSeconds": 76,
            "createdAt": "2022-09-26T17:52:41.769Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "fist",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "Z2xoZi1wbGVkZ2U7MTs=",
                        "setID": "glhf-pledge",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#B22222",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "36edbbe7-c892-472a-9718-52bdeac5e8b7",
            "commenter": {
                "id": "227922728",
                "login": "koqtel_",
                "displayName": "KoqTel_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 77,
            "createdAt": "2022-09-26T17:52:43.026Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "POURQUOI ? 🤨 PepeHands",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bm9fYXVkaW87MTs=",
                        "setID": "no_audio",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#DAA520",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "e019197c-6d93-4628-81ac-1e6f20559f17",
            "commenter": {
                "id": "524626257",
                "login": "boccace",
                "displayName": "boccace",
                "__typename": "User"
            },
            "contentOffsetSeconds": 78,
            "createdAt": "2022-09-26T17:52:43.955Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "@DHIEEN tg",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "d4416c8f-53c1-4249-b3c4-f435dd88a5a8",
            "commenter": {
                "id": "163758555",
                "login": "enoratonlaveur",
                "displayName": "Enoratonlaveur",
                "__typename": "User"
            },
            "contentOffsetSeconds": 83,
            "createdAt": "2022-09-26T17:52:49.49Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Bonsoir, tous heureux de retrouver Zen",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#A297A5",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "6162528a-5e6d-4a9d-b8ef-ec47bbc65883",
            "commenter": {
                "id": "693283059",
                "login": "vinceberard54",
                "displayName": "vinceberard54",
                "__typename": "User"
            },
            "contentOffsetSeconds": 84,
            "createdAt": "2022-09-26T17:52:50.411Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "yo",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "054b3fed-ad96-41fb-8a1b-7e77cf441142",
            "commenter": {
                "id": "464026762",
                "login": "shunsuii_",
                "displayName": "Shunsuii_",
                "__typename": "User"
            },
            "contentOffsetSeconds": 88,
            "createdAt": "2022-09-26T17:52:53.956Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bm9fdmlkZW87MTs=",
                        "setID": "no_video",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#22A9B2",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "95e997d0-5e65-4548-9b24-c7308113c67f",
            "commenter": {
                "id": "24378859",
                "login": "dhieen",
                "displayName": "DHIEEN",
                "__typename": "User"
            },
            "contentOffsetSeconds": 90,
            "createdAt": "2022-09-26T17:52:56.424Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "ca va etre un classique ce soir",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "d3c5d670-72cc-4729-8900-52c0a32d064f",
            "commenter": {
                "id": "454419747",
                "login": "karimgoatzer",
                "displayName": "karimgoatzer",
                "__typename": "User"
            },
            "contentOffsetSeconds": 93,
            "createdAt": "2022-09-26T17:52:59.388Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Flopkujow Flopkujow Flopkujow Flopkujow",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "c3Vic2NyaWJlcjswOw==",
                        "setID": "subscriber",
                        "version": "0",
                        "__typename": "Badge"
                    },
                    {
                        "id": "cHJlbWl1bTsxOw==",
                        "setID": "premium",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FF7F50",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "5bdc72b9-dc25-4ce4-9c27-d0b10df42046",
            "commenter": {
                "id": "733285890",
                "login": "ninlgamma",
                "displayName": "ninlgamma",
                "__typename": "User"
            },
            "contentOffsetSeconds": 96,
            "createdAt": "2022-09-26T17:53:01.786Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse MaxRave MaxDanse",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": "#FF0000",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "d80368b9-dd8c-4c10-a157-99f6c2ec0e15",
            "commenter": {
                "id": "403776678",
                "login": "cest_cocom_wsh",
                "displayName": "Cest_Cocom_Wsh",
                "__typename": "User"
            },
            "contentOffsetSeconds": 97,
            "createdAt": "2022-09-26T17:53:03.155Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "OUAIS",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "Yml0czsxOw==",
                        "setID": "bits",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FF69B4",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "44f54ea6-5383-4991-b7e2-ef2573af6d98",
            "commenter": {
                "id": "641312245",
                "login": "bouloumm",
                "displayName": "bouloumm",
                "__typename": "User"
            },
            "contentOffsetSeconds": 98,
            "createdAt": "2022-09-26T17:53:04.627Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge FLOPKUJOW Sadge",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "Z2xoZi1wbGVkZ2U7MTs=",
                        "setID": "glhf-pledge",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#B22222",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "7828d9a1-ba85-4f76-b4d6-9f4a12f254ec",
            "commenter": {
                "id": "78338756",
                "login": "gienco",
                "displayName": "Gienco",
                "__typename": "User"
            },
            "contentOffsetSeconds": 100,
            "createdAt": "2022-09-26T17:53:05.877Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "!game talk show",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [
                    {
                        "id": "bW9kZXJhdG9yOzE7",
                        "setID": "moderator",
                        "version": "1",
                        "__typename": "Badge"
                    },
                    {
                        "id": "Z2xoZi1wbGVkZ2U7MTs=",
                        "setID": "glhf-pledge",
                        "version": "1",
                        "__typename": "Badge"
                    }
                ],
                "userColor": "#FFFFFF",
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    },
    {
        "cursor": "eyJpZCI6IjEzZmQ2MzI3LTVmZmItNGY0MS1hOTdhLTdkZmVlNDE5NWZiMyIsImhrIjoiYnJvYWRjYXN0OjQ2MTA4ODIwMjUyIiwic2siOiJBQUFBRjJfYzkwQVhHSHFINHdBQVFBIn0",
        "node": {
            "id": "13fd6327-5ffb-4f41-a97a-7dfee4195fb3",
            "commenter": {
                "id": "552653463",
                "login": "grg1476",
                "displayName": "grg1476",
                "__typename": "User"
            },
            "contentOffsetSeconds": 100,
            "createdAt": "2022-09-26T17:53:06.361Z",
            "message": {
                "fragments": [
                    {
                        "emote": null,
                        "text": "Flopkujow",
                        "__typename": "VideoCommentMessageFragment"
                    }
                ],
                "userBadges": [],
                "userColor": null,
                "__typename": "VideoCommentMessage"
            },
            "__typename": "VideoComment"
        },
        "__typename": "VideoCommentEdge"
    }
]


async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// chatGetter.getChatFromSecOffset(0).then((json) => {
//     var edges = json.data.video.comments.edges;
//     console.log(edges);

//     edges.forEach(async (edge) => {
//         var chatElement = ChatGetter.createChatElement(edge.node);

//         await sleep(1000);

//         var lastChatElement = chatListContainer.getElementsByClassName("last")[0];
//         if (lastChatElement) {
//             lastChatElement.classList.remove("last");
//         }
//         chatElement.classList.add("last");

//         chatListContainer.appendChild(chatElement);
//     });
    
//     cursor = json.data.video.comments.pageInfo.endCursor;
// });

// var messages = []

// var edges = testResponse;
// count = 0;
// edges.forEach(async (edge) => {
//     var messageTimestamp = chatGetter.getTimeDiffFromStartInSec(edge.node.createdAt.replace("Z", "").replace("T", " "));
//     var chatElement = ChatGetter.createChatElement(edge.node);

//     messages.push({
//         "timestamp": messageTimestamp,
//         "element": chatElement
//     });
// });

// console.log(messages);

// var times = [];
// var timeIntervals = [];

if (video != null) {
    video.addEventListener('timeupdate', async function() { // average update time is 0.260 seconds (4 times per second)
        var currentTime = video.currentTime;

        // get the next message only if we got the previous one
        if (chatGetter.messages.length > 0 && chatGetter.messages[0].timestamp <= currentTime) {
            chatGetter.getNextMessages(currentTime).then((nextMessages) => {
                if (nextMessages.length != 0) {
                    nextMessages.forEach((nextMessage) => {
    
                        chatListContainer.appendChild(nextMessage);
                        
                        chatListContainer.scrollTop = chatListContainer.scrollHeight; // scroll to bottom
                    });
                }
            });
        }

    });
}

// var agerageTimeInterval = 0;
// timeIntervals.forEach((timeInterval) => {
//     agerageTimeInterval += timeInterval;
// });
// agerageTimeInterval /= timeIntervals.length;
