/*
var body = document.body.children[0];
console.log(body);
var h1 = body.children[0];

alert("ree");

document.title = "Dog";

h1.innerHTML("Howdy");
*/

function changeTitle() {
    document.title = "Dog";
}

function changeH1() {
    document.body.children[0].innerHTML = "Howdy";
}

function changeH1Back() {
    document.body.children[0].innerHTML = "Welcome";
}

function changePet() {
    document.body.children[1].children[0].innerHTML = "pet";
}

function changeExc() {
    document.body.children[1].children[1].innerHTML = "!";
}

function changeImg() {
    document.body.children[2].src = "https://vetstreet.brightspotcdn.com/dims4/default/54186d0/2147483647/thumbnail/590x420/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F40%2F58%2F3bc5c01c4cdb8a0581681831faa9%2Fgreat-dane-shaking-paw-thinkstockphotos-522650067-590.jpg";
}