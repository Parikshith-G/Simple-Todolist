const express = require("express");
const port = 3000;
const app = express();
var addItems = [];
app.use(express.static("public"));
app.set("view engine", "ejs");
const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }));
app.get("/", function (req, res) {
  var today = new Date();
  var options = {
    weekday: "long",
    day: "numeric",
    month: "long",
  };
  var day = today.toLocaleDateString("en-US", options);
  res.render("index", { kindOfDay: day, addItem: addItems });
});

app.post("/", function (req, res, next) {
  addItem = req.body.addItem;
  addItems.push(addItem);

  res.redirect("/");
});

app.listen(port, function () {
  console.log("App listening on port " + port);
});
