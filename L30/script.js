// Clear the screen on click of C button.
const clearScreen = async () => {
    document.getElementById("result").value = "";
}

// Display entered value on the screen.
const setScreenValue = async (value) => {   
    document.getElementById("result").value += value;
}