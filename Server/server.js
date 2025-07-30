import express from "express";
import { spawn } from "node:child_process";
const app = express()
const PORT = 8080

app.get("/:name", handleName);


async function handleName(req, res) {
    const name = req.params.name;
    const ls = spawn('ls')
    // console.log(ls);

    const image = spawn(`python3`, [process.cwd() + "/Scripts/main.py", name]);
    image.on("close", (code) => {
        console.log(`the proccess pytho3 main.py... closed with code ${code}`);
        
    })
    res.type("png");
    res.status(200);
    res.sendFile(process.cwd() + "/output.png")

    console.log(ls);

}

app.listen(PORT, () => {
    console.log("server is running...");
})