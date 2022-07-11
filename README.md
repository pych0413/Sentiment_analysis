Sentiment Analysis by YOLOv5 display in Streamlit
======
![img1](/src/project_map.png)
This project is about Sentiment Analysis. It collect the data in Google and [Pexels](https://www.pexels.com/). After the collection, annotate the data in [Roboflow](https://app.roboflow.com/). Then, train the Sentiment Analysis model by [YOLOv5](https://github.com/ultralytics/yolov5). Finally, use the [Haar-cascades](https://github.com/opencv/opencv/tree/master/data/haarcascades) to detect the face and analyse the sentiment by the trained YOLOv5's model. [Streamlit](https://streamlit.io/) has been used to display whole the process.   
______ 

Requirement
------
+ Windows 11
+ Download [Anaconda](https://www.anaconda.com/) ( version 1.9.0 + )
+ Web Browser (Google Chrome or other)  
______

Setup a development environment
------
> ### Go to the environment.  
> ![ac1](/src/anaconda_1.jpg)

> ### Create the new environment.  
> ![ac2](/src/anaconda_2.jpg)

> ### Select the Python 3.9.12+.  
> ![ac3](/src/anaconda_3.jpg)

> ### Open the Terminal.  
> ![ac4](/src/anaconda_4.jpg)

> ### Go to the path of the GitHub file.
>> cd ***Your_file_path***  
>> pip install -r requirements.txt  
>
> ![ac5](/src/anaconda_5.jpg)
  

______
Display the model in web app (Streamlit)
------
> ### Open the web app in Terminal.
>> app.bat
>
> ![ac6](/src/anaconda_6.jpg)  

> ### Import the jpg photo.  
> ![sl1](/src/streamlit_1.jpg)  

> ### See the Face detected result by Haar-cascades and click the Sentiment Analysis to analyse the sentiment.  
> ![sl2](/src/streamlit_2.jpg)  

> ### It displays the Sentiment analysis result and you can download the result by the '***Download image***' button.  
> ![sl3](/src/streamlit_3.jpg)  

