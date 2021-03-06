"""
从divide_by_car文件夹中的文件中提取1000辆车的轨迹数据
"""

import numpy as np

linux_path = "/root/taxiData"
windows_path = "K:\毕业论文\TaxiData"
mac_path = "/Volumes/MyZone/毕业论文/TaxiData"
base_path = linux_path

taxi_size = 500

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-20.npy").item()
taxi_ids = []

new_trajectories = {}
for key in trajectories_by_car.keys():
    if len(taxi_ids) > taxi_size:
        break

    taxi_ids.append(key)
    new_trajectories[key] = trajectories_by_car[key]

np.save("taxi_ids", taxi_ids)

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-20_simplified", new_trajectories)
print("got 2014-10-20")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-21.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-21_simplified", new_trajectories)
print("got 2014-10-21")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-22.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-22_simplified", new_trajectories)
print("got 2014-10-22")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-23.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-23_simplified", new_trajectories)
print("got 2014-10-23")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-24.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-24_simplified", new_trajectories)
print("got 2014-10-24")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-25.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-25_simplified", new_trajectories)
print("got 2014-10-25")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-26.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-26_simplified", new_trajectories)
print("got 2014-10-26")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-27.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-27_simplified", new_trajectories)
print("got 2014-10-27")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-28.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-28_simplified", new_trajectories)
print("got 2014-10-28")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-29.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-29_simplified", new_trajectories)
print("got 2014-10-29")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-10-31.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-10-31_simplified", new_trajectories)
print("got 2014-10-31")



trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-01.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-01_simplified", new_trajectories)
print("got 2014-11-01")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-02.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-02_simplified", new_trajectories)
print("got 2014-11-02")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-03.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-03_simplified", new_trajectories)
print("got 2014-11-03")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-04.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-04_simplified", new_trajectories)
print("got 2014-11-04")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-05.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-05_simplified", new_trajectories)
print("got 2014-11-05")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-06.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-06_simplified", new_trajectories)
print("got 2014-11-06")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-07.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-07_simplified", new_trajectories)
print("got 2014-11-07")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-08.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-08_simplified", new_trajectories)
print("got 2014-11-08")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-09.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-09_simplified", new_trajectories)
print("got 2014-11-09")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-10.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-10_simplified", new_trajectories)
print("got 2014-11-10")


trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-11.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-11_simplified", new_trajectories)
print("got 2014-11-11")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-12.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-12_simplified", new_trajectories)
print("got 2014-11-12")

trajectories_by_car = np.load(base_path + "/divide_by_taxi/car_trajectory_2014-11-13.npy").item()

new_trajectories = {}
for key in taxi_ids:
    if key in trajectories_by_car:
        new_trajectories[key] = trajectories_by_car[key]

np.save(base_path + "/divide_by_taxi/car_trajectory_2014-11-13_simplified", new_trajectories)
print("got 2014-11-13")