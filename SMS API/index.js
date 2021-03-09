const lib = require('lib');

// Configuration parameters and credentials
lib.Configuration.aPIUsername = "aPIUsername"; // API Key
lib.Configuration.aPIPassword = "aPIPassword"; // API Token

var controller = lib.APIController;

function getBalance(callback)

controller.getBalance(function(error, response, context) {});

function createSendSMS(input, callback)

var input = [];
input['body'] = new SendSMSRequest({ "key": "value" });
input['contentType'] = 'Content-Type';
input['accept'] = 'Accept';

controller.createSendSMS(input, function(error, response, context) {});

function createBulkSMS(body, contentType, accept, callback)

var body = new BulkSMSRequest({ "messages": [{ "to": ["971562316353", "971562316354", "971562316355"], "content": "Same content goes to three numbers", "from": "SignSMS" }] });
var contentType = 'application/json';
var accept = 'application/json';

controller.createBulkSMS(body, contentType, accept, function(error, response, context) {});