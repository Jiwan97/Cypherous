

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



// if continueQuiz button clicked
continue_btn.onclick = ()=>{
    info_box.classList.remove("activeInfo");
    quiz_box.classList.add("activeQuiz");
    startTimer(time1);
    startTimerLine(0);
}


let counter;
let counterLine;
let widthValue = 0;




const next_btn = document.querySelector("footer .next_btn");



next_btn.onclick = ()=>{
    clearInterval(counter);
    clearInterval(counterLine);
    showResult();
}



function startTimer(time){
    counter = setInterval(timer, 1000);
    function timer(){
        timeCount.textContent = time;
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
        if(time < 9){
            let addZero = timeCount.textContent;
            timeCount.textContent = "0" + addZero;
        }
        if(time < 0){
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
