var video = document.getElementById('video');

function playM3u8(url){
  if(Hls.isSupported()) {
      video.volume = 0.3;
      var hls = new Hls();
      var m3u8Url = decodeURIComponent(url)
      hls.loadSource(m3u8Url);
      hls.attachMedia(video);
    //   hls.on(Hls.Events.MANIFEST_PARSED,function() {
    //     video.play();
    //   });
      document.title = url
    }
	else if (video.canPlayType('application/vnd.apple.mpegurl')) {
		video.src = url;
		video.addEventListener('canplay',function() {
		  video.play();
		});
		video.volume = 0.3;
		document.title = url;
  	}
}

function playPause() {
    video.paused?video.play():video.pause();
    console.log("playPause");
}

function volumeUp() {
    if(video.volume <= 0.9) video.volume+=0.1;
    console.log("volumeUp");
}

function volumeDown() {
    if(video.volume >= 0.1) video.volume-=0.1;
    console.log("volumeDown");
}

function seekRight() {
    video.currentTime+=5;
    console.log("seekRight");
}

function seekLeft() {
    video.currentTime-=5;
    console.log("seekLeft");
}

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

    video.currentTime = seconds;
    console.log("seekTime");
}

function vidFullscreen() {
    if (video.requestFullscreen) {
      video.requestFullscreen();
    } else if (video.mozRequestFullScreen) {
        video.mozRequestFullScreen();
    } else if (video.webkitRequestFullscreen) {
        video.webkitRequestFullscreen();
    }
}

playM3u8(window.location.href.split("#")[1])
$(window).on('load', function () {
    // $('#video').on('click', function(){this.paused?this.play():this.pause();});
    // Mousetrap.bind('space', playPause);
    // Mousetrap.bind('up', volumeUp);
    // Mousetrap.bind('down', volumeDown);
    // Mousetrap.bind('right', seekRight);
    // Mousetrap.bind('left', seekLeft);
    // Mousetrap.bind('f', vidFullscreen);
    Mousetrap.bind('s', seekTime);
});
