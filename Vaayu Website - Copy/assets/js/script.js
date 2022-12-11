const counter = document.getElementById('counter');
let endDate = new Date(2023, 02, 10, 05, 30);
let endTime = endDate.getTime();

function countdown() {
    let todayDate = new Date();
    let todayTime = todayDate.getTime();
    let remainingTime = endTime - todayTime;
    let oneMin = 60 * 1000;
    let oneHr = 60 * oneMin;
    let oneDay = 24 * oneHr;

    let addZeroes = (num) => (num < 10 ? `0${num}` : num);

    if (endTime < todayTime) {
        clearInterval(i);
        document.querySelector(
            ".countdown"
        ).innerHTML = `<h1>Countdown Has Expired</h1>`;
    } else {
        let daysLeft = Math.floor(remainingTime / oneDay);
        let hrsLeft = Math.floor((remainingTime % oneDay) / oneHr);
        let minsLeft = Math.floor((remainingTime % oneHr) / oneMin);
        let secsLeft = Math.floor((remainingTime % oneMin) / 1000);

        day = addZeroes(daysLeft);
        hour = addZeroes(hrsLeft);
        min = addZeroes(minsLeft);
        sec = addZeroes(secsLeft);

        counter.innerHTML = `${day} : ${hour} : ${min} : ${sec}`

    }
}

setInterval(countdown, 1000);
