# instagrab

# No longer works as the old Instagram API is now deprecated. Leaving this repo up as a demonstration of work with APIs, pagination, and data cleaning. 

**An interactive Python script to retrieve Instagram media content.**

`python instagrab.py`

Rest is pretty self-explanatory. 

Retrieves up to 33 images at a time. If the user has more than 33 images, there is a prompt to retrieve the next 33. There is a prompt to verify the final number of image downloads. A folder is created in the present directory and each of the files are stored there as `0.jpg`, `1.jpg`, and so on. 

Remember to insert your Instagram access code where it says `INSERTACCESSTOKENHERE` (line 8). You can get one here: http://instagramwordpress.rafsegat.com/docs/get-access-token/
