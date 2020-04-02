# University of Edinburgh - School of Psychology<br>Statistics Courses

---
Structure of the document  
============================  
<!--ts-->
1. [Welcome](#welcome)  
1. [Purpose of this repository](#purpose)  
1. [Repository structure](#structure)
1. [How do I contribute?](#contribute)
1. [Introduction to version control systems](#intro-git)  
1. [Writing](#writing)  
1. [Publishing](#publishing)  
1. [Accessing](#accessing)  
1. [Linking from Learn or external](#linking-eg-from-learn)  
<!--te-->

---

## <a name="welcome"></a>Welcome

Welcome to the GitHub repository for the Statistics courses of the School of Psychology of the University of Edinburgh!

The purpose of this repository is to have a unique place where up-to-date documents are stored (lecture or labs), and new content is drafted.
The centralised structure will help people finding the content that you developed, even if you will not be teaching the course in one particular year.
Most importantly, by linking Learn to links to this page, students will always see **up-to-date content**. Did students flag a typo in your lecture slides? Don't worry! You just need to update the file here and there is no need to re-upload everything on Learn all the time.

The next sections will introduce you to the structure of this directory, introduce you to version control systems, explain where to write your material and how to publish it online. Next, it will explain how to access the material you have prepared and how to link it to Blackboad Learn to make it visible to your students.

Thanks for reading!


## Purpose of this repository

The goal of this online repository is to store up-to-date content of lectures and labs so that you can just share a link to the course content on Learn, and students are taken to the most recent version (perhaps you fixed a typo).

The repository name is `uoe_psystats` and is stored on the [GitHub](https://github.com/) website. The repository is managed by the GitHub account `UoE-Psychology`, which is operated by the Statistics Senior Teaching Coordinators.


## Repository structure

The repository is stored under the account `UoE-Psychology` and is called `uoe_psystats`.
The repository link is https://github.com/UoE-Psychology/uoe_psystats

Going to this link will take you to the **master** branch of the folder.
You can think of a repository as a tree structure. The master branch is the most important one. You could in theory create a copy the master branch, which would be a side-branch, and call it for example `development`, on which you want to develop a specific course. However, as the folder has course-specific subfolders, there should be no need for that.

The repository has different course-specific subfolders:

- **dapr1** (course content for the UG course Data analysis for Psychology in R 1)
- **dapr2** (course content for the UG course Data analysis for Psychology in R 2)
- **dapr3** (course content for the UG course Data analysis for Psychology in R 3)
- **univar** (course content for the PG course Univariate statistics and methodology in R)
- **multivar** (course content for the PG course Multivariate statistics and methodology in R)

And a special subfolder named

- **docs**

The subfolder **docs** has, in turn, a subfolder for each of the courses above.

It is good practice to develop course material in the course-specific folders on the master branch.

Once you have finished developing the material and want to make it publishable online, copy the material on the **docs/<COURSE NAME>** subfolder. These will be the live contents that students will see from Learn.


## How do I contribute?

1. Obtain a GitHub account
2. Copy the online repository from GitHub to your PC
3. Create or edit course material on the local copy of the repository
4. Make sure to transfer your work to the repository stored online on GitHub


**Step 1. Obtain a GitHub account.**
If you are involved with teaching or tutoring quantitative courses in this school, the first thing you should do is to register for a GitHub account:

1. Go to [GitHub](https://github.com/)
2. Click "Sign up" on the top right corner
3. Choose a username, and write your academic email and password
4. Once you have created an account it is good practice to [verify yourself as an educator](https://education.github.com/)

You will use your GitHub account in order to contribute to the statistics repository.

**Step 2. Obtain a GitHub account.**


## Introduction to version control systems



# Writing   


#### Templates

In the `templates/` directory, you will find different examples for writing lectures, labs, and reports.  All of which are written in Rmarkdown.   

- Lectures are compiled as `.html`  
- Labs are compiled into a bookdown (a `.html` book with each lab as a chapter). The option also exists to build to `.pdf` should printouts be required.  
- Reports are compiled to `.pdf`

**Important:** Do not use this repository to store actual reports. Everything here is public!  

#### Course colour schemes  

Our courses use the following colour schemes:

- DAPR1: ![](https://placehold.it/15/6BCDED/000000?text=+) `#6BCDED`
- DAPR2: ![](https://placehold.it/15/e41a1c/000000?text=+) `#e41a1c`
- DAPR3: ![](https://placehold.it/15/4daf4a/000000?text=+) `#4daf4a`
- USMR: ![](https://placehold.it/15/FCBB06/000000?text=+) `#FCBB06`
- MSMR: ![](https://placehold.it/15/a41ae4/000000?text=+) `#a41ae4`

Where possible, all materials (lectures, labs, reports etc.) corresponded to given course will follow the designated colour scheme.  
How to set the colour scheme for each course is detailed in the sections below explaining how to write different types of content.  

### Lectures

For lectures, the template we provide uses [`xaringan` package](https://github.com/yihui/xaringan).  

You can find a tutorial on how to produce slides using `xaringan` [here](https://slides.yihui.org/xaringan/#1).  

```{r}
install.packages('xaringan')
devtools::install_github("gadenbuie/xaringanthemer")
```

#### Setting the course colour  

At the top of each lecture `.Rmd`, there is a code chunk which sets the colour for the slides:     

```{r xaringan-themer, include = FALSE}
library(xaringanthemer)
mono_accent(
  base_color = "#0F4C81",
  header_color = "#000000",
  header_font_google = google_font("Roboto Condensed"),
  text_font_google   = google_font("Roboto", "300", "300i"),
  code_font_google   = google_font("Source Code Pro")
)
```

Set the `base_color` to the appropriate hex-code for the course you are writing for.  


### Labs

Our labs are written and compiled as bookdowns, but also built as `.pdfs` should students require printouts.

Each lab begins with the same structure:

- Link to lecture slides
- Link to .pdf version
- Learning objectives
- Readings

After that point, courses vary in lab structure - some contain walkthroughs, some are just questions.  

#### Drop-down questions/solution boxes  

Our labsheets have the ability to include dropdown question and solution boxes.  

To write a question:    
```
`r qbegin()`  
This is the question. It will have a heading of "Question"
`r qend()`  
```

You can add question numbers/labels, using:
```
`r qbegin(1)`  
This Q will end up with a heading of "Question 1"
`r qend()`  

`r qbegin("example 1",qlabel=FALSE)`  
This Q will end up with a heading of "example 1"
`r qend()`  
```

To include solutions:  
```
`r solbegin(show=TRUE)`  
This is the solution. When rendered, it will be visible, and it will have a heading of "Solution"  
`r solend(show=TRUE)`  

`r solbegin(show=FALSE)`  
This is the solution. When rendered, it will NOT be visible
`r solend(show=FALSE)`  

`r solbegin(show=TRUE, label="peppapig 1", slabel=FALSE)`  
This is the solution. When rendered, it will be visible, and it will have a heading of "peppapig 1".
`r solend(show=TRUE)`  
```

You can render with and without solutions shown by setting a variable such as HIDE_SOLUTIONS at the top of each lab which is either TRUE/FALSE, and then passing that variable to the `solbegin()` and `solend()` functions (e.g., `r solbegin(show=HIDE_SOLUTIONS)`).

#### Setting the course colour  

Open the `index.Rmd` for the bookdown.  
In the yaml front matter at the top of this file, the title contains reference to images which are held in the `images/` directory of the bookdown.  

This adds to the title a coloured square corresponding to the course colour scheme. The number of squares corresponds to the year to which the course is offered.  

For instance, for dapr2, two squares are included:  
```
---
title: |
  ![](images/dapr2.png){width=0.51in}
  ![](images/dapr2.png){width=0.51in}
  <br>
  Data Analysis for Psychology in R 2
author: "School of Psychology, The University of Edinburgh"
```

Edit the path to call the appropriate course image the appropriate number of times.  

#### Compiling  

To compile to `.html`, open the `index.Rmd` and click knit. This will call `bookdown::render_book()`.  

To build both `.html` and `.pdf`: in Rstudio menu: Build > Build All.

All rendered files can be found in the `_book/` directory.  


## Publishing  

Any finished **and rendered**  materials should be placed in the `docs/` directory.  

Place the compiled `.html` files (or **entire contents** of the `_book/` directory, if publishing a bookdown) into the appropriate subdirectory of `docs/`.  

## Accessing  

A github page is built from the `docs/` directory, meaning that any `.html` within `docs/` are rendered appropriately and can be linked to from elsewhere.

In a browser, navigating to [https://uoe-psychology.github.io/uoe_psystats](https://uoe-psychology.github.io/uoe_psystats) will take you to the the published homepage (equivalent to `docs/`).  

To access your published material, simply append the appropriate filepath to this url.   
For example, if you have put a lecture titled `dapr2-lecture3.html` inside `docs/dapr2/lectures/`, then https://uoe-psychology.github.io/uoe_psystats/dapr2/lectures/dapr2-lecture3.html will take you to the published file.  

The version of the site you see in a browser **will not** automatically update to show files which you add to `docs/`.  To update this requires running `makeindex.py docs/`.  This script will update the pages, excluding any directories named `BOOK` and  
There is an index.html, but to update this you need to run the makeindex.py script on /docs.  It will ignore any directory named `book/` or `book_sols/` (to ensure that necessary `index.html` files doesn't get overwritten).  

## Linking (e.g. from Learn)  

To link to the pages, simply navigate to the appropriate path at [https://uoe-psychology.github.io/uoe_psystats](https://uoe-psychology.github.io/uoe_psystats), and create a link in Learn.  

Links between lectures and labs follow the same procedure. For instance, to include a link in a lab to a lecture:

```{r}

The lecture slides are available
[here](https://uoe-psychology.github.io/uoe_psystats/dapr1/lectures/lecture1.html)

```
