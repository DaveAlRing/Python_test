// for loops

// for(let i = 0; i < 5; i++){
//     console.log("Hello ", i);
// }
// console.log('loop complete');

// const names = ['shaun', 'mario', 'luigi'];
// for(let i = 0; i < names.length; i++){
//     // console.log(names[i], i);
//     let html = `<div>${names[i]}</div>`;
//     console.log(html);
// }

// while loops

// const names = ['shaun', 'mario', 'luigi'];
// let i=0;
// while(i < names.length){
//     console.log(names[i], i);
//     i++;
// }

// do while loops

// let i = 5;
// do{
//     console.log('val of i is: ', i);
//     i++;
// } while(i < 5);

// if statements

// const age = 20;
// if(age >= 20){
//     console.log("you are over 20 years old");
// }

// const ninjas = ['shaun', 'ryu', 'chun-li', 'yoshi'];
// if(ninjas.length > 3){
//     console.log("that's a lot of ninjas")
// };

// logical operators - OR || and AND &&

// const password = "p@ssdf";
// if(password.length >= 12 && password.includes("@")){
//     console.log("Strong password");
// } else if(password.length >= 8 || password.includes("@") && password.length > 5){
//     console.log("that password works");
// } else {
//     console.log("Doesn't work");
// }

// logical NOT (!)

// let user = false;
// if(!user){
//     console.log("you must be logged in to continue");
// }

// console.log(!true);
// console.log(!false);

// break and continue

// const scores = [50, 25, 0, 30, 100, 20, 10];

// for(let i = 0; i < scores.length; i++){
//     if(scores[i] === 0){
//         continue;
//     }

//     console.log("your score: ", scores[i]);

//     if(scores[i] === 100){
//         console.log("Congrats, you win!");
//         break
//     }
// }

// switch statements (use strict ===)

// const grade = 'D';

// switch(grade){
//     case 'A':
//         console.log("You got an A!");
//         break;
//     case 'B':
//         console.log("You got an B!");
//         break;
//     case 'C':
//         console.log("You got an C!");
//         break;
//     case 'D':
//         console.log("You got an D!");
//         break;
//     case 'E':
//         console.log("You got an E!");
//         break;
//     default:
//         console.log("Not valid");
// }

// // using if statements
// if(grade === 'A'){

// } else if(grade === 'B'){

// } else if(grade === 'C'){

// } else if(grade === 'D'){

// } else if(grade === 'E'){

// } else {

// }

// variables & block scope

// let age = 30; 

// if(true){
//     let age = 40;
//     let name = 'shaun';
//     console.log("inside 1st code block: ", age, name);
//     if(true){
//         let age = 50;
//         console.log("inside 2nd code block: ", age);
//     }
// }

// console.log("outside code block: ", age, name);