var fs = require("fs")
fs.readdir(__dirname, function (err, file) {
    var s = "var s=" + JSON.stringify(file)
    fs.writeFileSync("index.js",s)
})