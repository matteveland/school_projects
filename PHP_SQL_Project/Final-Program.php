<?php
/*
Your Portfolio Project consists of three components:

Program corrections
Lessons learned reflection
Final program
Assignment Instructions

1. Program corrections:

Make appropriate corrections to all the programming assignments submitted as Critical Thinking Assignments from Modules 1-6.
Submit the programs along with a carefully outlined description of corrections made in order for programs to run correctly.

2. Lessons learned reflection:

Create a 2-3 page summary that outlines the lessons learned in this PHP/MySQL course.

3. Final program: Create a PHP class named "User" with the following private fields:

- name
- birthdate in yyyy/mm/dd format
- age
- department.

In the class, include getter and setter methods to get and set the values of those variables.

- Author a data entry webform using HTML text input boxes and a submit button. When the user clicks on the submit button, a "User" class is instantiated and the new User object's fields are populated.
- The HTML input boxes correspond to the field in the "User" class.
- Add an "Insert" button that allows the user to insert the form data to a MySQL table.
//INSERT INTO `finalProject`(`id`, `name`, `birthdate`, `age`, `department`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5])
- Add a "Display" button the displays the contents of your MySQL table on the web form when the end-user clicks on the button.


Assignment Submission Instructions

Zip up the following files and submit in one file:
Compiled Module 1-6 programs with corrections
Lessons learned reflection
Final program course code and application screenshots
The name of the zip file should be LastName_FirstName_MOD8_PORTFOLIO_OPT1.zip
Good Luck!

Ask your instructor for assistance if you need it.
*/

define('DB_USER', 'PHP_Class_User');
define('DB_PASSWORD', 'phpclass');
define('DB_HOST', 'localhost');
define('DB_NAME', 'ITS345');

$connect = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

if ($connect->connect_error) {
  echo $connect->connect_error;
  unset($connect);
  // code...
} else {
  $connect->set_charset('utf8');
}

class User
{
  private $name;
  private $birthdate;
  private $age;
  private $department;
  private $connect;

  //setters/getters

  public function setName($name)
  {
    $this->name = $name;
  }
  public function getName()
  {
    return $this->name;
  }
  public function setBirthdate($birthdate)
  {
    $this->birthdate = $birthdate;
  }
  public function getBirthdate()
  {
    return $birthdate;
  }
  public function setAge($age)
  {
    $this->age = $age;
  }
  public function getAge()
  {
    return $age;
  }
  public function setDepartment($department)
  {
    $this->department = $department;
  }
  public function getDepartment()
  {
    return $department;
  }
  //submit user information.

  public function submitUser($connect, $name, $birthdate, $age, $department)
  {


    if (!is_numeric($age)) {
      echo "<p class='error'>Your age was not a number. Please enter a number and submit again.</p>";
    }

    $submitUser = "INSERT INTO finalProject(id, name, birthdate, age, department) VALUES (id,'$name','$birthdate','$age','$department')";

    $submitConnect = mysqli_query($connect, $submitUser);
    if (!$submitConnect) {
      echo "<p class='error'>Connection to database did not work.</p>";
    } else {
      echo "<p class='success'>" . $name . " was successfully added to the database. </p>";
    }
  }
}

//Chose to use required for form field so the need of empty() would not be needed.
if (isset($_POST['submitUser'])) {


  $name = mysqli_real_escape_string($connect, $_POST['name']);
  //change birthdate to yyy/mm/dd/ format
  $birthdate = mysqli_real_escape_string($connect, $_POST['birthdate']);
  $birthdate = strtotime($birthdate);
  $birthdate = date('Y/m/d', $birthdate);
  $age = mysqli_real_escape_string($connect, $_POST['age']);
  $department = mysqli_real_escape_string($connect, $_POST['department']);

  $newUserSubmit = new User();
  $newUserSubmit->submitUser($connect, $name, $birthdate, $age, $department);

}

//display contents of Database
function table($total, $item1, $item2, $item3, $item4)
{
  $arrayVar = array($item1, $item2, $item3, $item4);
  $total = count(mysqli_num_rows($total));

  echo '<table style="border-collapse: collapse;">
  <thead style="border: 1px solid black;">
  <tr style="border: 1px solid black;">';
  for ($i = 0; $i < count($arrayVar); $i++) {
    echo '<td style="border: 1px solid black;">' . $arrayVar[$i] . '</td>';
  }
  echo '</th></tr></thead><tbody>';
}

function results($results, $item1, $item2, $item3, $item4)
{
  while ($row = mysqli_fetch_assoc($results)) {
    echo '<tr>
    <td style="border: 1px solid black;">' . $row[$item1] . '</td>
    <td style="border: 1px solid black;">' . $row[$item2] . '</td>
    <td style="border: 1px solid black;">' . $row[$item3] . '</td>
    <td style="border: 1px solid black;">' . $row[$item4] . '</td>
    ';
  }
  echo '</tbody></table>';
}

?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>Final Project</title>
  <style media="screen">
  .error {
    background-color: tomato;
  }
  .success {
    background-color: MediumSeaGreen;
  }
  </style>
</head>
<body>
  <h1>Please insert a User:</h1>
  <form class="" action="#" method="post">
    <!--Name-->
    <label for="name">User's Name:</label>
    <input type="text" name="name" value="" placeholder="name" required>
    <br>
    <!--birthdate-->
    <label for="birthdate">User's Birthday</label>
    <input type="date" name="birthdate" value="" placeholder="birthdate" required>
    <br>
    <!--age-->
    <label for="age">User's Age</label>
    <input type="text" name="age" value="" placeholder="age" required>
    <br>
    <!--department-->
    <label for="department">User's department</label>
    <input type="department" name="department" value="" placeholder="department" required>
    <br>
    <!--Name--><label for="submitUser"></label>
    <button type="submit" name="submitUser">Submit User Information</button>
  </form>
  <br>
  <h1>User information within the database</h1>
  <form class="" action="#" method="post">
    <button type="submit" name="showUsers">Display Users</button><button type="submit" name="remove">Do Not Display Users</button>
  </form>
  <br>

  <?php

  $query = "SELECT * FROM finalProject WHERE 1 ORDER BY id ASC";
  $results = mysqli_query($connect, $query);
  if (isset($_POST["showUsers"])) {
    table($results, "Name", "Birthdate", "Age", "Department");
    results($results, "name", "birthdate", "age", "department");
    mysqli_free_results($results);
  }elseif (isset($_POST["remove"])) {
    echo "Users no longer displayed.";
  }else {
    // code...
  }
  mysqli_close($connect);

  ?>
</body>
</html>
