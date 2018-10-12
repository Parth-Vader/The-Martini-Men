# Our proposed solution:-

### We divide our post prediction solution into three parts :-

1) **Recognizing high importance zones**, i.e. segregating and prioritising disaster affected area to send help in an efficient manner. 

    - **How it works** : We provide an offline group messaging platform, redType, to the people to communicate with first responders which helps the aiders assess the immediacy of the situation.



    - **Installation** : To install the app, a user has to just tap the phone to that of another user and redType is sent from one user to another via Android Beam.

    - **Mesh Network** : To allow messages to be sent directly from device to device, users connect to all nearby devices by creating a localized mesh network which is achieved using the Android Nearby Connections API.

    - To facilitate message backup, we provide cloud integration, where in it uploads a copy of global message data to a MongoDB storage running on Azure Cloud.

    - The frequency of messages, i.e. the mesh network traffic, received by first responders in nearby zones would in turn give us the estimate of the measure of importance of a particular disaster affected region.

2) **Aid Transfer Optimization**, i.e. deciding on Aid stations where there’s sufficient help available and from where sending support would be best.

    - **How it works** : Given a network of Aid stations, we keep a track of the quantity of emergency supplies available, focussing mainly on those which are closest to high importance zones(say layer 1). Next, we identify Aid stations closest to the layer 1 stations(say layer 2) and steer all their aids towards the nearest (optimal) layer 1 stations.



    - Priority will be given to Aid stations which have support available and are closest to the Layer 1 stations and/or affected areas

    - The steps involved in this process would be to first choose an affected area (say A) whose demands are to be met, then frame the objective function and constraint equations based on the availability of supplies in a nearby Aid station, its distance from area A, cost and time involved. After getting a solution to this problem with the help of the python pulp library, we update the demand/supply data  and move on to the next affected area.

    - We continue doing this in concurrence to sending independent aid signals(for government help) from layer 1 stations.

3) **ETA with the help of redType** : 
