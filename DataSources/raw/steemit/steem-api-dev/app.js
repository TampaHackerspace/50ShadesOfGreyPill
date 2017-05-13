var express = require('express');
var path = require('path');
var logger = require('morgan');
var bodyParser = require('body-parser');
var cors = require('cors');
var http = require('http'),
  https = require('https');
http.globalAgent.maxSockets = Infinity;
https.globalAgent.maxSockets = Infinity;

var app = express();

app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cors());

// view engine setup
var hbs = require('hbs');
app.set('view engine', 'hbs');

app.use(express.static(path.join(__dirname, 'public'), {maxAge: (86400000 * 7)}));
app.use(express.static(path.join(__dirname, 'node_modules')));
app.use('/', require('./routes/api'));

app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.json(['error', {
    message: err.message,
    error: {}
  }]);
});


module.exports = app;
