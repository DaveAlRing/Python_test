// let age = 25;
// let year = 2019;

// console.log(age, year);

// age = 30;
// console.log(age);

// const points = 100;
// console.log(points);

// // // strings
// // console.log("hello world");

// // console.log(email);

// // // string concatentation
// // let firstName = "Brandon";
// // let lastName = "Sanderson";
// // let fullName = firstName + " " + lastName;
// // console.log(fullName);

// // //getting charactesr
// // console.log(fullName[0]);

// // //string length
// // console.log(fullName.length);

// // //string methods
// // console.log(fullName.toUpperCase());
// // //let result = fullName.toLowerCase();
// // //console.log(result);

// // let index = email.indexOf("@");
// // console.log(index);

// let email = "mario@thenetninja.co.uk"

// //let result = email.lastIndexOf("n");

// //let result = email.slice(0,5);

// //let result = email.substr(4,10);

// //let result = email.replace("m", "w");

// let result = email.replace("n", "w");

// console.log(result);

// let radius = 10;
// const pi = 3.14;

// //console.log(radius,pi);

// //math +, -, *, /, **, %

// //let result = radius % 3;

// //let result = pi * radius**2;

// // let result = 5 * (10-3)**2;
// // console.log(result);

// let likes = 10;
// // likes++;
// // likes += 10;
// // likes -=2;
// // likes *=2;
// // likes /=2;
// // console.log(likes);

// // NaN - not a number
// // console.log(5/"hello");
// // console.log(5*"hello");

// let result = "the blog has " + likes + " likes";
// console.log(result);

// // template strings
// const title = "Best reads of 2019";
// const author = "Mario";
// const likes = 30;

// // concatenation way
// // let result = "The blog called " + title + " by the author " + author + " has " + likes + " likes.";
// // console.log(result);

// // template string way
// let result = `The blog called ${title} by ${author} has ${likes} likes`;
// console.log(result);

// // creating html templates
// let html = `
//  <h2>${title}</h2>
//  <p>By ${author}</p>
//  <span>This blog has ${likes} likes</span>
//  `;

//  console.log(html);

// let ninjas = ["shaun", "ryu", "chun-li"];
// // // ninjas[2] = "Naruto";
// // // console.log(ninjas[2]);

// // let ages = [20, 25, 30, 35];
// // console.log(ages.indexOf(25));

// // array methods

// // let result = ninjas.join('- ');
// // let result = ninjas.concat(["ken", "crystal"]);
// // console.log(result.join(" * "));

// let result = ninjas.push("Ken");
// result = ninjas.pop();
// console.log(ninjas);

// undefined and null
// let age = null;
// console.log(age, age + 3, `the age is ${age}`);

// //boolean
// console.log(true, false);
// let email = "luigi@thenetninja.co.uk";
// // let result = email.includes('!');
// let names = ["mario", "luigi", "toad"];
// let result = names.includes('luigi');
// console.log(result);

// methods can return booleans

// //comparison operators
// let age = 25;

// console.log(age == 25);
// console.log(age == 30);
// console.log(age != 30);
// console.log(age > 20);
// console.log(age < 25);
// console.log(age <= 25);
// console.log(age >= 25);

// let name = 'shaun';

// console.log(name > 'crystal');

// let age = 25;

// // loose comparison ==

// // console.log(age == 25);
// // console.log(age == '25');

// // strict comparison ===

// console.log(age === '25');

// type conversion
let score = '100';
score = Number(score);

console.log(score + 1, typeof score);
// let result = Number('hello');
// console.log(result);
