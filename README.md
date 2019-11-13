# University of Edinburgh Psychology Statistics Course Content  

In each course directory, there are subdirectories for lectures, labs, and lab_solutions (where necessary).  
  

Any finished **and rendered**  materials should be placed in the /docs directory.  
A github page is built from this repository, meaning that any .htmls are rendered appropriately. (in the future, /docs could be replaced by submodule of proper site such as Milan's one).  
In a browser, navigating to [https://uoe-psychology.github.io/uoe-psystats](https://uoe-psychology.github.io/uoe-psystats) followed by your files location within /docs will show you your file.  
There is an index.html, but to update this you need to run the makeindex.py script on /docs.  

 
Currently, different courses have content written/compiled in different ways.  
The majority are written in .rmd, and compiled either as a bookdown or with the teachR package.   
> devtools::install_github("UoE-Psychology/teachR")  
  

## DAPR1  
### Lectures  
.rmd, knitted with teachR package.  

### Labs  
.rmd, knitted as bookdown.  
  

## DAPR2  
 
## DAPR3  
 
## Univariate  
### Lectures  
Currently written as .rnw, and compiled using knitr and beamer  
### Labs  
Written in .rmd, compiled using the teachR::make.sheet() function to create separate htmls with/without solutions.

## Multivariate  
### Lectures  
### Labs  
  




