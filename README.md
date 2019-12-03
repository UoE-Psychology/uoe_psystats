# University of Edinburgh Psychology Statistics Course Content  

In each course directory, there are subdirectories for lectures, labs, and lab_solutions (where necessary).  
  
## /docs  
Any finished **and rendered**  materials should be placed in the /docs directory.  
  
A github page is built from this repository, meaning that any .htmls are rendered appropriately. (in the future, /docs could be replaced by submodule of proper site such as Milan's one).   

In a browser, navigating to [https://uoe-psychology.github.io/uoe-psystats](https://uoe-psychology.github.io/uoe_psystats) with the filepath within /docs will show you your published file.   
  
There is an index.html, but to update this you need to run the makeindex.py script on /docs.  It will ignore any directory named "book" (to ensure the index.html doesn't get overwritten).  

## Colours  
- DAPR1: #6BCDED    
- DAPR2: #B38ED2  
- DAPR3:  
- USMR: #FCBB06  
- MSMR: #072448  


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
> devtools::install_github("UoE-Psychology/teachR")  

## Multivariate  
### Lectures  
### Labs  
  




