# Our Proposed Solution :-

## Website : http://redtype.azurewebsites.net/

## Prediction : 

### Monitoring disasters using 

**UAVs :** Drones equipped with camera sensors which produce aerial photos of the affected area could help us recognize unsteady conditions using Deep Learning techniques. 
<br>
*For example,* in case of a flood :
<br>
In addition to spotting people in need of help, drones will be able to predict further flooding, and help provide estimates of how long certain areas would be underwater.
<br><br>
**Images from Social Media :** As our lives get immensely integrated with social media in general, a lot of information about any on going situation can be derived from it. 
<br>
Images collected are sent to the server for remote processing. 
Here, we use the **Microsoft Azure Custom Vision API** to analyse the images and predict the probability of the same coming from an area which has been hit by a natural disaster recently. As of now our model is only trained on flood labeled images but it can be extended to situations depicting wildfire, earthquakes and landslides.
<br><br>
![img3](https://raw.githubusercontent.com/anshu1997/The-Martini-Men/master/img3.jpg?token=APhACHwKe1PbR97TDNfcHdENZBMja_Grks5b1xd5wA%3D%3D)


### Forecast from Global NASA data :
With the help of information extracted from NRT Global Flood Mapping we can get the approximate latitude and longitude measurements of areas which have imminent danger due to flood. The high-risk flood zones from NASA satellites which are updated every 24 hrs, are displayed on the redDash map. 


## Post Prediction : 
**redType :** We provide a simple chat system for the victim as well as the rescuer so that they can effectively communicate with each other, even without internet connectivity. *redType* is an Android app with basic SMS functionality brought to life through the **Twilio API**. 
<br>During time of emergency, it would help victims send SOS messages to our Helpline number along with the Location of the sender. The Helpline admin can then reply through our interface back to the victim, stating the course of the rescue operation.


![img4](https://raw.githubusercontent.com/anshu1997/The-Martini-Men/master/img4.jpg?token=APhACHwKe1PbR97TDNfcHdENZBMja_Grks5b1xd5wA%3D%3D)


<hr />

### Future Work :
#### We intend to focus on three most important extensions of this project in near future :-


1) **Recognizing high importance zones**, i.e. segregating and prioritising disaster affected area to send help in an efficient manner. 

    - **How it works** : Provide an offline group messaging platform, along with redType, to the people to communicate with first responders which helps the aiders assess the immediacy of the situation.

    
![img1](https://raw.githubusercontent.com/Parth-Vader/The-Martini-Men/master/img1.jpg?token=APhACHwKe1PbR97TDNfcHdENZBMja_Grks5b1xd5wA%3D%3D)

    - **Mesh Network** : To allow messages to be sent directly from device to device, users connect to all nearby devices by creating a localized mesh network which is achieved using the Android Nearby Connections API.

    - *The frequency of messages,* i.e. the mesh network traffic, received by first responders in nearby zones would in turn give us the estimate of the measure of importance of a particular disaster affected region.


2) **Aid Transfer Optimization**, i.e. deciding on Aid stations where there’s sufficient help available and from where sending support would be best.

    - **How it works** : Given a network of Aid stations, we keep a track of the quantity of emergency supplies available, focussing mainly on those which are closest to high importance zones(say layer 1). Next, we identify Aid stations closest to the layer 1 stations(say layer 2) and steer all their aids towards the nearest (optimal) layer 1 stations.
    
![img2](https://raw.githubusercontent.com/Parth-Vader/The-Martini-Men/master/img2.jpg?token=APhACKOS9yZ7sgFhCW2dtz4-KRo_gRd4ks5b1xejwA%3D%3D)
    - Priority will be given to Aid stations which have support available and are closest to the Layer 1 stations and/or affected areas

3) **ETA with the help of redType** : i.e. provide an estimate of when help will reach the victims based on the developed conditions of the surroundings.
    - It would take into account the preparation time at each Aid station, mode of transport used and the distance (taking the most preferable route) from the affected area, given the circumstances.
    - The estimate could also help the first responders know how much time they would take to reach the victims and speeden their actions accordingly
