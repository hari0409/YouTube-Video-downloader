# YouTube-Video-downloader  
A simple youtube video downloaded will a some use full functionality  

When you run the file this window will pop out!  
![image](https://user-images.githubusercontent.com/73524123/118356556-799bb680-b593-11eb-87cf-545e2f2d222c.png)  
Enter the url of the video link in the box  
Choose the location where the video must be stored  
![image](https://user-images.githubusercontent.com/73524123/118356658-f75fc200-b593-11eb-8534-8012104c7a3f.png)  
It will display the path in green  
Select the resolution to be downloaded  
![image](https://user-images.githubusercontent.com/73524123/118356678-0e9eaf80-b594-11eb-873e-66638acf17f4.png)  
Before selecting ensure you have selected a available resolution  
First download the audio  
wait untill the download is comlpete,while downloading the python window will be "Not Responding" but dont close the window  
After the audio download is complete it will display the following message  
![image](https://user-images.githubusercontent.com/73524123/118356730-4e659700-b594-11eb-8474-81bb1a1cdd4a.png)  
Click on download video  
It will print the resolution you have clicked and start downloading the video  
You will hear a beep sound for 2 second after the download is completed (You can remove it if you find it annoying)  
Then close the window (Not the Terminal) ---VERY IMPORTENT  
Then input the name the video has to be stored as and also with no spaces --IMPORTENT  
![image](https://user-images.githubusercontent.com/73524123/118356927-1743b580-b595-11eb-81d3-17e4c5190fce.png)  
Then the audio and video will mergerd with ffmpeg to give you the output which will be available in the location you specified  
You will see the below  
![image](https://user-images.githubusercontent.com/73524123/118356968-4823ea80-b595-11eb-861b-8cdf90ad818a.png)  
And make sure it end similar to this  
![image](https://user-images.githubusercontent.com/73524123/118356987-612c9b80-b595-11eb-8613-b7e8ca1f5119.png)  
Which depends on the video you download  
Now the video wold have been stored in your given location  
By default the audio is deleted but you can also save it by un-commenting these lines  
![image](https://user-images.githubusercontent.com/73524123/118357229-a4d3d500-b596-11eb-99e1-b435b8e98f37.png)  
You can also change the audio format here  
![image](https://user-images.githubusercontent.com/73524123/118357244-c2a13a00-b596-11eb-97e0-00d73cc004ba.png)  
#NOTE:  
You must have already downloaded ffmpeg and must have add it as an environmental variable  
FFMPEG help in merging the audio with video cuz of DASH delivering system of YouTube   
->Know More : [DASH](https://developers.google.com/youtube/v3/live/guides/encoding-with-dash)  
Download FFMPEG from [FFMPEG](https://github.com/BtbN/FFmpeg-Builds/releases)  
The below version or any updated one.  
![image](https://user-images.githubusercontent.com/73524123/118357385-815d5a00-b597-11eb-833c-3b2bccad4b51.png)  
Thank You....✌✌  
  
