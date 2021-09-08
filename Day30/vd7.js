var student = {
    name: 'Nguyen Van A',
    gender: 'male',
    age: 20
};
console.log(student.name, student.gender, student.age)

var studentList = [
    {
        name: 'Nguyen Van A',
        gender: 'male',
        age: 20
    },
    {
        name: 'Nguyen Thi C',
        gender: 'female',
        age: 25
    }
];
var n = studentList.length;
console.log('Ho va ten\t|\tGioi tinh\t|\tTuoi')
for(var i = 0; i < n; i++) {
    var st = studentList[i];
    console.log(`${st.name}\t|\t${st.gender}\t\t|\t${st.age}`);
}