import express from "express";
import { exec } from "node:child_process";
import { Request, Response } from "express";

const app = express()
const PORT = 8080

app.get("/:name", handleName);
app.get("/", handleHealth);

async function handleName(req:Request, res:Response) {
    
    const name = req.params.name.replace("+", " ");

    if (!process.cwd().includes("/Scripts")){
        process.chdir(`${process.cwd()}/Scripts`);
    }


    const cmd = `'./.pyenv/bin/python3' main.py '${name}' --stdout`;
    const bufferSize = 1024 * 1024 * 10; // 1MB 

    exec(cmd, {"maxBuffer": bufferSize, encoding: "binary"},  (err, stdout, stderr) => {
        if (err){
            console.log(err.code);
            console.log(err.message);
            console.log(stderr);
        }
        res.type("png");
        res.status(200);
        res.send(Buffer.from(stdout, "binary"));
        res.end()
    });

}

async function handleHealth(req:Request, res:Response) {
    res.status(200);
    res.send("<h1>Ready To Go...</h1>");
    res.end();
}

app.listen(PORT, () => {
    console.log(`server is running on port ${PORT}...`);
})