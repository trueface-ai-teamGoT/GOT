const express = require('express')
const path = require('path')
// const router = require('./router/router.js')
const router = require('express').Router()
const IP = process.env.IP || 'localhost'
const PORT = process.env.PORT || '3000'
const app = express()  
// const api = require('../server/helpers/api')
// const dummyData = require('../database/dummyData').dummyData

app.use(express.static(path.join(__dirname, '../public')));

// app.get('/images/instagram', api.instagram.getInstagramUserImages)
// app.get('/images/twitter', api.twitter)
app.get('/', (req, res) => {
  res.send('youve hit the root path')
})

app.post('/testpath', (req, res) => {
  console.log('************* req =>', req)
  res.send('youve hit the testpath path')
})

app.listen(PORT, (err) => {  
  if (err) { return console.log('failure at app.listen in server/index =>', err) }
  console.log(`server is listening on ${PORT}`)
})

module.exports.app = app;
