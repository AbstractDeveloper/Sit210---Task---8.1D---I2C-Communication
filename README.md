Task 8.1D Raspberry Pi I2C 

Hardware Required -
Raspberry Pi, BH1750 Ambient sensor (or another temperature sensor capable of being 
used with I2C, or even another SoC device e.g. Particle Photon, Arduino)


Software Required -
Python IDE (or IDE for the programming language you are using)


Pre-requisites: You must do the following before this task
None


Task Objective -
The aim of the task is to build an I2C application. The application can vary depending on 
what sensor you are using. For example, if you are using ambient light sensor, to read the 
environment light intensity using I2C. If you are using another I2C, perhaps to send a 
value/mock data across to the other device. 


Steps: 
1. Design a simple circuit board connecting the ambient sensor (or anything else you 
are using) to the I2C pins of the Raspberry Pi. 
2. Write code that configures the sensor, reads data and prints out the results as 
categories of “too bright”, “bright”, “medium”, “dark” and “too dark” (or displays mock 
data).
