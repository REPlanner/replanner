
import airsim
import cv2
import numpy as np
import os
import pprint
import threading
import tempfile

num_drones=3

ids=["Drone"+str(i+1) for i in range(num_drones)]
print(ids)

client = airsim.MultirotorClient()
client.confirmConnection()
airsim.wait_key('Press any key to takeoff')
f=[]
for i in ids:
    client.enableApiControl(True, i)
    client.armDisarm(True, i)
    f.append(client.takeoffAsync(vehicle_name=i))
for t in f:
    t.join()
f=[]
airsim.wait_key('Press any key to start')

path="C:\\Users\\AcydLAB\\Documents\\path_points"
file1=open(path+ "\\NewUAV1.txt", "r").readlines()
file2=open(path+ "\\NewUAV2.txt", "r").readlines()
file3=open(path+ "\\NewUAV3.txt", "r").readlines()
i=0
j=0
k=0

while(i != len(file1) and j != len(file2) and k != len(file3)):
    if i != len(file1):
        pos=file1[i].split()
        c=client.moveToPositionAsync(.9*float(pos[0]), .9*float(pos[2]), -15, 10,vehicle_name="Drone1")
        c.join()
        i+=1
    if j != len(file2):
        pos=file2[j].split()
        c=client.moveToPositionAsync(float(pos[0]), float(pos[2]), -15, 10, vehicle_name="Drone2")
        c.join()
        j+=1
    if k != len(file3):
        pos=file3[k].split()
        c=client.moveToPositionAsync(float(pos[0]), float(pos[2]), -15, 10, vehicle_name="Drone3")
        c.join()
        k+=1

airsim.wait_key('Press any key to reset to original state')
for i in ids:
    client.armDisarm(False, i)
client.reset()
for i in ids:
    client.enableApiControl(False,i)
