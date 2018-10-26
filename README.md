# Project 1 ECEN 689 Fall 2018:  Determining Correlations Between United States’ Health and Income Data



Project 1 for ECEN 689 course involved gathering health and income data for the United States.
The project also involved parsing through the data, and ensuring accurate representation of U.S. counties.
The project’s objective was to determine if health parameters ( obesity, diabetes, etc) were correlated with income data collected by the IRS (Internal Revenue Service).

---

## Datasets used

The first dataset is  “Food Environment Atlas”. Food environment factors interact to influence food choices and diet quality. 
The objectives of the Food Atlas, made available by the U.S. Department of Agriculture, are to assemble statistics on food environment indicators and to provide a spatial overview of access to healthy food. The atlas contains health and well-being indicators such as diabetes and obesity rates.

The current version of the Food Environment Atlas has over 275 variables, including new indicators on access and proximity to a grocery store for sub populations; an indicator on the SNAP Combined Application Project for recipients of Supplemental Security Income (at the State level). Indicators on farmers' markets that report accepting credit cards or report selling baked and prepared food products. Data was used for the years 2008 and 2013.
The second dataset is “County Income Tax Statistics”. The Internal Revenue Service (IRS) is the revenue service of the United States federal government. 
It is responsible for collecting taxes and administering the Internal Revenue Code. Public information includes individual tax statistics for 2016, grouped by FIPS code.

--- 

## Obesity, Diabetes, Adjusted Gross Income (AGI) data projection on the United States' map

* Diabetes  map in 2008

![alt text](https://github.com/khalednakhleh/ecen689_project1/blob/master/graphs/diabetes_2008.png "diabetes map 2008")

* Diabetes map in 2013

![alt text](https://github.com/khalednakhleh/ecen689_project1/blob/master/graphs/diabetes_2013.png "diabetes map 2013")


* Obesity map in 2008
![alt text](https://github.com/khalednakhleh/ecen689_project1/blob/master/graphs/obesity_2008.png "obesity map 2008")

* Obesity map in 2013

![alt text](https://github.com/khalednakhleh/ecen689_project1/blob/master/graphs/obesity_2013.png "obesity map 2013")


* AGI map in 2013

![alt text](https://github.com/khalednakhleh/ecen689_project1/blob/master/graphs/agi.png "agi map 2013")



--- 

## Packages used

I used [Plotly](https://plot.ly) to generate the United States' maps. Using the offline graph generator, the software generates an HTML file saved locally that displays the maps on your browser. HTML files are available in the repository.















