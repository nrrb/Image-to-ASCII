This is a script that uses the Python Imaging Library to rasterize image files into ASCII art text files. It chooses characters by average brightness over the character box. 

Input
-----
![saxbig](https://raw.github.com/tothebeat/Image-to-ASCII/master/saxbig.gif)

Output
------

````
Dark Background:
gdddddddddddddddddddddddddddddddddddd      ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddd`                          `dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddddddddd        MMMMMMMMMMMMMMMMMMMMMM        dddddddddddd`          dddddddddddddddddddddddddddddddddddddd
ddddddddddddddddd      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     `dddddd    MMMMMMMM    `dddddddddddddddddddddddddddddddddd
dddddddddddddd     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     dd   MMMMMMMMMMMMM    dddddddddddddddddddddddddddddddd
dddddddddddd    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     MMMMMMMMMM      MMM      MMMMMMM    dddddddddddddddddddddddddddddd
ddddddddd`    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM      MMMMMMMMMMM          `     MMMMMM    ddddddddddddd`              
dddddddd    MMMMMMMMMMMMMMMMMMMM     MMMMMMMMMMMMM   MMMMMMMMMMM        dddddddd   MMMMMMM   `dddddd          MMMMMMMM  
dddddd    MMMMMMMMMMMMMMMMMMMMMM      MMMMMMMMMMMMMMMMMMMMMM              ddddddd   MMMMMMM    ddddd   MMMMMMMMMMMMMMM  
ddddd    MMMMMMMMMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMMMM          MMMM    ddddd    MMMMMMMMM   `d    MMMMMMMMMMMMMMMM  
dddd   MMMMMMMMMMMMMMMMMMMMMMMMMMMM  MMMMMMMMMMMMMM            MMMMMMMMMM   dd    MMMMMMMMMMMMM     MMMMMMMMMMMMMMMMMM  
ddd   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                      MMMMMMMMMMMMMMMM      MMMMMM   MMMMMMMMMMMMMMMMMMMMMMMMMMMMM  
dd   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM             MMMMMMMMMMMMM  MMMMMMM                MMMMMMMMMMMMMMMMMMMMMMMMMMMMM  
d    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                 dddddd`   MMMMMMMMMMMMMMMMMMMMMMMMMMMM  
d   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   MMMMMMMM   dddddddd   MMMMMMMMMMMMMMMMMMMMMMMMMMMM  
d   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   ddddddddd    MMMMMMMMMMMMMMMMMMMMMMMMM   
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   `dddddddddd    MMMMMMMMMMMMMMMMMMMMMMM   
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   `dddddddddddd     MMMMMMMMMMMMMMMMMM    d
d   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   dddddddddddddddd       MMMMMMMMM      ddd
d   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   ddddddddddddddddddddd`            ddddddd
d^   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   `ddddddddddddddddddddddddddddddddddddddddd
dd    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    dddddddddddddddddddddddddddddddddddddddddd
ddd   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   ddddddddddddddddddddddddddddddddddddddddddd
dddd   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   dddddddddddddddddddddddddddddddddddddddddddd
ddddd    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ddddddddddddddddddddddddddddddddddddddddddddd
dddddd    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    dddddddddddddddddddddddddddddddddddddddddddddd
dddddddd    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    dddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddd    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    dddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddd     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     dddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddd     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     ddddddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddd      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM      dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddddd^            MMMMMMMMMMMMMMMMMMMM          dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddddd    dddddd^                        ^      ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddddd   ddddddddddddddddddddddddddddddddddd    ddddd    dddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddddd^       dddddddddddddddddddddddddddddddd            ddddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddd        ddddddddddddddddddddddddddddddddd^       ddddddddddddddddddddddddddddddddddddddddddddddddddddd
````

````
Light Background:
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MMMMMM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<WMMMMMMMMMMMMMMMMMMMMMMMMMMW<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<MMMMMMMM                      MMMMMMMM<<<<<<<<<<<<WMMMMMMMMMM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<MMMMMM                                  MMMMMW<<<<<<MMMM        MMMMW<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<MMMMM                                          MMMMM<<MMM             MMMM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<MMMM                                 MMMMM          MMMMMM   MMMMMM       MMMM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<WMMMM                                   MMMMMM           MMMMMMMMMMWMMMMM      MMMM<<<<<<<<<<<<<WMMMMMMMWWWWWWW
>>>>>>>>WWWW                    WWWWW             WWW           WWWWWWWW>>>>>>>>WWW       WWWN>>>>>>WWWWWWWWWW        WW
>>>>>>WWWW                      WWWWWW                      WWWWWWWWWWWWWW>>>>>>>WWW       WWWW>>>>>WWW               WW
>>>>>WWWW                        WWW                     WWWWWWWWWW    WWWW>>>>>WWWW         WWWN>WWWW                WW
>>>>WWW                            WW              WWWWWWWWWWWW          WWW>>WWWW             WWWWW                  WW
>>>WWW                              WWWWWWWWWWWWWWWWWWWWWW                WWWWWW      WWW                             WW
>>WWW                                 WWWWWWWWWWWWW             WW       WWWWWWWWWWWWWWWW                             WW
>WWWW                                                          WWWWWWWWWWWWWWWWW>>>>>>NWWW                            WW
>WWW                                                             WWW        WWW>>>>>>>>WWW                            WW
>WWW                                                                        WWW>>>>>>>>>WWWW                         WWW
WWWW                                                                        WWWN>>>>>>>>>>WWWW                       WWW
WWWW                                                                        WWWN>>>>>>>>>>>>WWWWW                  WWWW>
>WWW                                                                        WWW>>>>>>>>>>>>>>>>WWWWWWW         WWWWWW>>>
>WWW                                                                        WWW>>>>>>>>>>>>>>>>>>>>>NWWWWWWWWWWWW>>>>>>>
>#WWW                                                                      WWWN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>WWWW                                                                    WWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>WWW                                                                    WWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>WWW                                                                  WWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>WWWW                                                              WWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>WWWW                                                            WWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>WWWW                                                        WWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>WWWW                                                    WWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>WWWWW                                              WWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>WWWWW                                        WWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>WWWWWW                                WWWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>#WWWWWWWWWWWW                    WWWWWWWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>WWWW>>>>>>#WWWWWWWWWWWWWWWWWWWWWWWW#WWWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>WWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WWWW>>>>>WWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>#WWWWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WWWWWWWWWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>WWWWWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#WWWWWWW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
````
