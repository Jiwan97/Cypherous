

const info_box = document.querySelector(".info_box");
const quiz_box = document.querySelector(".quiz_box");
const continue_btn = info_box.querySelector(".buttons .continue");
const result_box = document.querySelector(".result_box");
const option_list = document.querySelector(".option_list");
const time_line = document.querySelector("header .time_line");
const timeText = document.querySelector(".timer .time_left_txt");
const timeCount = document.querySelector(".timer .timer_sec");
const titleValue = document.querySelector(".title");
titleValue.innerHTML= title

let counter;
let counterLine;
let widthValue = 0;


if (time1<600) {
    info_box.classList.remove("activeInfo");
    quiz_box.classList.add("activeQuiz");
    startTimer(time1);
    startTimerLine(0);

}
// if continueQuiz button clicked
continue_btn.onclick = ()=>{
    info_box.classList.remove("activeInfo");
    quiz_box.classList.add("activeQuiz");
    startTimer(time1);
    startTimerLine(0);
}


const next_btn = document.querySelector("footer .next_btn");



next_btn.onclick = ()=>{
    clearInterval(counter);
    clearInterval(counterLine);
    showResult();
}



function startTimer(time){
    counter = setInterval(timer, 1000);
    function timer(){

        timeCount.textContent = convertHMS(time);
        time--;
        $.ajax({
            url: '/timelapse',
            data: {
                'time': time,
                'answer_id':answer_id,
            },
            success:function(response){
                console.log(response.success)
            }
        });
        if(time < 1){
            clearInterval(counter); //clear counter
            timeText.textContent = "Time Off";
            next_btn.click();
        }
    }
}

function startTimerLine(time){
    counterLine = setInterval(timer, time1);
    function timer(){
        time += 1;
        time_line.style.width = time + "px";
        if(time > 1199){
            clearInterval(counterLine);
        }
    }
}

function convertHMS(value) {
    const sec = parseInt(value, 10);
    let hours   = Math.floor(sec / 3600);
    let minutes = Math.floor((sec - (hours * 3600)) / 60);
    let seconds = sec - (hours * 3600) - (minutes * 60);
    // add 0 if value < 10; Example: 2 => 02
    if (hours   < 10) {hours   = "0"+hours;}
    if (minutes < 10) {minutes = "0"+minutes;}
    if (seconds < 10) {seconds = "0"+seconds;}
    if (hours == 0) {
      return minutes + ':' + seconds;
    } else {
      return hours + ':' + minutes + ':' + seconds;
    }
}