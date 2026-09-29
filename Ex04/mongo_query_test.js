use college
// Create index
db.students.createIndex({ rollno: 1 })
// Query student by roll number
db.students.find({ rollno: 50000 })
// Project specific fields
db.students.find({}, { name: 1, mark: 1, _id: 0 }).limit(5)
