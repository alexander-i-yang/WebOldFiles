
let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

let today = new Date();
let todayYear = today.getYear()+2000-100;
for(var i=0; i<months.length; ++i) {
  let isThisMonth = today.getMonth();
  isThisMonth = isThisMonth==i? "selected" : "";
  let month = '<option ' + isThisMonth + '>' + months[i] + '</option>';
  $("#month-selector").append(month);
}

for(var i = 1990; i<=todayYear; ++i) {
  let isThisYear = todayYear==i? "selected" : "";
  let year = '<option ' + isThisYear + '>' + i + '</option>';
  $("#year-selector").append(year);
}

for(let i = 0; i<days.length; ++i) {
  let dayName = '<div class="day-header">' + days[i] + '</div>'
  $("main").append(dayName);
}

resetCalendar();

$("#year-selector").change(function() {
  let newYear = $(this).val();
  console.log(newYear);
  today.setYear(newYear);
  console.log(today);
  clearDays();
  resetCalendar();
});

$("#month-selector").change(function() {
  let newMonth = months.indexOf($(this).val());
  today.setMonth(newMonth);
  console.log(today);
  clearDays();
  resetCalendar();
});

function resetCalendar() {
  let firstDay = getDayMonth(today);
  let lastDay = getLastDay(today);
  let todayDate = today.getDate();
  for(let i = 0; i<lastDay; ++i) {
    let selected = i==todayDate ? "selected" : "";
    let day = $('<div class="day ' + selected + '"><div>' + (i+1) + '</div></div>');
    day.css("grid-column", (i+firstDay+1)%7);
    $("main").append(day);
  }
  $(".day").click(function() {
    $(".day").removeClass("selected");
    $(this).addClass("selected");
  });
}

function clearDays() {
  $(".day").remove();
}

function getDayMonth(dayMonth) {
  let newDay = new Date(dayMonth.getTime());
  newDay.setDate(1);
  return newDay.getDay();
}

function getLastDay(dayMonth) {
  let newDay = new Date(dayMonth.getTime());
  newDay.setMonth(dayMonth.getMonth()+1);
  newDay.setDate(0);
  return newDay.getDate();
}
