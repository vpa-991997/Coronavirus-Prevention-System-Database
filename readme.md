 # Coronavirus Prevention System :space_invader:
 
## This project seeks to provide a solution by leveraging Artificial Intelligence :desktop_computer: to scan the area for both people wearing and not wearing masks, providing a mask to those not wearing one, and logging events for statistical tracking purposes.

### :heavy_check_mark:Our Motivation 
![image](https://www.tfhd.com/sites/default/files/styles/news_banner/public/news/TFHS_COVID-19_News_1170x591_Draft1.jpg?itok=uOqtXuwm)

:bangbang: COVID- 19 has been spreading quickly since November 2019. More than 400,000 people have lost their lives

‼️ WHO and public health officials recommend wearing mask and social distancing of 6-feet or more to reduce the risk of transmission

‼️ We wanted to build a low cost and effective robot that uses machine learning to detect faces of people without masks. Automatically open its storage compartments for non-mask wearing person to get a face mask 


### :heavy_check_mark:Our Objectives
‼️ Aims to provide a cost-effective and easy to use system to distribute single-use masks 

‼️ Rely on simple tried-and-true components and designs

‼️ Two main functions: Detection & Data collection. By gathering user data, we will be able to prepare user statistics on health and behaviors


### :heavy_check_mark:Our System Overview
**LAMP Stack**
- Linux (The Operating System): Serves as the first layer for this stack model. Linux is free and open-source operating system, which provide flexibilities and configuration options to run our server.
- <s>Apache (The Web Server)</s>: Since we are planning to host the database locally, we do not use the Apache to deliver the website on the internet.
- MySQL (The Database): MySQL is known as open-source relational database management system for storing information. This will be the second layer for our model, that will store the data, and deliver the information as requested.
- Python (The Programming Language): We use Python as our primary scripting language to create dynamic database server. 

### :heavy_check_mark:Our Database System
- Person_id (int) : auto_increment 
- Mask (boolean type)
- Date_time (datetime type)

After 128 frames captured the person coming toward the camera within distance, every person in the video will be labeled 
as “Mask” or “No Mask”, which will be recorded in the metadata file. This data file is imported to MySQL database with
“PersonID” will be the primary key to distinguish with the preexisting data. “PersonID” is “AUTO_INCREMENT”, which 
allows us to generate unique number automatically when a new data record is added into the table, following by “Mask”, will be 
stored in Boolean type: Mask: 1 and No-mask: 0. To store date and time information, we use SQL datetime type in order to define specific time a person has experience mask detection system.

### :heavy_check_mark:Our GUI Application
- Used Python GUI framework Tkinter which is fast and easy to make funtional GUI within 2 months
- This is User-friendly App for different purposes:
  - Show databses
  - Display data based on different date
  - Can be used for analytical purposes in the future!


