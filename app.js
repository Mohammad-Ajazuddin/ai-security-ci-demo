const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const { exec } = require("child_process");

const app = express();
app.use(express.json());

const db = new sqlite3.Database(":memory:");

// ❌ SQL Injection Vulnerability
app.get("/user", (req, res) => {
  const id = req.query.id;
  db.all("SELECT * FROM users WHERE id=" + id, (err, rows) => {
    res.json(rows);
  });
});

// ❌ Command Injection Vulnerability
app.get("/ping", (req, res) => {
  exec("ping -c 1 " + req.query.host, (err, stdout) => {
    res.send(stdout);
  });
});

app.listen(3000, () => console.log("Vulnerable app running"));
