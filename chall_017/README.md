# Gynvael LiveStream Challanges Solution Mission 017

We are provided link http://gynvael.coldwind.pl/b8263ba523af6ebd992e3782e9edd99fbdad4203_mission017/ from [Gynvael LiveStream](https://www.youtube.com/watch?v=9xGgZUMNl2Y).
<br>
Opening the link we get 
<pre>
Welcome to my secret and secure website!
It is safe and secure because it uses top notch crypto!
None of that homemade crypto stuff, but real AES-128-OFB!

Decrypted cookie data: {"access_level":"user"}

ACCESS TO THE FLAG DENIED!
Only admin has access!
</pre>

Printing the cookie we get <pre>mission017session=6VhhU05LYPoyhOCajJ9mZw%2BdSO1%2FAj4%3D</pre>.

The page already says its AES-128-OFB and this [Wikipedia](https://en.wikipedia.org/wiki/File:OFB_decryption.svg) pages explains the decryption better than i can.

Its base64 encoded, decoding it and changing some character like "user" to "aaaa" by XORing "user" ciphertext with "user" text and then XORing with "aaaa", turns out it works.

But how do we set it to "admin" as we got only 4 characters. What we have to do is add another character at end of ciphertext and bruteforce it to '}'.

So our final aim is:

* XOR 'user"}' obtained ciphertext with 'admin"'
* Add a byte at end of newly obtained ciphertext so that when it decrypts it becomes '}'
* Bruteforce it against the link provided.


#### Answer
<pre>
HMAC? What do you mean "HMAC"?
</pre>


See the [Solution_017](code.py) for the code.


Once again thank you Gynvael for this awesome challange.


# Author
Arun Kumar Shreevastava