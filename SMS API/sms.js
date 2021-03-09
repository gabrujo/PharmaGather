var unirest = require("unirest");

var req = unirest("GET", "https://d7sms.p.rapidapi.com/secure/balance");

req.headers({
	"x-rapidapi-host": "d7sms.p.rapidapi.com",
	"x-rapidapi-key": "SIGN-UP-FOR-KEY"
});

req.end(function (res) {
	if (res.error) throw new Error(res.error);
	console.log(res.body);
});