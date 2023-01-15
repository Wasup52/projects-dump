var thumbs = document.getElementsByName("thumb");

console.log("thumbs: ", thumbs);

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

var isOver = false;
var overId;

thumbs.forEach(function(thumb) {
    // change the src link from thumb0 to thumb1 then thumb2 then thumb3 and then back to thumb0 on a loop
    // this will make the thumbnails change every 5 seconds
    
    thumb.addEventListener("mouseover", async function() {
        isOver = true;
        overId = thumb.id;
        // console.log("isOver: ", isOver);
    });

    thumb.addEventListener("mouseout", async function() {
        isOver = false;
        overId = thumb.id;
        // console.log("isOver: ", isOver);

        var src = thumb.src;
        var num = src.split("thumb")[2].split("-")[0];
        thumb.src = src.replace("thumb" + num, "thumb" + 0);
    });
});

function changeThumb(id) {
}

while (isOver) {
    var thumb = document.getElementById(overId);

    console.log("isOver: ", isOver);
    // get the current src link
    var src = thumb.src;
    // get the current number
    var num = src.split("thumb")[2].split("-")[0];
    console.log("num: ", num);
    // increment the number
    newNum = num+1;
    // if the number is greater than 3, set it to 0
    if(newNum > 3) newNum = 0;
    // set the new src link
    thumb.src = src.replace("thumb" + num, "thumb" + newNum);
    console.log("thumb.src: " + thumb.src);
}