var name=prompt("Enter student name");
var m1=Number(prompt("Enter Mark1"));
var m2=Number(prompt("Enter Mark2"));
var m3=Number(prompt("Enter Mark3"));

var total=Number(m1+m2+m3);

if(total>145){
console.log("A+");
}
else if((total>140)&&(total<=145))
{
console.log("A");
}
else if((total>135)&&(total<=140))
{
console.log("B+");
}
else if((total>130)&&(total<=135))
{
console.log("B");
}
else if(total<130)
{
console.log("Failed");
}
else{
console.log("Invalid");
}