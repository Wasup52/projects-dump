class Utils {

    static formatTime(seconds) {
        var hours = Math.floor(seconds / 3600);
        var minutes = Math.floor((seconds - (hours * 3600)) / 60);
        var seconds = Math.floor(seconds - (hours * 3600) - (minutes * 60));
        var time = "";
        if (hours != 0) {
            time = hours+":";
        }
        time += minutes<10?"0"+minutes:minutes;
        time += ":";
        time += seconds<10?"0"+seconds:seconds;
        return time;
    }

    static createTextSpan(text) {
        var span = document.createElement("span");
        span.innerText = text;
        return span;
    }
}