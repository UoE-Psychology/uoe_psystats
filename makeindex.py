""" Build index from directory listing

make_index.py </path/to/directory> [--header <header text>]
"""

from __future__ import print_function
import os.path, time
import os
import argparse
# May need to do "pip install mako"
from mako.template import Template



INDEX_TEMPLATE = r"""

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>
<meta name="keywords" content="" />
<meta name="description" content="" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700,800" rel="stylesheet" />
<link href="${site}/default.css" rel="stylesheet" type="text/css" media="all"/>

</head>
<body>
<div id="header-wrapper">
	<div id="header" class="container">
		<div id="logo">
			<h1><a href="https://uoe-psychology.github.io/uoe_psystats/">University of Edinburgh</a></h1>
		</div>
		<div id="menu">
			<li><a href="mailto:ug.ppls.stats@ed.ac.uk" target="_top">Contact Us (UG)</a></li>
			<li><a href="mailto:pg.ppls.stats@ed.ac.uk" target="_top">Contact Us (PG)</a></li>
        </div>
	</div>
</div>

<!---<div id="header-featured">--->
</div>
	<div id="banner-wrapper">
		<div id="banner" class="container">
            <h2>Data Analysis for Psychological Research</h2>
			<span>Psychology Department, 7 George Square</span>
        </div>
	</div>
<div class="bannerbox">
    <span class="bannerbox-${headcol}"></span>
</div>

<div id="wrapper">
	<div id="featured-wrapper">
		<div id="featured" class="container">
            <ul style="text-align:left">
                <li>${dirlabs.get(headcol)}</li>
                <li><a href="../">Back</a></li>
            </ul>
            <div class="containerdirs">
            <div class="description">
                <h3>${dirdesc.get(headcol2,"")}</h3>
            </div>
			% for name in dirnames:
                <div class="column1">
                    <div class="title"><a href="${name}"><span class="icon icon-${name}"></span></a>
                        <h2><a href="${name}">${dirlabs.get(name)}</a></h2>
                    </div>
                </div>
			% endfor
			</div>
		</div>
    </div>
    <div id="page" class="container">
		<div class="sbox1">
			<!---<h2>Files</h2>--->
			<ul class="style2">
			% for name in filenames:
				<li class="icon icon-ok"><a href="${name}">${name}</a></li>
            % endfor
			</ul>
           </div>
	</div>
</div>
<div id="footer-wrapper"></div>
</body>
</html>
"""


EXCLUDED = ['index.html','style.css','readme.txt','images','fonts','default.css','data','functions','labsheets']
EXCLUDEDDIR = ['book','book_sols']

dlabs={'': 'Home',
       'dapr1':'Data Analysis in Psychology using R 1',
       'dapr2':'Data Analysis in Psychology using R 2',
       'dapr3':'Data Analysis in Psychology using R 3',
       'usmr':'Univariate Statistics & Methodology in R',
       'multivar':'Multivariate Statistics & Methodology in R',
       'book':'Course Book',
       'lectures':'Lecture Slides',
       'labsheets':'Labs'}
#<h2><a href="${name}">${dirlabels[name]}</a></h2>

