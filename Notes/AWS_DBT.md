### sturcture of code
![Screen Shot 2021-06-08 at 15 49 52](https://user-images.githubusercontent.com/61960385/121148654-4e9c3e00-c885-11eb-95b1-60839b9bf895.png)

in .aws, we setup the config (ecs role) to have permissions without using password.
![Screen Shot 2021-06-08 at 15 44 11](https://user-images.githubusercontent.com/61960385/121148801-6f649380-c885-11eb-8f0b-b5c28abc292e.png)

- In .dbt, we setup db info/variables without sensitive password.
- In entrypoint, we interpolate those variables in dbt yaml files from airflow to image.
- In dockerfile, we install dbt package, copy files, setup env variables and excute entrypoint.sh
![Screen Shot 2021-06-08 at 15 51 25](https://user-images.githubusercontent.com/61960385/121149699-3bd63900-c886-11eb-96fa-939d8432ec8c.png)
<img width="399" alt="Screen Shot 2021-06-09 at 11 23 12" src="https://user-images.githubusercontent.com/61960385/121281128-c5374b00-c91a-11eb-8e60-0c3af63649a4.png">
<img width="783" alt="Screen Shot 2021-06-09 at 12 03 09" src="https://user-images.githubusercontent.com/61960385/121281134-c799a500-c91a-11eb-852e-5bcddbf9c4a3.png">
