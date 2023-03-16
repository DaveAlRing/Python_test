// // function declaration

// function greet(x){
//     console.log("My function: ", x);
// }

// greet("Hello");
// greet("Hiya");
// greet("Bye");

// // function expression

// const speak = function(){
//     console.log("Good day!");
// };

// speak();

// arguments & parameters

const speak = function(name = "Luigi", time = "night"){
    console.log(`good ${time}, ${name}`);
};

speak("Teagan", "Morning");


