# Image challenge

Someone decided to hide the picture from view and encrypted it! Restore the original image, return the painting to the people.

The original picture is a 32x32 color image in the RGB format. It is presented as an array of length 3072, where first 1024 integers correspond to the red component, then go the green values, the last 1024 are blue. The attacker split the array into 12 equal parts and encrypted each one separately, using OpenFHE library and CKKS scheme. 

As input you will receive ordered encrypted pieces of the image, cryptocontext and public key. All files are in data.zip. The purpose of this bounty is to get the original array back.


