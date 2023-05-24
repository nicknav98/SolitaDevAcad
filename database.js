var mysql = require('mysql')
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'adminUser', //
  password: 'Testing123', //
  database: 'TestDB',
})
connection.connect((err) => {
  if (err) {
    console.log(err)
    return
  }
  console.log('Database connected')
})
module.exports = connection