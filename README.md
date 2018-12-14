# Touch Screen Relay Panel
In this project I've designed and built a relay control panel based on the raspberryPi board and 3.5" touchscreen. \
The project is designated for 12v systems such as cars and small trucks. Using the touchscreen, the user can define
what are the accessories he wish to control and also decide on the representation on the display screen. \
To implement this project the user should be lightly familiar with Python and Linux OS, and have basic knowledge in
electronics. \
In this work I've used 8ch relay board and actually controlling 6ch (due to wire selection).

<!---[main](https://user-images.githubusercontent.com/25335836/49975742-11dd6f00-fef4-11e8-8532-9836decbe74b.jpg)--->

![main](https://user-images.githubusercontent.com/25335836/49976497-22431900-fef7-11e8-9296-b024fbd926c4.gif)

## Materials and equipment
The materials that was used in this project are:
1. [RaspberryPi 3b+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
2. [5v 8ch relay board](https://www.amazon.com/SainSmart-101-70-102-8-Channel-Relay-Module/dp/B0057OC5WK)
3. [DIP Switch - 8 Position](https://www.sparkfun.com/products/8034)
4. 12v step-down converter (12v --> 5v) ([for example](https://www.amazon.com/eBoot-LM2596-Converter-3-0-40V-1-5-35V/dp/B01GJ0SC2C/ref=asc_df_B01GJ0SC2C/?tag=hyprod-20&linkCode=df0&hvadid=167122786755&hvpos=1o4&hvnetw=g&hvrand=13176459983025186939&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9032081&hvtargid=pla-305123447649&psc=1)) 
5. 3D printer to print the case and cover
6. 8 or more cord cable
7. soldering and isolating equipment


## Preparing the raspberryPi
1. Before starting using the raspberryPi please follow the instructions [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up). 
In this work we will use the NOOBS installer with **Raspbian**.
2. Prepare the touchscreen using it's own instructions. \
    I used 3.5" TFT touchscreen from [Kuman](https://www.amazon.com/Kuman-320x480-Resolution-Protective-Raspberry/dp/B01FXC5ECS/ref=sr_1_1?ie=UTF8&qid=1544734613&sr=8-1&keywords=kuman+3.5%22).
    To install that touch screen I needed to run the following command in the terminal:
    ```
    git clone https://github.com/goodtft/LCD-show.git
    ```
    ```
    chmod -R 755 LCD-show    
    ```
    ```
    cd LCD-show/
    ```
    ```
    sudo ./LCD35-show
    ```
    After rebooting the touchscreen will start functioning.
    
3. Create new folder named `TouchScreenRelayPanel` and copy all the files from the 
(git repo)[https://github.com/ronberenstein/TouchScreenRelayPanel] to the folder. \
Alternative method is to use git:
    ```
    git clone https://github.com/ronberenstein/TouchScreenRelayPanel.git
    ``` 
4. Install guizero. Open new terminal (Ctrl+t) and enter:
   ```
   sudo pip3 install guizero
   ```
5. After Raspbian is installed we will need to add the main program (main.py) to the raspberryPi autostart using crontab ([tip](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up)). \
Open new terminal (Ctrl+t) and enter the following command:
    ```
    sudo crontab -e
    ```
    Select to open using nano. Add the following line to the end of the file:
    ```
    @reboot python3 /home/pi/Desktop/main.py &
    ```
    close and save using Ctrl+x and enter Y.

At this point the program should run every time the raspberryPi is starts.

## Building the case
The raspberryPi+touchscreen case was created using 3D printing. CAD+STL files of the can be found [here](ADD!!!!!!!!!!!)
Alternative cases can be built using traditional techniques, or using of-the-shelf electrical boxes.

## Electrical diagram
We use the raspberryPi GPIO pins to control the relay board. \
I used 8 cord cable (Ethernet CAT6 cable). 2 cords are dedicated to the 5v and ground inputs, leaving 6 cords for controlling the relay. By
using 10 cord cable, all 8 relay channel can be utilize.
The electrical connection are as follows:

![electric connections diagram](https://user-images.githubusercontent.com/25335836/49975123-59aec700-fef1-11e8-934d-552a25336d1f.png)


## Possible modifications
By replacing the images of the button, new type of button can be created.


## Points for discussion
1. I believe that the project can also be implemented using the raspberryPi zero.
