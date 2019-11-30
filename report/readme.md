# Assessed Coursework 2 — Data Analysis of a Document Tracker

Table of contents
* [1. Introduction](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker/tree/master/report#1-introduction)
* [2. Requirements Checklist](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker/tree/master/report#2-requirements-checklist)
* [3. Design Considerations](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker/tree/master/report#3-design-considerations)
* [4. User Guide](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker/tree/master/report#4-user-guide)
* [5. Developer Guide](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker/tree/master/report#5-developer-guide)
* [6. Testing](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker/tree/master/report#6-testing)
* [7. Reflection from CW1](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker/tree/master/report#7-reflection-from-cw1)
* [8. Conclusions](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker/tree/master/report#8-conclusions)

## 1. Introduction

## 2. Requirements Checklist

| Requirement                                                                       | Achieved?     |
| --------------------------------------------------------------------------------- |:-------------:|
| Core logic of application must be in Python 3                                     | Yes           |
| Views by country and continent                                                    | Yes           |
| Views by browser                                                                  | Yes           |
| "Also likes" document suggestion functionality                                    | Yes           |
| "Also likes" graph                                                                | No            |
| GUI functionality with tkinter                                                    | Yes           |
| Command line functionality                                                        | Yes           |

All of the requirements have been completed apart from creating an "also likes" graph. 

I think, this may be changed in future I guess?

## 3. Design Considerations

## 4. User Guide

This application has two very distinct user interfaces. One is the command line interface and the other is the graphical user interface. They both allow for the same functionality, only they are done in different ways.

### Command Line Interface

The command line interface, while more complicated for everyday users, allows for quick interaction for more advanced users. It allows for typing commands to do tasks and passing parameters into the tasks. There is a limitation towards what commands can be understood by this interface. A valid command has the following structure:

```bash
% python3 cw2.py -u user_uuid -d doc_uuid -t task_id -f file_name
```

A valid command starts with python3 to tell the machine to run the application with python3, followed by the applications python file name which is cw2.py. After this what comes can be totally optional using the following commands:

* **-t**: sets the task the application will perform and allows for the following parameters:
    * *2a* - Display a histogram of countries of the viewers.
    * *2b* - Display a histogram of continents of the viewers.
    * *3a* - Display a histogram of all browser identifiers of viewers.
    * *3b* - Display a histogram of browser names of viewers.
    * *4d* - Display a list of other documents the reader may like.
    * *5* - Display a graph of relationship between a document and all documents found as also like documents.
    * *6* - Display a graph based on task *5*.
    * *7* - Display a line chart showing the frequency of views of a given document over time.

* **-f**: sets the file to be used by the application. The expected parameter is the location of the file.

* **-u**: sets a user ID that will be passed into the requested task.

* **-d**: sets a document ID that will be passed into the requested task.

* **-h** *or* **--help**: calls the help function which will display a small user guide on the command line to ensure the user is able to get help when needed. This screen can be seen here:

![--help flag output](https://raw.githubusercontent.com/CMHayden/Data-Analysis-of-a-Document-Tracker/master/report/img/commandLine--help.png?token=AFNT2CFGTUQQWWLZMOOOGD255P5KS)

### Graphical User Interface


## 5. Developer Guide

## 6. Testing

## 7. Reflection from CW1

## 8. Conclusion