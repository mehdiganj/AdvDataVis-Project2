# Advanced Data Visualization - Electric Bus Deployment
Visualization for project #2

## Installation

The tool needs to be run using a local server. Node.JS is recommended

1. Install Node.JS
2. Using the terminal/command prompt, run the command: 

```bash
npm install --global http-server
``` 
3. Once installed, locate the project folder in the terminal, then run: http-server
4. Open the server IP address into the web browser to open the index, then select Main.html

Detailed step by step is shown in the video explanation, which can be found at https://youtu.be/URBzca6angw (uploaded as Unlisted and it can only be accessed with this link)

## Introduction
The objective of this project is to create an interactive visualization prototype of electric bus
deployment data using D3.js.

D3.js is a JavaScript library for producing dynamic, interactive data visualizations in web browsers.

The clients of this projects are domain scientists (Cathy Liu, Jianli Chen, Yirong Zhou from the Department of Civil \& Environmental Engineering) who work on smart city design.
The input data for this project is created based on battery-electric buses (BEB) optimization deployment considering cost and environmental equity for disadvantaged population.
The input dataset for each plan is obtained from https://trid.trb.org/view/1862847
The output data of the optimization problem as:

\begin{itemize}
    \item Locations and number of both in-depot and on-route charging stations
    \item Number of buses to be replaced
    \item The exact buses to be replaced
\end{itemize}

The Utah Transit Authority (UTA) is selected as case study for this project and three different plans with various budgets (\$25M for plan 1, \$60M for plan 2, and \$120M for plan 3) are taken into account.


We used the result of the optimization problem as input data in order to design a web page and enable user interaction using D3.js as the main objective of the project.

