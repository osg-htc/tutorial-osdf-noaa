# training-osdf-climate

## Notes

examples from Emma: https://github.com/NCAR/osdf_examples
* This looks like the simplest to implement: https://github.com/NCAR/osdf_examples/blob/main/notebooks/ndc_workflows/sonar_ai.ipynb
* these would need to be detangled from the PBS stuff:
    * https://github.com/NCAR/osdf_examples/blob/main/notebooks/geocat_climatology.ipynb
    * https://github.com/NCAR/osdf_examples/blob/main/notebooks/cesm_oceanheat.ipynb

## To Dos
- make a simple version of the sonar viz script that takes in an input file and produces a visualization
- determine what software dependencies need to be added to the jupyter environment
- get a list of potential input files we could use
- Once we decide on inputs, make a mirror somewhere in space we control
- confirm outline with everyone
- make a container?

## Outline
 
## Notebook 1: basic client use

- define each component of a pelican / OSDF URL (markdown text)
- list the key verbs for interacting with objects (markdown text)
- apply knowledge to get an object, create an output, and put it somewhere.
    - randomly assign a URL to each person via * magic *
    - have them get a file
    - run the script that visualizes the data
    - put the resulting file back into a common origin
    - use pelican ls
    - pull someone else's visualization + look at it. 

## Notebook 2: basic fsspec example

- same as above, but all in the notebook? 🤔
- Anything else to highlight? 

## Notebook 3: submitting jobs

- motivation: want to do this for thousands of files
    - review the list command on the input origin
    - identify what we need to run at scale
- drill down to one job: conceptual overview - origins as where data goes/comes from as part of jobs
    - make a diagram. Excalidraw? 
- identify key config / ingredients in submit file
    - map concepts to submit file lines
    - introduce variables / queue from our list
- go through submit file together
- submit a bunch of jobs. what could go wrong. 
