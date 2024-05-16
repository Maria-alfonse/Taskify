let taskId = document.querySelector("[name='id']")
let Ttitle = document.querySelector("[name='title']")
let teacherN = document.querySelector("[name='teacher']")
let des = document.querySelector("[name='Description']")
let admin= document.querySelector("[name='admin']")





function showError(errorElement,errorMessage){
    document.querySelector("."+errorElement).classList.add("dispaly-error");
    document.querySelector("."+errorElement).innerHTML =errorMessage;
}

function clearError() {
    let errors = document.querySelectorAll(".error");
    for (let error of errors) {
        error.innerHTML = "";
        error.classList.remove("display-error");
    }
    
}

document.forms[0].onsubmit = function(event) {
    clearError();
    
    if (taskId.value === "") {
        showError("Taskid-error", "Invalid Task id, it cannot be empty.");
        event.preventDefault(); 
        return false;
    }
    
    if (taskId.value.length > 3) {
        showError("Taskid-error", "Invalid Task id, it cannot be greater than 3 characters.");
        event.preventDefault(); 
        return false;
    }
   
    if (Ttitle.value === "") {
        showError("title-error", "Invalid Task Title, it cannot be empty.");
        event.preventDefault(); 
        return false;
    }
    
    if (Ttitle.value.length > 55) {
        showError("title-error", "Invalid Task Title, it cannot be greater than 55 characters.");
        event.preventDefault();   
        return false;
    }

    if (teacherN.value === "") {
        showError("TName-error", "Invalid Teacher Name, it cannot be empty.");
        event.preventDefault();
        return false;
    }
    
    if (teacherN.value.length > 55) {
        showError("TName-error", "Invalid, it cannot be greater than 55 characters.");
        event.preventDefault();
        return false;
    }
    
    if (des.value.length > 160) {
        showError("des-error", "Invalid Description, it cannot be greater than 160 characters.");
        event.preventDefault();
        return false;
    }
    if(admin.value ===""){
        showError("admin-error","Invalid admin name, it cannot be empty.")
        event.preventDefault();
        return false;
    }
  

    alert('Your task has been added. You can add another one!')
    window.localStorage.setItem("taskidVal",taskId.value);
        localStorage.setItem('TtitleVal',Ttitle.value);
        localStorage.setItem("teacherN",teacherN.value);
        localStorage.setItem("des",des.value);
        localStorage.setItem("adimnN",admin.value);
        let optionVal = this.choose.value;
        localStorage.setItem('option',optionVal)
        taskId.value = "";
    Ttitle.value = "";
    teacherN.value = "";
    des.value = "";
    admin.value="";
     
    
}

