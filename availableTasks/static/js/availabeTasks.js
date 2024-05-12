var x = document.getElementById("high");
var y = document.getElementById("medium");
var z = document.getElementById("low");
function high() {
    x.style.left = "15px";
    y.style.left = "900px";
    z.style.left = "1200px";
}

function medium() {
    x.style.left = "-1185px";
    y.style.left = "15px";
    z.style.left = "900px"
}
function low() {
    x.style.left = "-2090px";
    y.style.left = "-900px";
    z.style.left = "15px"
}
document.getElementById("user").innerHTML=localStorage.getItem("username");
var priority = localStorage.getItem("option")
if(priority === "Low"){
    document.getElementById("id2").innerHTML=localStorage.getItem("TtitleVal")
}
if(priority === "High"){
    document.getElementById("id").innerHTML=localStorage.getItem("TtitleVal")
}
if(priority === "Medium"){
    document.getElementById("id1").innerHTML=localStorage.getItem("TtitleVal")
}