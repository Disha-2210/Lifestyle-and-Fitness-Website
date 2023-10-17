function calculateBMI(event) {
  event.preventDefault();

  var age = document.getElementById("age").value;
  var height = document.getElementById("height").value;
  var weight = document.getElementById("weight").value;
  var gender = document.getElementById("gender").value;

  // BMI calculation formula
  var bmi = weight / ((height / 100) * (height / 100));

  // Display the result
  var resultElement = document.getElementById("result");
  resultElement.innerHTML = "Your Body Mass Index (BMI) is: " + bmi.toFixed(2);

  // Interpret BMI based on gender and age
  if (gender === "male") {
    if (age < 18) {
      resultElement.innerHTML += "<br>Interpretation for males under 18 may vary.";
    } else if (bmi < 18.5) {
      resultElement.innerHTML += "<br>Underweight";
    } else if (bmi >= 18.5 && bmi < 25) {
      resultElement.innerHTML += "<br>Normal weight";
    } else if (bmi >= 25 && bmi < 30) {
      resultElement.innerHTML += "<br>Overweight";
    } else {
      resultElement.innerHTML += "<br>Obese";
    }
  } else {
    if (age < 18) {
      resultElement.innerHTML += "<br>Interpretation for females under 18 may vary.";
    } else if (bmi < 18.5) {
      resultElement.innerHTML += "<br>Underweight";
    } else if (bmi >= 18.5 && bmi < 24) {
      resultElement.innerHTML += "<br>Normal weight";
    } else if (bmi >= 24 && bmi < 30) {
      resultElement.innerHTML += "<br>Overweight";
    } else {
      resultElement.innerHTML += "<br>Obese";
    }
  }
}
