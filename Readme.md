# Data Analysis of a Document Tracker

The aim of this coursework is to develop a simple, data-intensive application in Python 3. This is a pair project which will be undertaken by Ridwan Mukhtar and I. 

## Table of Contents

* [Overview](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker#overview)

* [Lab Environment](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker#lab-environemnt)

* [Requirements](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker#requirements)

* [Report Format](https://github.com/CMHayden/Data-Analysis-of-a-Document-Tracker#report-format)

## Overview

The learning objective of this coursework is to develop proficiency in advanced programming concepts, stemming from both object-oriented and functional programming paradigms, and to apply these programming skills to a concrete application of a moderate size. Design choices regarding languages, tools, and libraries chosen for the implementation need to be justified in the adjoining report.

This coursework will develop personal abilities in using modern scripting languages as a "glueware" to build, configure and maintain a moderately complex application, and deepen the understanding of integrating components on a Linux system.

The report needs to critically reflect on the software used for implementing this application, and discuss advantages and disadvantages of this choice. The report should also contain a discussion, contrasting software development on Windows and Linux systems and comparing software development in scripting vs. systems languages (based on the experience from the two pieces of coursework).

## Lab Environemnt

Software environment: You should use Python 3 as installed on the Linux lab machines (EM 2.50) for the implementation. This installation also provides the pandas, tkinter, and matplot libraries.

If you want to develop the software on your own laptop you need to install the above software. Both Python and the libraries are available for download at: https://www.python.org/download.

For each of the chosen technologies, the report should discuss why it is the most appropriate choice for this application, and possible alternatives should be mentioned.

## Requirements

| Requirement                                                                       | Achieved?     |
| --------------------------------------------------------------------------------- |:-------------:|
| Core logic of application must be in Python 3                                     | No            |
| Views by country and continent                                                    | No            |
| Views by browser                                                                  | No            |
| "Also likes" document suggestion functionality                                    | No            |
| "Also likes" graph                                                                | No            |
| GUI functionality with tkinter                                                    | No            |
| Command line functionality                                                        | No            |

### Core logic of application must be in Python 3

Logic must be done with Python 3. Some suggested libraries include *json library* for parsing data, *[pandas](https://pandas.pydata.org/)* for processing the input data, *[tkinter](https://docs.python.org/2/library/tkinter.html)* for creating the GUI and *[matplot](https://matplotlib.org/)* for visualizing the results. *[Graphviz](https://www.graphviz.org/)* package is also recommended for translating *.dot* formats to *.ps*.

### Views by country and continent

We want to analyse the data in terms of country and continent. The application should take a string as input which identifies a document (*UUID*), and return a histogram of the views by country. Using this data, we want to also group the countries by continents and generate a new histogram.

### Views by browser

We want to identify the most popular browser. We must examine the *visitor_useragent* field and count the number of occurrences for each value. It should return a histogram of all browser identifiers of the viewers. Finally, we must process the data and display a histogram using the browser name (eg, chrome or mozilla) instead of name, version and OS. 

### "Also likes" document suggestion functionality

For a given document, we want to identify other documents which have been read by this documents readers. To achieve this we will create a function which takes a document *UUID* and returns all visitor *UUID*s to gather the user ID's of readers of a document. We will then create a function that takes a visitor *UUID* and returns all document *UUID*s that have been read by the user. The also likes function will use this data to return a list of liked documents. This is then sorted based on **the number of readers of the same document**. A list is returned with the top 10 documents as a result.

### "Also likes" graph

### GUI functionality with tkinter

### Command line functionality

## Report Format

The report should be ten to fifteen pages long. Appendix is not included in page limit and may be used for screenshots. This is the format the report should follow:

* **Introduction** state the purpose of the report, the design remit, and any assumptions made. 

* **Requirements' Checklist** should clearly show which requirements were achieved and which were not.

* **Design Considerations** should clearly state what was done to ensure the application is useable and accessible.

* **User Guide** should include screenshots of running application along with text descriptions to help a user use the application.

* **Developer Guide** should include a description of the application design and main areas of code. May be beneficial to include code fragments.

* **Testing** should show the results for testing all cases and prove that the outputs are what are expected. Report any errors.

* **Reflections on programming language and implementation** should be a reflection of the language features and technologies which have been helpful in developing the application. It should identify the limitations of the application and suggest ways to overcome the limitations. Reflection on the type of language for this application domain and it's wider application.

* **What did I learn from CW1?** should be a discussion on how feedback from CW1 made this CW be approached differently.

* **Conclusions** should be a reflection on what we are proud of with the application and what we would have liked to do differently.

* **References** essentially just a bibliography.
