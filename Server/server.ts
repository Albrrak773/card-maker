import express from "express";
import { spawn } from "node:child_process";
import type { Request, Response } from "express";

const app = express()
const PORT = 8080

app.get("/:name", handleName)


async function handleName(req:Request, res:Response) {
    const name = req.params.name;
    const ls = spawn('ls')
    const image = spawn(`python3`, ["main.py", name]);

    res.type("png");
    res.status(200);
    res.sendFile("./output.png")

    console.log(ls);

}