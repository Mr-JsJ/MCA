function validateForm() {
  // Fetch form elements
  var fname = document.forms["myForm"]["fname"].value;
  var lname = document.forms["myForm"]["lname"].value;
  var dobday = document.forms["myForm"]["dobday"].value;
   var dobmonth = document.forms["myForm"]["dobmonth"].value;
    var dobyear = document.forms["myForm"]["dobyear"].value;
  var mobile = document.forms["myForm"]["ph"].value;
  var course = document.querySelector('input[name="course"]:checked');

  // Get the warning message elements
  var fnameWarning = document.getElementById("fnameWarning");
  var lnameWarning = document.getElementById("lnameWarning");
  var dobdayWarning = document.getElementById("dobdayWarning");
   var dobmonthWarning = document.getElementById("dobmonthWarning");
    var dobyearWarning = document.getElementById("dobyearWarning");
  var mobileWarning = document.getElementById("mobileWarning");
  var courseWarning = document.getElementById("courseWarning");

  // Reset warning messages
  fnameWarning.innerHTML = "";
  lnameWarning.innerHTML = "";
  dobdayWarning.innerHTML = "";
  dobmonthWarning.innerHTML = "";
  dobyearWarning.innerHTML = "";
  mobileWarning.innerHTML = "";
  courseWarning.innerHTML = "";

  // Check if First Name is blank
  if (fname.trim() === "") {
    fnameWarning.innerHTML = "First Name should not be blank";
    document.myForm.fname.focus();
    return false;
    
  }
  // Check if last Name is blank
  if (lname.trim() === "") {
    lnameWarning.innerHTML = "Second Name should not be blank";
    document.myForm.lname.focus();
    return false;
  }

  if (dobday === "") {
    dobdayWarning.innerHTML = "Please select the Date";
    document.myForm.dobday.focus();
    return false;
  }
  
   if (dobmonth === "") {
    dobmonthWarning.innerHTML = "Please select the MONTH";
    document.myForm.dobmonth.focus();
    return false;
  }

 if (dobyear === "") {
    dobyearWarning.innerHTML = "Please select the YEAR";
    document.myForm.dobyear.focus();
    return false;
  }

  const day = dobday;
  const month = dobmonth;
  
  if ( dobday < 1 ||  dobday > 31)  {
    document.getElementById("dobdayWarning").innerHTML =
      "Invalid day values.";
    document.myForm.dobday.focus();
    return false;
  }
  if(dobmonth < 1 || dobmonth > 12){
    document.getElementById("dobmonthWarning").innerHTML =
      "Invalid month values.";
    document.myForm.dobmonth.focus();
    return false;
  }

if(dobyear < 1900 || dobyear > 2100){
    document.getElementById("dobyearWarning").innerHTML =
      "Invalid year values.";
    document.myForm.dobyear.focus();
    return false;
  }

  // Check if Mobile number length is 10
  if (mobile.length !== 10) {
    mobileWarning.innerHTML = "Mobile number should be 10 digits long";
    document.myForm.ph.focus();
    return false;
  }

  // Check if at least one option is selected for Course
  if (!course) {
    courseWarning.innerHTML = "Please select a course";
    return false;
  }

  // The form is valid if it passes all the conditions
  alert("Form submitted Successfully");
  return true;
}
