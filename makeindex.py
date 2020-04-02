""" Build index from directory listing

make_index.py </path/to/directory> [--header <header text>]
"""
from __future__ import print_function
import os.path, time

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
                <li>${header}</li>
                <li><a href="../">Back</a></li>
            </ul>
            <div class="containerdirs">
			% for name in dirnames:
                <div class="column1">
                    <div class="title"><a href="${name}"><span class="icon icon-${name}"></span></a>
                        <h2><a href="${name}">${name}</a></h2>
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

EXCLUDED = ['index.html','style.css','readme.txt','images','fonts','default.css']
EXCLUDEDDIR = ['book','book_sols']

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template

def fun(dir,rootdir):
    print('Processing: '+dir)
    filenames = [fname for fname in sorted(os.listdir(dir))
              if fname not in EXCLUDED and os.path.isfile(dir+fname)]
    dirnames = [fname for fname in sorted(os.listdir(dir))
            if fname not in EXCLUDED  ]
    dirnames = [fname for fname in dirnames if fname not in filenames]
#    header = os.path.basename(dir)
    f = open(dir+'/index.html','w')
    print(Template(INDEX_TEMPLATE).render(dirnames=dirnames,filenames=filenames,
                                          header=dir.replace("docs/","Home"),
                                          headcol=dir.split("/")[2],
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