ddesc={'': 'The Department of Psychology at the University of Edinburgh offers 3 Undergraduate Courses in statistics, and 2 postgraduate courses. ',
       'dapr1':'Data Analysis in Psychology using R-1 is a year-long course providing foundations in working with data, probability, hypothesis testing and the use of R.<br><br>The course is taught based on a mixture of lectures, labs and structured independent learning tasks.<br>The course begins by covering the fundamental principles of describing data and of probability theory. It then builds to a discussion of how we make inferences about our hypotheses in psychology, dealing with probability distributions, sampling and hypothesis testing, and introduces simple statistical tests for two variables by way of example.<br><br>The labs also introduces the fundamental principles of programming in R, taking students from basic calculations to the foundations of data management, plotting and use of simple statistical tests.',
       
       'dapr2':'Data Analysis in Psychology using R 2 will arrive in the 2020-21 academic year.',
       'dapr3':'Data Analysis in Psychology using R 3 will arrive in the 2021-22 academic year.',
       
       'usmr':'Univariate Statistics & Methodology in R is a semester long course that is provided for students following Masters programmes in Psychology and Linguistics. It starts with an introduction to basic statistics and the basics of R programming, and will give student competence in the standard univariate methodology and analysis using R.<br><br>Design and analysis are taught under a unifying framework which shows a) how research problems and design should inform which statistical method to use and b) that all statistical methods are special cases of a more general model. The course concentrates on research designs and analysis for problems in which there is a single outcome variable and would be taught using the general linear model as a framework to design and analysis.<br><br>Content covered includes: Introduction to the use of statistical methods in research; Introduction to R for statistics; Refresher in inferential statistics including Hypothesis testing, Type I vs. Type II errors, p-values, power, correlation, chi-squares; Linear regression: including diagnostics, transformation, different families of models; Multiple regression: extending linear regression to multiple IVs and including interactions, effects coding; The general linear model (GLM) as an inclusive framework (including ANOVA, ANCOVA, mixed designs)',
       
       'multivar':'Multivariate Statistics & Methodology in R is a semester long course providing an advanced level overview of statistical analysis techniques and methodology issues relevant to psychological research. The course builds on the concepts and skills developed in Univariate Statistics and Methodology using R.<br><br>Multivariate Statistics and Methodology using R uses a problem-oriented approach to introduce analysis tools that extend to cases where multiple outcome variables are being studied simultaneously, and cases where the data contain a structure, e.g. children nested in classes, in schools, or more complex cases.<br><br>Content covered includes: Linear Mixed Modelling; Growth Curve Analysis; Principal Component Analysis; Factor Analysis; Path Analysis; Structural Equation Modelling',
       
       'dapr1lectures':'Coming soon..',
       'dapr2lectures':'Coming soon..',
       'dapr3lectures':'Coming soon..',
       'usmrlectures':'Coming soon..',
       'multivarlectures':'Coming soon..'
       }





def fun(dir,rootdir):
    print('Processing: '+dir)
    filenames = [fname for fname in sorted(os.listdir(dir)) if fname not in EXCLUDED and os.path.isfile(dir+fname)]
    dirnames = [fname for fname in sorted(os.listdir(dir)) if fname not in EXCLUDED]
    dirnames = [fname for fname in dirnames if fname not in filenames]
    dirorder = ["dapr1","dapr2","dapr3","usmr","multivar"]
    dirnames = [x for x in dirorder for y in dirnames if y == x] + [y for y in dirnames if y not in dirorder]
    
    #dirlabels = {**{k: dlabs[k] for k in dirnames if k in dlabs}, **{k:k for k in dirnames if k not in dlabs}}
    dirlabels = {**dlabs, **{k:k for k in dirnames if k not in dlabs}}
    dirdescriptions = {**ddesc, **{k:k for k in dirnames if k not in ddesc}}
    
  
    #header = os.path.basename(dir)
    f = open(dir+'/index.html','w')
    print(Template(INDEX_TEMPLATE).render(dirnames=dirnames,dirlabs=dirlabels,
                                          dirdesc=dirdescriptions,
                                          filenames=filenames,
                                          header=dir.replace("docs/","Home"),
                                          headcol=dir.split("/")[2],
                                          headcol2=''.join(dir.split("/")[2:]),
                                          site="https://uoe-psychology.github.io/uoe_psystats/",
                                          ROOTDIR=rootdir,time=time.ctime(os.path.getctime(dir))),file=f)
    f.close()
    
    for subdir in [dirnames for dirnames in dirnames if dirnames not in EXCLUDEDDIR]:
        try:
            fun(dir+subdir+"/",rootdir+'../')
        except:
            pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--header")
    args = parser.parse_args()
    fun(args.directory+'/','../')

if __name__ == '__main__':
    main()
