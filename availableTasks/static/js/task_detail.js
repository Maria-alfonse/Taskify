
let state = localStorage.getItem("status");
document.getElementById("res7").textContent = state;

const toggleTaskStatus = (event) => {
    event.preventDefault();
    let status = state === "Done" ? "Not Done" : "Done";

    const taskDetails = {
        title: localStorage.getItem("TtitleVal"),
        taskId: localStorage.getItem("taskidVal"),
        teacher: localStorage.getItem("teacherN"),
        description: localStorage.getItem("des"),
        createdBy: localStorage.getItem("adimnN"),
        priority: localStorage.getItem("option"),
        status: status
    };

    localStorage.setItem("completedTask", JSON.stringify(taskDetails));
    localStorage.setItem("status", status);

    alert(`Your task has been marked as ${status.toLowerCase()}!`);
    if (status == "Done") {
        window.location.href = "completed.html";
        document.getElementById("id1").innerHTML=localStorage.getItem("completedTask")
    } else {

        window.location.href = "TeacherHome.html";
    }
};

const cancelAction = () => {
    window.history.back();
};

document.getElementById('markAsDoneBtn').addEventListener('click', toggleTaskStatus);
document.getElementById('cancelBtn').addEventListener('click', cancelAction);

const updateDetails = () => {
    let statusText = localStorage.getItem("status") || "Not Done";
    let buttonLabel = statusText === "Done" ? "Mark as Not Done" : "Mark as Done";

    document.getElementById("markAsDoneBtn").textContent = buttonLabel;

    document.getElementById("res").textContent = localStorage.getItem("TtitleVal");
    document.getElementById("res1").textContent = localStorage.getItem("taskidVal");
    document.getElementById("res2").textContent = localStorage.getItem("TtitleVal");
    document.getElementById("res3").textContent = localStorage.getItem("teacherN");
    document.getElementById("res4").textContent = localStorage.getItem("des");
    document.getElementById("res5").textContent = localStorage.getItem("adimnN");
    document.getElementById("res6").textContent = localStorage.getItem("option");
    document.getElementById("res7").textContent = statusText;
};

updateDetails();