# conuhack

### Contributors :busts_in_silhouette:
- Sahil Kapal
- Walter Cheng
- Cheldon Mahon
- Esra'a Saleh

### How to use :question:
- Enter a YouTube URL inside text box and click the enter button. Then, wait until the server responds and get the result to the client side. The whole processes might take 30 seconds to few minutes, depends on the times of the video.

### Goal :trophy:
- To assist ESL students or other second language students by analysisng youtube videoes and find out the most common vocabulary spoken there. This draws their attention to the words that are more important for the development of their vocabulary.

### Steps :feet:
- Fetch youtube video to text information by IBM (API)
- Analyse the sentences to find out which are the most frequently used (back-end)
- Create html page for user to type in the youtube link (front-end)
- Create a server to transfer information (back-end)
- If possible, save the data to the database and find out which vocab people use the most in that month (to be done...)

### Things to install :arrow_down:
- Install things for this repo:
```
./install.sh
```
- If not work, try this first:
```
sudo chmod +x install.sh
```

- Start the server
```
python3 server.py
```

- Convert youtube to mp3
```
python3 mp3_youtube.py
```
