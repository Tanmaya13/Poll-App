function validate()
{
    const password = document.getElementById('password').value;

    

    //PASSWORD
    if(password === "")
    {
        document.getElementById("password_error").innerHTML = "Password is required !";
        error = true;
    }
    else if(password.length <= 8 || password.length > 16)
    {
        document.getElementById("password_error").innerHTML = "Password must be 8 - 16 characters long";
        error = true;
    }
    else if(!password.match(/[a-z]/)){
        document.getElementById("password_error").innerHTML = "Password must contain a lowercase character";
        error = true;
    }
    else if(!password.match(/[A-Z]/)){
        document.getElementById("password_error").innerHTML = "Password must contain a uppercase character";
        error = true;
    }
    else if(!password.match(/[0-9]/)){
        document.getElementById("password_error").innerHTML = "Password must contain a number";
        error = true;
    }
    else if(!password.match(/[!@#$%^&*]/)){
        document.getElementById("password_error").innerHTML = "Password must contain a character among !@]#$%^&*";
        error = true;
    }
    else{
        document.getElementById("password_error").innerHTML = "";
    }

}

