# Gynvael LiveStream Challanges Solution Mission 006

We are provided with a file http://goo.gl/S395x6 from [Gynvael LiveStream](https://www.youtube.com/watch?v=KvyBn4Btv8E) thats all nothing else.
<br>
Sorting this file in Sublime Text i could see that max number was 24.

My first approach was to treat this as a image and draw lines from first point to the next, which gave me a gibrish looking image, tried changing magnification but it lead to nothing.

Then i thought these are not lines maybe but set of point so i plotted them. Bingo i got a QR code.The QR code was small 24*24 so i maginified it by plotting a rectangle rather than a point.

![QRCode Image](/result_m6.jpg?raw=true "QRCode obtained")

Scanned using Barcode Scanner to confirm and then used an [online service](https://zxing.org/w/decode.jspx) to get the answer in text format (I could have typed it but who cares)


#### Answer
<pre>
Mirrored QR? Seriously?!
</pre>


See the [Solution_006](solve6.py) for the code with comment and with all my approachs.


Once again thank you Gynvael for this awesome challange.


# Author
Arun Kumar Shreevastava