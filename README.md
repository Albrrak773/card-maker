






# misc
in this project the way the image is sent is by making the python script output the image binary to stdout and then make the javascript read the stdout and just pass the binary straight to the client.
the following is what would happen if did not do that and how I learned how to do that:
#### what would happen if the file was saved to the file system instead of using stdout?
will let's see the time line:
* the server calls the python script
* the python script generates the image and saves it to the file system under the name output.png
* the server then reads and sends the file output.png
* so far so good.. but let's say the server gets 10 requests at approximately the same time
**this is where problems start to happen**
* it would be the perfect storm for a [race condition.](https://en.wikipedia.org/wiki/Race_condition)
* but let's assume that somehow launching 10 process that all write to the same file doesn't create a race condition. this is still bad because some clinet might get the image output of a different client!
* all of the above is bad, but we can fix it by not having the script output the image to the same file with the same name. maybe we can have it save the image with the name that the client sent... yah that could work but 2 people could send a request with the same name around the same time so..
* so we could instead create a random number for each request and tell the script to save the image under that random number that way when we read the image we read the one with that random number which we know for a fact to be acccoiated with the client
* that's great but know I have to save the image of every single request! that is absurd and very inefficient. ok maybe I delete the image after the request is done.

so by the end we do have solution and it does work but it intrduces extra latency (because now we have to do 2 I/O operatoins to the disk one to save the image and one to delete it) as well as other potential problems that would accure when there are a lot of requets at the same time.

### how did I figure out how send to stdout
while reading the pillow docs I came across [this example](https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#example-draw-a-gray-cross-over-an-image), and at the last line it showed that you can output the image to stdout.
which did a 💡! in my head and I kinda just took it from there, if I can output to stdout how do I capture that stdout in node, how do I send that stdout binary to cline... a fter a bit of research all of that was answered in no time.
if I made the script output to the file system that's not that bad and it's probably fine especially for a small project but I am here to learn and write great code, not to do a 'good enough' job.