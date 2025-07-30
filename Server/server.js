import express from "express";
import { exec } from "node:child_process";
const app = express()
const PORT = 8080

app.get("/:name", handleName);


async function handleName(req, res) {
    const name = req.params.name;
    const bufferSize = 1024 * 1024 * 10 // 1MB 
    const cwd = process.cwd() 
    const cmd = `'${cwd + "/Scripts/.pyenv/bin/python3"}' '${cwd + "/Scripts/main.py"}' ${name} --stdout`
    exec(cmd, {"maxBuffer": bufferSize, encoding: null },  async (err, stdout, stderr) => {
        res.type("png");
        res.status(200);
        res.send(stdout);
    })



}

app.listen(PORT, () => {
    console.log("server is running...");
})